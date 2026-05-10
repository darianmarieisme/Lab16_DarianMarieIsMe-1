'''Lab 16 Option 1
Darian Marie Bruce
This program reads a CSV file and creates a line plot
05/10/2026'''

import matplotlib.pyplot as plt
from pathlib import Path
import csv
import datetime

graph_path: Path = Path('OHUR.csv')
output_path: Path = Path("ohio_unemployment.png")

def read_unemployment_data(file_path: Path) -> tuple[list[datetime.datetime], list[float]]:
    '''
    This method reads the CSV file and outputs the data as a tuple
    parameters:
    file_path: the path where the OHUR CSV is stored
    Output:
    A tuple that includes a list of all dates, then a list of all ue rates
    '''

    dates: list[datetime.datetime] = []
    unemployment_rates: list[float] = []

    lines = graph_path.read_text(encoding = 'utf-8').splitlines()
    reader = csv.reader(lines)

    header_row = next(reader)
    print(header_row)

    for row in reader:
        try: 
            date = datetime.datetime.strptime(row[0], "%Y-%m-%d")
            ohur: float = float(row[1])
        except ValueError:
            print(f"Could not convert data in row: {row}")

        else:
            dates.append(date)
            unemployment_rates.append(ohur)

    return dates, unemployment_rates

def create_graph(dates: list[datetime.datetime],
                 unemployment_rates: list[float],
                 output_path: Path) -> None:
    '''
    This method creates and outputs a graph using dates and unemployment
    rates from the CSV file
    parameters:
    dates: read from the CSV file
    unemployment_rates: read from the CSV file
    output_path: the path of the output file
    '''
    plt.style.use('dark_background')

    figure, graph = plt.subplots()

    plt.title("Ohio Unemployment (by Month): 1976 - 2022")
    plt.xlabel("Date")
    plt.ylabel("Unemployment Rate")

    graph.plot(dates, unemployment_rates, color = 'blue')
    
    figure.savefig(output_path)
    plt.show() 

def main() -> None:
    '''Runs the unemployment graph program'''
    dates, unemployment_rates = read_unemployment_data(graph_path)
    create_graph(dates, unemployment_rates, output_path)

if __name__ == "__main__":
    main()