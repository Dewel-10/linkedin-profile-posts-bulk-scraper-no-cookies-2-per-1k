import json
import threading
import queue
import logging
from pathlib import Path

from extractors.linkedin_posts_parser import LinkedInPostParser
from outputs.exporters import save_json

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def worker(task_queue: queue.Queue, results: list):
    parser = LinkedInPostParser()
    while True:
        try:
            url = task_queue.get_nowait()
        except queue.Empty:
            return
        try:
            logging.info(f"Processing URL: {url}")
            result = parser.scrape(url)
            results.append(result)
        except Exception as e:
            logging.error(f"Failed to scrape {url}: {e}")
        finally:
            task_queue.task_done()

def main():
    input_file = Path("data/inputs.sample.txt")
    if not input_file.exists():
        logging.error("Input file not found: data/inputs.sample.txt")
        return

    urls = [line.strip() for line in input_file.read_text().splitlines() if line.strip()]
    if not urls:
        logging.error("No URLs found in input file.")
        return

    task_queue = queue.Queue()
    for url in urls:
        task_queue.put(url)

    results = []
    threads = []
    thread_count = min(6, len(urls))

    for _ in range(thread_count):
        t = threading.Thread(target=worker, args=(task_queue, results))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    save_json("output.json", results)
    logging.info("Scraping completed. Results saved to output.json")

if __name__ == "__main__":
    main()