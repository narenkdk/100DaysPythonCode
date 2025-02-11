#Day 80: Web scraping


#Write a script to scrape data from a website.


import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://example.com/news"  # Replace with the target website

# Send a GET request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all article titles (Modify the tag and class as needed)
    articles = soup.find_all("h2", class_="article-title")
    
    # Print extracted titles
    for index, article in enumerate(articles, 1):
        print(f"{index}. {article.get_text(strip=True)}")
else:
    print("Failed to retrieve the webpage")
