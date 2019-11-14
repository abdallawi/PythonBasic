import requests
from bs4 import BeautifulSoup

# Makes sense:

endpoint = 'https://www.alternate.be/html/search.html?query=M.2+2280&x=0&y=0'

# 1. This program is intended to scrape the prices from certain products [M.2 && SSD] on alternate

respons = requests.get(endpoint)
soup = BeautifulSoup(respons.text, 'html.parser')
container = soup.select('.productLink')

# 2. Should map the prices, model, brand into a csv file

for tag in container:
    print(tag.attrs)

# 3. Produce a meaningful graph from this data

# 4. Predict if prices are going to drop over the coming weeks [at least 2]
