import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s = s.strip()
    pattern = re.search(r"(\d{1,2})(:| )?(\d{2})?( )(AM|PM) to (\d{1,2})(:| )?(\d{2})?( )(PM|AM)",s)
    if pattern:
        hours_1 = int(pattern.group(1))
        hours_2 = int(pattern.group(6))
        minutes_1 = (pattern.group(3))
        minutes_2 = (pattern.group(8))
        if minutes_1 == None:
            minutes_1 = 0
        else:
            minutes_1 = int(minutes_1)
        if minutes_2 == None :
            minutes_2 = 0
        else:
            minutes_2 = int(minutes_2)
        time_1 = pattern.group(5)
        time_2 = pattern.group(10)
        if hours_1 <12 and time_1 == 'AM':
            hours_1 = hours_1
        elif hours_1 > 12 and time_1 == 'AM':
            raise ValueError
        elif hours_1 <12 and time_1 == 'PM':
            hours_1 = (hours_1) + 12
        elif hours_1 >12 and time_1 == 'PM':
            raise ValueError
        elif hours_1 == 12 and time_1 == 'AM':
            hours_1 = 0
        elif hours_1 == 12 and time_1 == 'PM':
            hours_1 = 12
        #end of hour_1
        if hours_2 <12 and time_2 == 'AM':
            hours_2 = (hours_2)
        elif hours_2 > 12 and time_2 == 'AM':
            raise ValueError
        elif hours_2 <12 and time_2 == 'PM':
            hours_2 = (hours_2) + 12
        elif hours_2 >12 and time_2 == 'PM':
            raise ValueError
        elif hours_2 == 12 and time_2 == 'PM':
            hours_2 = 12
        elif hours_2 == 12 and time_2 == 'AM':
            hours_2 = 0
        # 3end of hour_2
        if minutes_1 >= 60 or minutes_2 >= 60 or minutes_1 < 0 or minutes_2 < 0:
            raise ValueError('Invalid Input')


        #end of minutes
        return (f"{hours_1:02}:{minutes_1:02} to {hours_2:02}:{minutes_2:02}")
    else:
        raise ValueError('Invalid Input')


...


if __name__ == "__main__":
    main()
