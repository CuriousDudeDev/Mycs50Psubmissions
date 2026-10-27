from random import randrange as r


def main():
    level = get_level()

    score = 0
    num = 0
    while num < 10 :
        ints = generate_integer(level)
        int1 = ints[0]
        int2 = ints[1]
        answer = int1 + int2
        attempts = 0
        while True:
            if attempts == 3:
                print(f'{int1} + {int2} = {answer}')
                print('EEE')
                num += 1
                break
            try:
                answer_given = int(input(f'{int1} + {int2} = '))
            except ValueError:
                attempts += 1
                continue
            else:
                if answer_given == answer:
                    score += 1
                    num += 1
                    break
                else:
                    attempts += 1
    return f'Score: {score}'


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
    ints=[]
    if level > 1:
        ints[0] = r(10**(level-1) , 10**(level))
        ints[1] = r(10**(level-1) , 10**(level))
    else:
        ints[0] = r(0 , 10**(level))
        ints[1] = r(0 , 10**(level))
    return ints



if __name__ == "__main__":
    main()
