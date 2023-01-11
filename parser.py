"""пример работы с beautifulsoup"""
# 1.  регулярные выражения
# 2. сторонние билиотеки beautifulsoup, lxml
# 3. scrapy

import requests
from bs4 import BeautifulSoup

url = "https://dedmorozural.ru/novosti"
response = requests.get(url)
# print(response.status_code)
# print(response.text)


# Создаем суп для разбора html
soup = BeautifulSoup(response.text, 'html.parser')

# получем тэг тайтл
# print(soup.title)
#
# # bs4.element.Tag
# print(type(soup.title))
#
# # через точку находим первый тэг
# print(soup.a)
#
# # чтобы получить текст внутри тэга
# print(soup.a.string)
# # str
# print(soup.a.text)
#
# # атрибут найти
# print(soup.a.get('href'))

# найти все тэги
# print(soup.findAll('a'))
#
# images_tags = soup.findAll('img')
# for images_tag in images_tags:
#     print(images_tag)

# поиск по классу - самое основное

big_body_tag = soup.find('div', class_='modulebody1')

# 1 вариант искать по классу - норм
# 1.1 вариант искать уже в найденном
modulebody3 = big_body_tag.find('div', class_='modulebody3')
# print(modulebody3)
# print(big_body_tag)


# 2 если не полчается искать по классу или по тэгу, то придется искать по порядку
# .contents
# print(big_body_tag.contents)
# print(len(big_body_tag.contents))
# прыжки по модуль боди
print(big_body_tag.contents[1].contents[1].contents)

print(big_body_tag.contents[1].contents)


print('*'*50)
# получение своих детей
for child in big_body_tag.children:
    print(1)
    print(child)

 # рекурсивные дети
print('*' * 50)
for child in big_body_tag.descendants:
    print(0)
    print(child)
