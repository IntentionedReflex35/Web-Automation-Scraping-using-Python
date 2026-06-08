# Project 2: Accra Craigslist Website

# Import libraries
import requests
import html5lib
from bs4 import BeautifulSoup
import pandas as pd

headers = {"User-Agent": "Mozilla/5.0 "
                         "(Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, likeGecko) "
                         "Chrome/119.0.0.0 Safari/537.36"
           }

# Accessing website
base_url = "https://accra.craigslist.org/search/rea#search=2~gallery~0"
response = requests.get(base_url, timeout=20, headers=headers)
soup = BeautifulSoup(response.content, "html5lib")

# Get content
print(soup.prettify())
