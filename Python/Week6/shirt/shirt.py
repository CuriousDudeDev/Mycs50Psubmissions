from sys import exit , argv
from PIL import Image , ImageOps

if len(argv) < 2:
    exit('Too few command-line arguments')
if len(argv) > 3:
    exit('Too many command-line arguments')
if  not argv[2].lower().endswith(('.jpg' , '.jpeg' , '.png')):
    exit('Invalid Output')
extension1 = argv[1].split('.')[1]
extension2 = argv[2].split('.')[1]
if extension1 != extension2:
    exit('Input and output have different extensions')

try:
    image = Image.open(argv[1])
except FileNotFoundError:
    exit('Image does not exist')
with Image.open(argv[1]) as image:
    shirt = Image.open('shirt.png')
    image = ImageOps.fit(
        image=image,
        size = shirt.size,
        method=Image.Resampling.BICUBIC,
        bleed=0.0,
        centering=(0.5, 0.5),
    )
    image.paste(shirt , (0,0) , shirt)
    image.save(argv[2])

