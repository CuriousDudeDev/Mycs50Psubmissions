from random import randrange as r


def main():
    level = get_level()

    score = 0
    num = 0
    while num < 10 :

        int1 = generate_integer(level)
        int2 = generate_integer(level)
        answer = int1 + int2
        attempts = 0
        while True:
            if attempts == 3:
                print(f'{int1} + {int2} = {answer}')
                num += 1
                break
            try:
                answer_given = int(input(f'{int1} + {int2} = '))
            except ValueError:
                attempts += 1
                print('EEE')
                continue
            else:
                if answer_given == answer:
                    score += 1
                    num += 1
                    break
                else:
                    attempts += 1
                    print('EEE')
    print(f'Score: {score}')


def get_level():
    while True:
        try:
            level = int(input('Level: '))
        except ValueError:
            continue
        else:
            if level > 3 or level <= 0:
                continue
            else:
                return level



def generate_integer(level):

    if level > 1:
        num = r(10**(level-1) , 10**(level))

    else:
        num = r(0 , 10**(level))
    return num




if __name__ == "__main__":
    main()
