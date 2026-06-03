# Project 1: Customer Reports/ Consumer Reports
import requests
import html5lib
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 "
                         "(Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, likeGecko) "
                         "Chrome/119.0.0.0 Safari/537.36"
           }
base_url = "https://www.consumerreports.org/"

response = requests.get(base_url, timeout=20, headers=headers)

soup = BeautifulSoup(response.content, "html5lib")

print(soup.prettify())
