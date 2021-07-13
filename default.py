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

for lis in all_text_tf_website:
    if '' in lis:
        print(lis)
    else:
        pass


def remove_items(test_list, item):
    rest = [i for i in test_list if i != item]
    return rest


if __name__ == "__main__":
    item = ''
    res = remove_items(all_text_tf_website, item)
    print(str(res))
