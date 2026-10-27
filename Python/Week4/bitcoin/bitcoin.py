import requests as r
from sys import argv,exit
if len(argv) <2:
    exit('Missing command line argument')
elif len(argv) > 2:
    exit('Too many arguments')
else:
    try:
        num = float(argv[1])
    except ValueError:
        exit('Invalid Argument')
    else:

