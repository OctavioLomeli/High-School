from selenium import webdriver
import csv
import pandas as pd

url = 'https://www.worldometers.info/world-population/'

driver = webdriver.Chrome()

# passing in the url of the website to scrape
driver.get(url)

# opening new file 
with open('World_stats.csv', 'w') as myFile:

    csv_writer = csv.writer(myFile)
    csv_writer.writerow(['Header', 'Stat'])
    
    # finding the main data
    world_pop = driver.find_element_by_xpath('.//*[@id="maincounter-wrap"]/h1').text
    world_pop_stat = driver.find_element_by_class_name('rts-counter').text
    
    # writing the data in a file
    csv_writer.writerow([world_pop, world_pop_stat])
    
    # looking for headers and numbers in a section that repeats
    for section in driver.find_elements_by_class_name('sec-box'):
        
        head = section.find_element_by_class_name('sec-text').text
        
        number = section.find_element_by_class_name('sec-counter').text
        
        # writing header and its number in the file
        csv_writer.writerow([head, number])    
        
driver.quit()

# inputting data into a pandas dataFrame to visualise better
df = pd.read_csv('World_stats.csv')
df.head()
