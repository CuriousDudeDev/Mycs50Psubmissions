import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s = s.strip()
    pattern = re.search(r"(\d{1,2})(:| )?(\d{2})?(| )(AM|PM) to (\d{1,2})(:| )?(\d{2})?(| )(PM|AM)",s)
    if pattern:
        hours_1 = pattern.group(1)
        hours_2 = pattern.group(6)
        minutes_1 = pattern.group(3)
        minutes_2 = pattern.group(8)
        

        else:
        raise ValueError('Invalid Input')


...


if __name__ == "__main__":
    main()
