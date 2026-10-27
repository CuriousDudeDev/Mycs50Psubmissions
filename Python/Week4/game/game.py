from random import randint as r

while True:
    try:
        level = int(input('Level: '))
    except ValueError:
        continue
    else:
        if level <= 0:
            continue
        break
number = r(1 , level)
while True:
    try:
        guess = int(input('Guess: '))
    except ValueError:
        continue
    else:
        if guess <= 0:
            continue
        elif guess == number:
            print('Just Right!')
            break
        elif guess > number:
            print('Too Large!')
        else:
            print('Too Small!')
