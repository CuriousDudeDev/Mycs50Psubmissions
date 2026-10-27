import random


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
    ...


if __name__ == "__main__":
    main()
