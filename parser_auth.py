import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPDigestAuth
from requests.auth import HTTPBasicAuth

domain = 'https://dedmorozural.ru'
url = f'{domain}/novosti'

headers = {
    'accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / avif, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3;q = 0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'cookie': '_ym_uid=1673249962549307735; _ym_d=1673249962; PHPSESSID=91914949032709a1b618b90380ec3597; _ym_isad=1; InstantCMS[logdate]=1673337102; InstantCMS[userid]=00cb7b95006f9aa9c861d9fc32fba967',
    'referer': 'https://dedmorozural.ru/login',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

# response = requests.get(url, auth=HTTPDigestAuth('DanteOnline', 'dywtbofywed'))
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

span = soup.find('span', class_='register')
print(span)

span = soup.find('span', class_='my_profile')
print(span)
