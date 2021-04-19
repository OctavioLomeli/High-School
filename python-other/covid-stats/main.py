import tkinter as tk
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# website to scrape
source = requests.get('https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F09c7w0&gl=US&ceid=US%3Aen').text
soup = BeautifulSoup(source, 'lxml')

sections = soup.find_all('tr', class_='sgXwHf wdLSAe YvL7re')

states = []
cases = []
deaths = []

for data in sections:
    states.append(data.find('div', class_='TWa0lb').text)

    state_stats = data.find_all('td', class_='l3HOY')
    for index in range(len(state_stats)):
        state_stats[index] = state_stats[index].text

    cases.append(state_stats[0])
    deaths.append(state_stats[-1])

# not needed anymore
del state_stats

for index in range(len(cases)):
    cases[index] = int(cases[index].replace(",", '', 3))
    deaths[index] = int(deaths[index].replace(",", '', 3))

states.reverse()
cases.reverse()
deaths.reverse()

# displays half of all state's case numbers (not all states since too large)
def graph_case_pt1():
    plt.barh(states[:21], cases[:21])
    plt.title('COVID-19 Cases By State')
    plt.ylabel('State')
    plt.xlabel('# of Cases In Millions')
    plt.tight_layout()
    plt.grid(True)
    plt.show()

# other half
def graph_case_pt2():
    plt.barh(states[21:], cases[21:])
    plt.title('COVID-19 Cases By State')
    plt.ylabel('State')
    plt.xlabel('# of Cases In Millions')
    plt.tight_layout()
    plt.grid(True)
    plt.show()

# displays half of all state's death numbers (not all states since too large)
def graph_death_pt1():
    plt.barh(states[:21], deaths[:21])
    plt.title('COVID-19 Deaths By State')
    plt.ylabel('State')
    plt.xlabel('# of Cases')
    plt.tight_layout()
    plt.grid(True)
    plt.show()

# other half
def graph_death_pt2():
    plt.barh(states[21:], deaths[21:])
    plt.title('COVID-19 Deaths By State')
    plt.ylabel('State')
    plt.xlabel('# of Cases')
    plt.tight_layout()
    plt.grid(True)
    plt.show()


root = tk.Tk()
root.title('COVID-19 State Stats')
root.geometry('370x370')
root['bg'] = '#3d405b'

# widgets
title = tk.Label(root, text='COVID-19 Stats', fg='white', pady=10, padx=60, font=('System', 25), bg='#3d405b')
title.grid(row=0, column=3)

case_button1 = tk.Button(root, text="Cases pt.1", fg='Black', bg='#e56b6f', font=('Verdana', 18), padx=9, command=graph_case_pt1)
case_button1.grid(row=1, column=3)

buffer1 = tk.Label(root, pady=5, bg='#3d405b').grid(row=2)

case_button2 = tk.Button(root, text="Cases pt.2", fg='Black', bg='#e56b6f', font=('Verdana', 18), padx=9, command=graph_case_pt2)
case_button2.grid(row=3, column=3)

buffer2 = tk.Label(root, pady=5, bg='#3d405b').grid(row=4)

death_button1 = tk.Button(root, text="Deaths pt.1", fg='Black', bg='#e56b6f', font=('Verdana', 18), command=graph_death_pt1)
death_button1.grid(row=5, column=3)

buffer3 = tk.Label(root, pady=5, bg='#3d405b').grid(row=6)
death_button2 = tk.Button(root, text="Deaths pt.2", fg='Black', bg='#e56b6f', font=('Verdana', 18), command=graph_death_pt2)

death_button2.grid(row=7, column=3)
# end of widgets

root.mainloop()
