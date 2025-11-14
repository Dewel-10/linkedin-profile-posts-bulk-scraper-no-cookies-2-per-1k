import logging
import time
import random
from .utils_datetime import now_timestamp

class LinkedInPostParser:
    """
    Mock LinkedIn scraper producing structured output.
    Replace fetch logic with real scraping as needed.
    """

    def scrape(self, url: str) -> dict:
        logging.info(f"Fetching LinkedIn post data from: {url}")

        # Simulated network delay
        time.sleep(random.uniform(0.3, 0.8))

        return {
            "type": "post",
            "id": str(random.randint(7000000000000000000, 7999999999999999999)),
            "linkedinUrl": url,
            "content": "This is simulated post content extracted from LinkedIn.",
            "author": {
                "publicIdentifier": "mock-user",
                "name": "Mock User",
                "info": "Automation Tester"
            },
            "postedAt": {
                "timestamp": now_timestamp(),
                "date": time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
            },
            "engagement": {
                "likes": random.randint(10, 500),
                "comments": random.randint(0, 100),
                "shares": random.randint(0, 50)
            },
            "reactions": [
                {
                    "reactionType": "LIKE",
                    "actor": {"name": "Sample Reactor"}
                }
            ],
            "comments": [
                {
                    "id": str(random.randint(7000000000000000000, 7999999999999999999)),
                    "commentary": "This is a mock comment for testing.",
                    "actor": {"name": "Commenter User"}
                }
            ]
        }