import requests
import lxml
from bs4 import BeautifulSoup
import csv
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk

plt.rcParams.update({'font.size': 6})
countries = {
    "United Kingdom":
    "https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US%3Aen&mid=%2Fm%2F07ssc",
    "United States":
    "https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F09c7w0&gl=US&ceid=US%3Aen",
    "Argentina":
    "https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US%3Aen&mid=%2Fm%2F0jgd",
    "Colombia":
    "https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US%3Aen&mid=%2Fm%2F01ls2",
    "Mexico":
    "https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US%3Aen&mid=%2Fm%2F0b90_r",
    "Brazil":
    'https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US%3Aen&mid=%2Fm%2F015fr',
    "Spain":
    "https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US%3Aen&mid=%2Fm%2F06mkj",
    'Italy':
    "https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US%3Aen&mid=%2Fm%2F03rjj",
    "India":
    "https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US%3Aen&mid=%2Fm%2F03rk0"
}

# getting data for all countries in the countries dictionary
for key, value in countries.items():
    # creating csv file to store data for each country
    with open("covid-stats-{}.csv".format(key.replace(" ", "-")), "w") as myFile:
        csv_writer = csv.writer(myFile)
        csv_writer.writerow(["Location", "Cases", "Deaths"])

        source = requests.get(value).text
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

        # removing accents
        for index in range(len(cases)):
            try:
                for char in states[index]:
                    if char in "áã":
                        states[index] = states[index].replace(char, "a")
                    elif char == "é":
                        states[index] = states[index].replace("é", "e")
                    elif char == "í":
                        states[index] = states[index].replace("í", "i")
                    elif char in "óô":
                        states[index] = states[index].replace(char, "o")
                # skipping location if there is no data for the amount of cases
                if cases[index] == "No data":
                    continue
                # converting string numbers into integers
                else:
                    cases[index] = int(cases[index].replace(",", "", 2))
                # for the locations with no data on death, it will be turned into a -1
                if deaths[index] == "No data":
                    deaths[index] = -1
                # convert string number to integer
                else:
                    deaths[index] = int(deaths[index].replace(",", "", 2))
                if len(states[index]) > 10:
                  states[index] = states[index][:11]

                csv_writer.writerow([states[index], cases[index], deaths[index]])
            # just in case
            except Exception as e:
                print(e)
                continue

# putting data in dataframe
for key in countries.keys():
    countries[key] = pd.read_csv("covid-stats-{}.csv".format(key.replace(" ", "-")))

root = tk.Tk()
root.geometry("800x450")
root.resizable(False, False)
root.title("COVID-19 Statistics")
root['bg'] = "#e9c46a"

# frames
topFrame = tk.Frame(root, bg="#e9c46a")
topFrame.pack(side=tk.TOP)

bottomFrame = tk.Frame(root, bg="#e9c46a")
bottomFrame.pack(side=tk.BOTTOM, pady=10)

rightFrame = tk.Frame(root, bg="#e9c46a")
rightFrame.pack(side=tk.RIGHT)

leftFrame = tk.Frame(root, bg="#e9c46a")
leftFrame.pack(side=tk.LEFT)

# content in top frame
tk.Label(
    topFrame,
    text="COVID-19 Statistics",
    bg="#e9c46a",
    fg="black",
    font=("Arial", 30)).pack()

# content in bottom frame
country_label = tk.Label(
    bottomFrame,
    bg="#e9c46a",
    fg="black",
    text="Set Country: ",
    font=("Arial", 18)).pack(side=tk.LEFT)
country_entry = tk.Entry(
    bottomFrame, bg="white", fg="black", font=("Arial", 20))
country_entry.pack(
        side=tk.LEFT, padx=20)

# content in right frame
button_graph_case_pt1 = tk.Button(
    rightFrame,
    text="Cases pt.1",
    bg="#4d5061",
    fg="white",
    font=("Arial", 13),
    width=8)
button_graph_case_pt1.grid(pady=5, padx=5)
button_graph_case_pt2 = tk.Button(
    rightFrame,
    text="Cases pt.2",
    bg="#4d5061",
    fg="white",
    font=("Arial", 13),
    width=8)
button_graph_case_pt2.grid(pady=5, padx=5)

button_graph_death_pt1 = tk.Button(
    rightFrame,
    text="Deaths pt.1",
    bg="#4d5061",
    fg="white",
    font=("Arial", 13),
    width=8)
button_graph_death_pt1.grid(pady=5, padx=5)
button_graph_death_pt2 = tk.Button(
    rightFrame,
    text="Deaths pt.2",
    bg="#4d5061",
    fg="white",
    font=("Arial", 13),
    width=8)
button_graph_death_pt2.grid(pady=5, padx=5)

# content in left frame
tk.Label( leftFrame, text="Available Countries:", bg="#e9c46a", fg="black", font=("Arial", 14)).pack()
for key in countries.keys():
  tk.Label( leftFrame, text=key, bg="#e9c46a", fg="black", font=("Arial", 12)).pack()

# functions
canvas = 0
  # delete graph
def remove_plot():
    global canvas
    try:
      canvas.get_tk_widget().destroy()
    except Exception as e:
      print(e)


# creates graph for cases
def graph_cases_pt1():
  global canvas
  try:
    canvas.get_tk_widget().destroy()
  except Exception as e:
    print(e)
  country = country_entry.get()

  if country not in countries.keys():
    country_entry.delete(0, "end")
    country_entry.insert(0, "Invalid Country")
    return

  def plot(x, y):
    fig = Figure(figsize=(12, 8))
    ax1 = fig.add_subplot(1,1,1)
    ax1.barh(x, y)
    return fig

  half_len = len(countries[country])/2
  if half_len.is_integer():
    half_len = int(half_len)
  else:
    half_len = int(half_len + .5)
  fig = plot(countries[country]["Location"].iloc[:half_len], countries[country]["Cases"].iloc[:half_len])
  canvas = FigureCanvasTkAgg(fig, master=root)
  canvas.get_tk_widget().pack()


# creates graph for case pt2
def graph_cases_pt2():
  global canvas
  try:
    canvas.get_tk_widget().destroy()
  except Exception as e:
    print(e)
  country = country_entry.get()

  if country not in countries.keys():
    country_entry.delete(0, "end")
    country_entry.insert(0, "Invalid Country")
    return

  def plot(x, y):
    fig = Figure(figsize=(12, 8))
    ax1 = fig.add_subplot(1,1,1)
    ax1.barh(x, y)
    return fig

  half_len = len(countries[country])/2
  if half_len.is_integer():
    half_len = int(half_len)
  else:
    half_len = int(half_len + .5)
  fig = plot(countries[country]["Location"].iloc[half_len:], countries[country]["Cases"].iloc[half_len:])
  canvas = FigureCanvasTkAgg(fig, master=root)
  canvas.get_tk_widget().pack()


# creates graph for death
def graph_deaths_pt1():
  global canvas
  try: 
    canvas.get_tk_widget().destroy()
  except Exception as e:
    print(e)
  country = country_entry.get()

  if country not in countries.keys():
    country_entry.delete(0, "end")
    country_entry.insert(0, "Invalid Country")
    return

  def plot(x, y):
    fig = Figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.barh(x, y)
    return fig

  half_len = len(countries[country])/2
  if half_len.is_integer():
    half_len = int(half_len)
  else:
    half_len = int(half_len + .5)
  plt.figure(figsize=(8, 6))
  fig = plot(countries[country]["Location"].iloc[:half_len], countries[country]["Deaths"].iloc[:half_len])
  canvas = FigureCanvasTkAgg(fig, master=root)
  canvas.get_tk_widget().pack()


# creates graph for death
def graph_deaths_pt2():
  global canvas
  try:
    canvas.get_tk_widget().destroy()
  except Exception as e:
    print(e)
  country = country_entry.get()

  if country not in countries.keys():
    country_entry.delete(0, "end")
    country_entry.insert(0, "Invalid Country")
    return

  def plot(x, y):
    fig = Figure(figsize=(12, 8))
    ax1 = fig.add_subplot(1,1,1)
    ax1.barh(x, y)
    return fig

  half_len = len(countries[country])/2
  if half_len.is_integer():
    half_len = int(half_len)
  else:
    half_len = int(half_len + .5)
  fig = plot(countries[country]["Location"].iloc[half_len:], countries[country]["Deaths"].iloc[half_len:])
  canvas = FigureCanvasTkAgg(fig, master=root)
  canvas.get_tk_widget().pack()


# configuring commands
button_graph_case_pt1.configure(command=graph_cases_pt1)
button_graph_case_pt2.configure(command=graph_cases_pt2)
button_graph_death_pt1.configure(command=graph_deaths_pt1)
button_graph_death_pt2.configure(command=graph_deaths_pt2)

root.mainloop()
