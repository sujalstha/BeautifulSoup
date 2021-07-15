# learning to being an expert #
from bs4 import BeautifulSoup
import requests
import lxml

url = requests.get('https://www.teamfortress.com/').text
soup = BeautifulSoup(url, 'lxml')
id_find = soup.find_all('div')
href = soup.find_all('href')
# text = id_find.id.text

all_text_tf_website = []

for href in id_find:
    text_tf_web = href.text.replace('\n', '')
    all_text_tf_website.append(text_tf_web)

r_text = ''

del all_text_tf_website[:4]

text_tf_website = [s for s in all_text_tf_website if s != '']

text_file = open("tf2 website text.txt", 'w')