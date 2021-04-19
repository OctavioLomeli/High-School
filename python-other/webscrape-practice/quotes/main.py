from bs4 import BeautifulSoup
import pandas as pd
import csv
import requests

# contains all html
source = requests.get('http://quotes.toscrape.com/').text

sc = BeautifulSoup(source, 'lxml')

# opens new file
with open('quotes_info.csv', 'w') as file_name:

    csv_writer = csv.writer(file_name)
    
    # writes the headers for columns
    csv_writer.writerow(['Quote', 'Author', 'Tags'])
    
    for div in sc.find_all('div', class_='quote'):
        
        # finds the quote within the div
        quote = div.find('span', class_='text').text[1:-1]
        
        # finds the author within the div
        author = div.find('small', class_='author').text
        
        # fixes error resulting from special letter in the 'e' of Andre
        if author[:4] == 'Andr':
            author = 'Andre Gide'
        
        tag = ""
        
        # adds all tags into one
        for a in div.find_all('a', class_='tag'):
            tag = tag + a.text + ', '
        
        # writes a new column with the data gathered
        csv_writer.writerow([quote, author, tag])

# creates a dataFrame to see the data more clearly
df = pd.read_csv('quotes_info.csv')
df.head()
