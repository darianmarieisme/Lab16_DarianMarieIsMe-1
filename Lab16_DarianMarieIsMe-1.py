'''Lab 16 Option 1
Darian Marie Bruce
This program reads a CSV file and creates a line plot
05/10/2026'''

import matplotlib.pyplot as plt
from pathlib import Path
import csv
import datetime

dates: list = []

unemployment_rates: list = []

path: Path = Path('OHUR.csv')

lines = path.read_text(encoding = 'utf-8').splitlines()

reader = csv.reader(lines)

header_row = next(reader)

print(header_row)

for index, col_title in enumerate(header_row):
    print(f'{index} {col_title}', end=' ')

print()