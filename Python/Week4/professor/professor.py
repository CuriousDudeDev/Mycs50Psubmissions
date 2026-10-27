from random import randint as r


def main():
    get_level()


def get_level():
    while True:
        try:
            level = int(input('Level: '))
        except ValueError:
            continue
        else:
            if level > 3 or level < 0:
                continue
            else:
                return level



def generate_integer(level):
    num = 0
    while num <= 10:
        int1 = r(10*level , 10*(level+1))
        int2 = r(10*level , 10*(level+1))
        answer = int1 + int2
        


if __name__ == "__main__":
    main()
