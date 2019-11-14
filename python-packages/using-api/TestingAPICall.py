import requests
from bs4 import BeautifulSoup

# Makes sense:

url = 'https://www.themoviedb.org/discover'
query = '/movie?primary_release_date.gte=2019-04-15&primary_release_date.lte=2019-04-21'

# Fetch our data:

resp = requests.get(url+query)
soup = BeautifulSoup(resp.text, 'html.parser')
container = soup.select('.result')

for tag in container:
    if tag['class'] == ['title', 'result']:
        print(tag['title'])
    # print(tag.attrs)
