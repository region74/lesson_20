import requests
from bs4 import BeautifulSoup
import pprint
import json

domain = 'https://74.ru'
url = f'{domain}/text/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

news_tag = soup.find_all('h2', class_='h9Jmx')
news_date = soup.find_all('time', class_='_2DfZq')

list_news = []
list_date = []

for new in news_tag:
    list_news.append(new.text)

for new in news_date:
    list_date.append(new.text)

with open('data.json', 'a') as f:
    for i in range(len(list_news)):
        result = f'{list_news[i]} ***** {list_date[i]}\n'
        # tmp = json.dumps(result)
        json.dump(result, f)
        print(result)

with open('log_news.txt', 'w') as f:
    for i in range(len(list_news)):
        result = f'{list_news[i]} ***** {list_date[i]}\n'
        # tmp = json.dumps(result)
        f.writelines(result)

# print('*' * 500)
# with open('data.json', 'r') as f:
#     result = json.loads(f)
#     print(result)
