"""
Print out a list of all the article titles on the Japan Times homepage: https://www.japantimes.co.jp/

"""

import requests
from bs4 import BeautifulSoup


url = 'https://www.japantimes.co.jp/'
r = requests.get(url)
r_html = r.text


soup = BeautifulSoup(r_html, 'html.parser')


for headline in soup.find_all('p', class_='article-title'):
    print(headline.text.strip())