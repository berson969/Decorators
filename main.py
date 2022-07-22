import bs4
from fake_headers import Headers
from requests import get
from datetime import datetime
import re
from decor_logger import decor_logging

# KEYWORDS = ['биткоин', 'Транзакции', 'слайдер']
KEYWORDS = ['API', 'фото', 'размер' 'биткоин','Транзакции', 'python', 'образ', 'все', 'БПФ']
KEYWORDS_SET = set(KEYWORDS)
HEADERS = Headers(browser='chrome', os="mac", headers=True).generate()
url = 'https://habr.com/ru/all/'
PATTERN = '[^A-Za-zА-Яа-яё\ ]'


@decor_logging
def find_href(article):
    href = article.find(class_="tm-article-snippet__title-link").attrs['href']
    return f"https://habr.com{href}"


@decor_logging
def check_and_print(title, text_for_check, article):
    text_for_check1 = re.sub(PATTERN, ' ', text_for_check)
    # print()
    if set(text_for_check1.split(sep=' ')).isdisjoint(KEYWORDS_SET) is False:
        date_realese = article.find(class_="tm-article-snippet__datetime-published").find('time').attrs['datetime']
        date_realese = datetime.strptime(date_realese, '%Y-%m-%dT%H:%M:%S.%fZ')
        print(f'СТАТЬЯ => {date_realese.date()}  {title.text}   {find_href(article)}')
        return True


response = get(url, headers=HEADERS).text
soup = bs4.BeautifulSoup(response, features='html.parser')
articles = soup.find_all('article')
# print(response)
for article in articles:
    title = article.find(class_="tm-article-snippet__title-link").find('span')
    res = check_and_print(title, title.text, article)
    if res is None:
        bodies = article.find(class_="tm-article-body tm-article-snippet__lead")
        for body in bodies.find_all('p'):
            if res is None:
                res = check_and_print(title, body.text, article)
                #  ищет внутри статьи
        if res is None:
            response2 = get(find_href(article), headers=HEADERS).text
            soup2 = bs4.BeautifulSoup(response2, features='html.parser')
            full_text = soup2.get_text(' ')
            check_and_print(title, full_text, article)
