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
        time_1 = pattern.group(5)
        time_2 = pattern.group(10)
        if time_1 == time_2:
            raise ValueError('Invalid Input')
        if time_1 == 'AM':
            am_hours == int(time_1)
            pm_hours == int(time_2)
        else:
            pm_hours = int(time_1)
            am_hours = int(time_1)
        if not minutes_1:
            minutes_1 = 0
        if not minutes_2:
            minutes_2 = 0
        if minutes-1 > 60 or minutes_2 > 60:
            raise ValueError('Invalid Input')

        else:
            raise ValueError('Invalid Input')


...


if __name__ == "__main__":
    main()
