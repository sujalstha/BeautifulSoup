# learning to being an expert #
from bs4 import BeautifulSoup
import requests
import lxml

url = requests.get('https://www.soccerstats.com/').text
soup = BeautifulSoup(url, 'lxml')
id_find = soup.find_all('div')
tbs = soup.find_all('seven columns')
tb = soup.find_all('td').text()

for tbs in id_find:
    for tb in tbs:
        print(tb)

'''all_text_tf_website = []

for href in id_find:
    text_tf_web = href.text.replace('\n', '')
    all_text_tf_website.append(text_tf_web)

r_text = ''

del all_text_tf_website[:4]

text_tf_website = [s for s in all_text_tf_website if s != '']

with io.open("tf2 website text.txt", 'w', encoding="utf-8") as text_file:
    text_file.write("\n".join(text_tf_website))'''

