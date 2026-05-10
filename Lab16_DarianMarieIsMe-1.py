'''Lab 16 Option 1
Darian Marie Bruce
This program reads a CSV file and creates a line plot
05/10/2026'''

import matplotlib.pyplot as plt
from pathlib import Path
import csv
import datetime

path: Path = Path('OHUR.csv')

lines = path.read_text(encoding = 'utf-8').splitlines()

reader = csv.reader(lines)

header_row = next(reader)

print(header_row)

# for index, col_title in enumerate(header_row):
    # print(f'{index} {col_title}', end=' ')

# print()

#processing info from file
dates: list = []

unemployment_rates: list = []

for row in reader:
    try: 
        date = datetime.datetime.strptime(row[0], "%Y-%m-%d")
        ohur: float = float(row[1])
    except ValueError:
        print(f"Could not convert data in row: {row}")

    else:
        dates.append(date)
        unemployment_rates.append(ohur)

#graph

plt.style.use('dark_background')
figure, graph = plt.subplots()
plt.title("Ohio Unemployment (by Mont): 1976 - 2022")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate")

graph.plot(dates, unemployment_rates, color = 'blue')
plt.show() 
