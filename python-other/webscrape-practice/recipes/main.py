from bs4 import BeautifulSoup
import pandas as pd
import csv
import requests

# gets the html
source = requests.get('https://www.allrecipes.com/recipes/').text

sc = BeautifulSoup(source, 'lxml')

# opens file to save data in
with open('recipe_info.csv', 'w') as my_file:

    csv_writer = csv.writer(my_file)
    
    # writes the headers for the columns in the file
    csv_writer.writerow(['Headline', 'Summary', 'Author', 'Rating', 'Rating Count'])
    
    for content in sc.find_all('div', class_='component card card__category'):

        # finds the title of the recipe
        title = content.find('h3', class_='card__title').text.strip()

        # finds the summary of the recipe if available
        try:
            summary = content.find('div', class_='card__summary').text.strip()
        except AttributeError:
            summary = 'Not available'
        
        # to replace a en-dash with a regular dash
        if len(summary) >= 50 and summary[50] == u"\u2014":
            summary = list(summary)
            summary[50] = '-'
            summary = ''.join(summary)
        
        # finds the author if available
        try:
            author = content.find('span', class_='card__authorName').text.strip()
        except AttributeError:
            author = 'Not Available'
        
        # finds the rating if available
        try:
            rating = len(content.find_all('span', class_='rating-star active'))
            if (rating == 0): rating = 'Not Available'
                
        except AttributeError:
            rating = 'Not Available'
        
        # finds the amount of ratings if available
        try:
            rating_count = content.find('span', class_='card__ratingCount card__metaDetailText').text.strip()
            
        except AttributeError:
            rating_count = 'Not Available'
        
        # writing the data into the csv file
        csv_writer.writerow([title, summary, author, rating, rating_count])
        
df = pd.read_csv('recipe_info.csv')
df.head()
