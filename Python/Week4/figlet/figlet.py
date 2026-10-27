from sys import argv , exit
from pyfiglet import figlet_format

if len(argv) == 1:
    

original = input('Input: ')
print(figlet_format(original , font=font_name))

