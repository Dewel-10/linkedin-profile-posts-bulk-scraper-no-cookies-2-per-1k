import json
import logging
from pathlib import Path

def save_json(filename: str, data):
    try:
        Path(filename).write_text(json.dumps(data, indent=2))
        logging.info(f"Saved output to {filename}")
    except Exception as e:
        logging.error(f"Failed to save JSON: {e}")