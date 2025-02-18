#Day 87: Web crawler


#Create a web crawler or web scraper.

#Advanced 

import requests
from bs4 import BeautifulSoup
import time

visited = set()  # Track visited links

def crawl(url, depth=2):
    if depth == 0 or url in visited:
        return
    
    print(f"Crawling: {url}")
    visited.add(url)

    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract and print page title
        title = soup.find("title")
        print(f"Title: {title.get_text() if title else 'No title'}\n")

        # Find and follow all links
        for link in soup.find_all("a", href=True):
            next_url = link["href"]
            if next_url.startswith("http"):
                time.sleep(1)  # Be respectful, avoid spamming
                crawl(next_url, depth - 1)

    except Exception as e:
        print(f"Error: {e}")

# Start crawling from an initial URL
crawl("https://example.com", depth=2)
