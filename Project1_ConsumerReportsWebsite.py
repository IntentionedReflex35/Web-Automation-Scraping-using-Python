# Project 1: Customer Reports/ Consumer Reports
# Import libraries
import requests
import html5lib
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 "
                         "(Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, likeGecko) "
                         "Chrome/119.0.0.0 Safari/537.36"
           }

# Get response
base_url = "https://www.consumerreports.org/"
response = requests.get(base_url, timeout=20, headers=headers)
soup = BeautifulSoup(response.content, "html5lib")

# Accessing the url
cards = soup.find_all('div', attrs={'class': 'border-t border-gray-light first:border-t-0 group'})
link_list = []      # Store all links here

for card in cards[1:]:
    link_tag = card.find('a')
    if link_tag:
        # Get the text
        text = link_tag.get_text(strip=True)
        # Get the full link
        link = base_url + link_tag['href']
        link_list.append(link)

# in-this-article list
for link in link_list:
    response = requests.get(link, timeout=20, headers=headers)
    soup = BeautifulSoup(response.content, "html5lib")
    in_this_article = soup.find_all('div', attrs={'id': 'in-this-article-3'})
    print(in_this_article)
