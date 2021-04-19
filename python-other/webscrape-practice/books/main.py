import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

# contains full html
source = requests.get('http://books.toscrape.com/').text

sc = BeautifulSoup(source, 'lxml')


with open('book_stats.csv', 'w') as file_name:
    csv_writer = csv.writer(file_name)
    # writing the headers for the columns
    csv_writer.writerow(['Book', 'Rating (1-5)','Price'])
    
    for article in sc.find_all('article'):
        
        # gets the title of the book
        title = article.find('h3').a.text

        # gets the price of the book
        price = article.find('p', class_='price_color').text
        
        # gets the rating of the book
        star = article.find('p', class_='star-rating')
        star = str(star)
        star = star.split( 'rating')[1].split('"')[0]
        
        # writes a new row containing the title, rating, and price of a book
        csv_writer.writerow([title, star ,price])

df = pd.read_csv('book_stats.csv')
print(df)
