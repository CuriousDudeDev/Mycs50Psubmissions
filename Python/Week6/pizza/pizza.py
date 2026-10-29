from tabulate import tabulate
import csv
from sys import exit , argv

if len(argv) < 2:
    exit('Too few command-line arguments')
if len(argv) > 2:
    exit('Too many command-line arguments')
if not argv[1].endswith('.csv'):
    exit('Not a CSV file')
try:
    file = open(argv[1] , 'r')
except FileNotFoundError:
    exit('File does not exist')
else:
    table = []
    with open(argv[1]) as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        table = list(reader)
        key = 1
        new_headers = {}
        for i in headers:
            new_headers[key] = i
            key += 1

        print(tabulate(table , new_headers , "colon_grid", colalign=["right", "left"]))
