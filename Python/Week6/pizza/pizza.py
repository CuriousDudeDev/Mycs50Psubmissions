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
        header = reader.fieldnames
        for row in reader:
            table.append({1:header[0] , 2:header[1] , 3:header[2]})
        headers = {1:header[0] , 2:header[1] , 3:header[2]}
        print(tabulate(table , headers , "colon_grid", colalign=["right", "left"]))
