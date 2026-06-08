# Project 2: Accra Craigslist Website

# Import libraries
import requests
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
# print(soup.prettify())

# Find element
search_results = soup.find_all('li', class_='cl-static-search-result')
extracted_data = []      # Empty list for data addition

# Loop through the results and extract the title, price , location and link for each listing
for result in search_results:
    # Extract link
    link_tag = result.find('a')
    link = link_tag['href'] if link_tag else None
    # Extract title
    title = result.get_text(strip=True)
    # Extract price
    price_tag = result.find('div', class_='price')
    price = price_tag.get_text(strip=True)
    # Extract location
    location_tag = result.find('div', class_="location")
    location = location_tag.get_text(strip=True)

    extracted_data.append({"Name": title,
                           "Link": link,
                           "Location": location,
                           "Price": price})


# print(extracted_data)

# Save DataFrame to CSV file
df = pd.DataFrame(extracted_data)
print(df)
df.to_csv('accra_craigslist.csv', index=False)
