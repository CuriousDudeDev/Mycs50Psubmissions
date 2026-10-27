import requests
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
        try:
            response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=442416a3583537eedb59226e3addccb1314e8c20df178b16088c884be02a4bdc")
        except requests.RequestException:
            exit('Error! Here!, Wait a minute or try again .')
        else:
            dump = response.json()
            price = dump['priceUsd']
            print(f"${price*num:,.4f} ")

