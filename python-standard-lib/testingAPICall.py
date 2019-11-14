import requests
from bs4 import BeautifulSoup

url = 'https://www.themoviedb.org/discover'
query = '/movie?primary_release_date.gte=2019-11-1&primary_release_date.lte=2019-22-14'

#Fetch our data:

resp = requests.get(url+query)
print(type(resp), resp.text)
soup = BeautifulSoup(resp.text, 'html.parser')
container = soup.select('.result')

for tag in container:
    if tag['class'] == ['result', '']:
        print()