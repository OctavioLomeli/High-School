from selenium import webdriver
import pandas as pd
import csv

driver = webdriver.Chrome()
# passing in url of website
driver.get("https://www.google.com/search?rlz=1C1CHBF_enUS923US923&biw=1536&bih=722&tbm=nws&sxsrf=ALeKk01wa-fYFiwtmqWkjxN5M7vkrmlwCA%3A1606289296044&ei=kAe-X7aXApH-9APrtJC4DQ&q=covid+19+vaccine&oq=covid+19+&gs_l=psy-ab.3.0.0i433k1j0l5j0i433k1l3j0.12538.14122.0.15690.11.7.1.3.3.0.138.675.6j1.7.0....0...1c.1.64.psy-ab..0.11.717...0i3k1j0i433i131k1.0.ReZBO1twbg0")

news_channel = []

for element in driver.find_elements_by_class_name("XTjFC"):
    element = element.text.encode("cp1252")
    element = element.decode("utf-8", errors="ignore")
    news_channel.append(element)

titles = []
for element in driver.find_elements_by_class_name("JheGif"):
    element = element.text.encode("cp1252")
    element = element.decode("utf-8", errors="ignore")
    titles.append(element)

descriptions = []
for element in driver.find_elements_by_class_name("Y3v8qd"):
    element = element.text.encode("cp1252")
    element = element.decode("utf-8", errors="ignore")
    descriptions.append(element)
    
time_released = []
for element in driver.find_elements_by_class_name("WG9SHc"):
    element = element.text.encode("cp1252")
    element = element.decode("utf-8", errors="ignore")
    time_released.append(element)
    
driver.quit()

with open("covid-19-vaccine-news.csv", "w") as myFile:
    
    csv_writer = csv.writer(myFile)
    csv_writer.writerow(["Source", "Title", "Description", "Time Released"])
    
    for index in range(len(news_channel)):
        csv_writer.writerow([news_channel[index], titles[index], descriptions[index], time_released[index]])

df = pd.read_csv("covid-19-vaccine-news.csv")
df.head()
