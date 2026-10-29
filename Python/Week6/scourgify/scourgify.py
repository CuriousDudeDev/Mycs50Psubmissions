import csv
import sys

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
if not sys.argv[1].endswith('.csv'):
    sys.exit('Not a CSV file')
try:
    file = open(sys.argv[1] , 'r')
except FileNotFoundError:
    sys.exit('File does not exist')
else:
    with open(sys.argv[1] , 'r') as file:
        reader = csv.DictReader(file)
        table = list(reader)
    with open(sys.argv[2] , 'w') as new_file:
        writer = csv.DictWriter(new_file, fieldnames = ['first' , 'last' , 'house'])
        writer.writeheader()
        for row in table:
            name = row['name']
            first , last = name.split(',')
            first = first.strip()
            last = last.strip()
            house = row['house']

            writer.writerow({"first": last, "last": first, 'house' : house})


