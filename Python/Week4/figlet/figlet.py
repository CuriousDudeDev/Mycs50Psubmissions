from sys import argv , exit
from pyfiglet import figlet_format, FigletFont
from random import choice

if len(argv) == 1:
    fonts = FigletFont.getFonts()
    font = choice(fonts)
elif len(argv) > 1:
    if argv[1] in ['-f' , '--font']:
        if argv[2] not in FigletFont.getFonts():
            exit('Invalid Font')
        try:
            font = argv[2]
        except IndexError:
            exit('Invalid number of arguments')

    else:
        exit(f'Invalid argument - {argv[1]}')
original = input('Input: ')
output = figlet_format(original , font)
print(output)



