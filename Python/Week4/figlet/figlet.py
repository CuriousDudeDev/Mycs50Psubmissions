from sys import argv , exit
from pyfiglet import figlet_format, FigletFont
from random import choice

if len(argv) == 1:
    fonts = FigletFont.getfonts()
    font = choice(fonts)
elif len(argv) > 1:
    if argv[1] 

