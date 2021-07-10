# learning to being an expert #
from bs4 import BeautifulSoup
import requests

url = requests.get('https://www.teamfortress.com/').text
soup = BeautifulSoup(url, 'html')

