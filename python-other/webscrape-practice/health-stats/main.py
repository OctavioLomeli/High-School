from selenium import webdriver
import csv
import pandas as pd

# url of website
url = 'https://www.worldometers.info/'

driver = webdriver.Chrome()

driver.get(url)

# opening new file to write in
with open('health_stats.csv', 'w') as myFile:
    
    csv_writer = csv.writer(myFile)
    
    csv_writer.writerow(['Header', 'Stat'])
    
    # looping through tags with and ID of 'c' + a number between 49 - 62
    for section_num in range(49 , 63):
        
        section = driver.find_element_by_id('c' + str(section_num))
        
        stat = section.find_element_by_class_name('counter-number').text
        
        head = section.find_element_by_class_name('counter-item').text
        
        csv_writer.writerow([head, stat])
    
driver.quit()

df = pd.read_csv('health_stats.csv')

df.head()
