import requests
from bs4 import BeautifulSoup
import pprint

domain = 'https://dedmorozural.ru'
url = f'{domain}/novosti'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

result = {}
titles = []
news_tag = soup.find_all('a', class_='con_titlelink')
for new in news_tag:
    text = new.text
    href = new.get('href')
    # print(text, href)
    # шаг 2
    url = f'{domain}{href}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # получаем заголовки
    new_titles_tag = soup.find_all('h1', class_='con_heading')

    for new_title_tag in new_titles_tag:
        # print(new_title_tag.text)
        titles.append(new_title_tag.text)

        # добавим в словарь
        result['text'] = titles

pprint.pprint(result)
