import requests
from bs4 import BeautifulSoup
import pandas as pd

def collect_user_rates(user_login):
   page_num = 1

   data = []

   while True:
       url = f'https://www.livelib.ru/reader/{user_login}/reviews/~{page_num}/'
       html_content = requests.get(url).text

       soup = BeautifulSoup(html_content, 'lxml')

       entries = soup.find_all('div', class_='lenta-card')

       if len(entries) == 0:
           break

       for entry in entries:
           div_lenta_card_book = entry.find('div', class_='lenta-card-book')
           div_lenta_card_book_wr = div_lenta_card_book.find('div', class_='lenta-card-book__wrapper')
           p_book_author = div_lenta_card_book_wr.find('p', class_='lenta-card__author-wrap')
           author_name = p_book_author.find('a').text

           book_name = div_lenta_card_book_wr.find('a', class_='lenta-card__book-title').text

           h3_rating = entry.find('h3', class_='lenta-card__title')
           rating = h3_rating.find('span', class_='lenta-card__mymark').text

           data.append({'author_name': author_name, 'book_name': book_name, 'rating': rating})

       page_num += 1

   return data

user_rates = collect_user_rates(user_login)
df = pd.DataFrame(user_rates)

df.to_excel('user_rates.xlsx')