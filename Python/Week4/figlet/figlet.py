from sys import argv , exit
from pyfiglet import figlet_format, FigletFont

if len(argv) == 1:
    fonts = FigletFont.getfonts()


original = input('Input: ')
print(figlet_format(original , font=font_name))

