from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


source = requests.get('https://www.worldometers.info/coronavirus/').text

sc = BeautifulSoup(source, 'lxml')

list_headers = sc.findAll(id='maincounter-wrap')

# Headers for stats
header1 = list_headers[0]
header2 = list_headers[1]
header3 = list_headers[2]


# list of stat to header
list_nums = sc.findAll(class_='maincounter-number')

stat1 = list_nums[0]
stat2 = list_nums[1]
stat3 = list_nums[2]

headers = []
for head in list_headers:
    head = str(head)
    head = head.split('>')
    head = head[2]
    head = head.split(':')
    head = head[0]
    headers.append(head)
del list_headers

stats = []
for stat in list_nums:
    stat = str(stat)
    stat = stat.split('>')
    stat = stat[2]
    stat = stat.split('<')
    stat = stat[0]
    stats.append(stat.strip() )

del list_nums

print(stats)
print(headers)
csv_file = open('covid_stats.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow([headers[0], headers[1], headers[2]])
csv_writer.writerow([stats[0], stats[1], stats[2]])
csv_file.close()
df = pd.read_csv('covid_stats.csv')
df.head()
