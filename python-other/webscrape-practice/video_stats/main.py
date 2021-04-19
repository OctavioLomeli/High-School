import pandas as pd
from selenium import webdriver
import csv

url = 'https://www.youtube.com/'

driver = webdriver.Chrome()

# passing in the url of the website to scrape
driver.get(url)

# opening new file
with open('video_stats.csv', 'w') as myFile:
    
    csv_writer = csv.writer(myFile)
    
    csv_writer.writerow(['Title', 'Channel', 'Views', 'Upload date'])
    
    # finding the names of youtubes videos
    titles = driver.find_elements_by_id('video-title')
    
    # removing all titles that are only blank spaces
    titles = [value.text for value in titles if value.text != '']
    
    # finding the html that contains the channel name, views, and upload date
    chan_views = driver.find_elements_by_class_name('style-scope ytd-video-meta-block')
    
    # removing empty elements
    chan_views = [chan_view.text for chan_view in chan_views if chan_view.text != ""]
    
    # organizing the list
    chan_views = [info.split('\n') for info in chan_views]
    
    indexes_to_remove = []
    
    # some videos are live streams which do not contain views so I am finding them
    for index in range(len(chan_views)):
        if chan_views[index][1].find('watching') != -1:
            indexes_to_remove.append(index)

    # removing the elements that are live streams
    for element in indexes_to_remove:
        chan_views.pop(element)
        titles.pop(element)

    # removing emojis or non-english characters from the video title by converting to byte then back to string
    for index in range(len(titles)):
        titles[index] = titles[index].encode(encoding='ascii', errors='ignore')
        chan_views[index][0] = chan_views[index][0].encode(encoding='ascii', errors='ignore')
     
    for index in range(len(titles)):
        titles[index] = titles[index].decode(encoding='UTF-8',errors='ignore')
        chan_views[index][0] = chan_views[index][0].decode(encoding='UTF-8', errors='ignore')
    
    # adding data into the csv file
    for index in range(len(titles)):
        csv_writer.writerow([titles[index], chan_views[index][0], chan_views[index][1], chan_views[index][2] ] )
    
driver.quit()

# putting data in dataframe to see better
df = pd.read_csv('video_stats.csv')
df
