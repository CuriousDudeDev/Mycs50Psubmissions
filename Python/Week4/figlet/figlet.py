from sys import argv , sys
from pyfiglet import figlet_format

if not (len(argv) == 1 or len(argv) == 3):
    sys.exit('Invalid number of arguments')
if argv[1] in ['-f' , '--font']:
    font_name = argv[1]
else:
    sys.exit(f'Invalid argument {argv[1]}')

original = input('Input: ')
print(figlet_format(original , font=font_name))

