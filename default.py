# learning to being an expert #
from bs4 import BeautifulSoup
import requests
import lxml

url = requests.get('https://www.teamfortress.com/').text
soup = BeautifulSoup(url, 'lxml')
id_find = soup.find_all('div')
text = id_find.href.p.text
print(text)
