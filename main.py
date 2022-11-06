import requests
import bs4


keywordz = {'дизайн', 'фото', 'web', 'python', 'ПК', 'ваш', 'Path'}


response = requests.get('https://habr.com/ru/all/')
text = response.text

soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.find_all(class_="tm-article-snippet")


for article in articles:
    article_text = article.find('h2').find('a')
    hub_set = set(article_text.text.split())
    if keywordz & hub_set:
        date = article.find('time').text
        title = article.find('h2').find('a').text
        print(title)
        href = article_text.attrs['href']
        url = 'https://habr.com' + href
        print(f'Дата: {date} - Заголовок: {title}   Ссылка: {url}')

