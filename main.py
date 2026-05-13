# Web Scraping With Beautiful Soup

# requests
# html5lib
# bs4

import requests
import html5lib
from bs4 import BeautifulSoup

# Define a header to mimic a real browser
headers = {"User-Agent": "Mozilla/5.0 "
                         "(Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, likeGecko) "
                         "Chrome/119.0.0.0 Safari/537.36"
           }
url = "https://en.wikipedia.org/wiki/Fallacy"

response = requests.get(url, timeout=10, headers=headers)

soup = BeautifulSoup(response.content, "html5lib")
print(soup.prettify())
