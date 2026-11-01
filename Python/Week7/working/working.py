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
        if hours_1 <=12 and time_1 == 'AM':
            hours_1 = int(hours_1)
        elif hours_1 >= 12 and time_1 == 'AM':
            raise ValueError
        elif hours_1 <=12 and time_1 == 'PM':
            hours_1 = int(hours_1) + 12
        elif hours_1 >=12 and time_1 == 'PM':
            raise ValueError
        #end of hour_1
        if hours_2 <=12 and time_2 == 'AM':
            hours_2 = int(hours_2)
        elif hours_2 >= 12 and time_2 == 'AM':
            raise ValueError
        elif hours_2 <=12 and time_2 == 'PM':
            hours_2 = int(hours_2) + 12
        elif hours_2 >=12 and time_2 == 'PM':
            raise ValueError

        if not minutes_1:
            minutes_1 = 0
        if not minutes_2:
            minutes_2 = 0
        if minutes_1 > 60 or minutes_2 > 60:
            raise ValueError('Invalid Input')


        else:
            raise ValueError('Invalid Input')


...


if __name__ == "__main__":
    main()
