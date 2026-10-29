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
    
