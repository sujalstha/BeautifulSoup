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
    text_tf_web = [href.text.replace('\n', '')]
    all_text_tf_website.append(text_tf_web)

r_text = ''
'''for lis in all_text_tf_website:
    if lis == str(r_text):
        all_text_tf_website.remove(r_text)

print('List 2: \n', all_text_tf_website)


list(filter(lambda a: a != '', all_text_tf_website))

print(all_text_tf_website)'''

for ele in all_text_tf_website:
    for lis in ele:
        print(lis)