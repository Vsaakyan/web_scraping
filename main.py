import requests
import bs4

KEYWORDS = {'Изучение языков', 'хранение данных', 'web', 'python'}

response = requests.get('https://habr.com/ru/all/')
resp_text = response.text

soup = bs4.BeautifulSoup(resp_text, features='html.parser')
articles = soup.find_all(class_='tm-article-snippet')

# def find_articles_info(articles_: articles):
for article in articles:
    articles_text = articles.find('h2').find('a').find('tm-article-snippet__hubs')
    articless_set = set(articles_text.text.split())
    print(articles_text)
    if KEYWORDS & articless_set:
        title = article.find('h2').find('a').text
        print(title)
        date = article.find("time").text
        print(date)
        href = articles_text.attrs['href']
        url = 'https://habr.com/ru/all/' + href
        #print(f' || Date of this article is --> {date} || \n || title is --> {title} || \n || URL is --> {url} ||')


#if __name__ == '__main__':
    #print(find_articles_info(articles))