import re
import sys
import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"(\d{1,2})(:| )?(\d{2})?AM (to|TO) (\d{1,2})(:| )?(\d{2})? PM",s)
    if not matches:
        raise ValueError('Invalid Input- Try Again')
    if matches:
        am_hours = matches.group(1)
        am_min = matches.group(3)
        pm_hours = matches.group(5)
        pm_min = matches.group(7)
        if not am_min:
            am_min = 0
        if not pm_min:
            pm_min = 0
        if int(am_min) > 60 or int(pm_min) > 60:
            raise ValueError('Invalid minutes')
        if int(am_hours) > 12 or int(pm_hours) > 12:
            raise ValueError('Invalid hours')
        if int(pm_hours) == 12:
            int(pm_hours) -= 12
        if int(am_hours) == 0:
            int(am_hours) -= 12



        return f"{int(am_hours):02d}:{am_min:02} to {int(pm_hours) + 12}:{pm_min:02}"


...


if __name__ == "__main__":
    main()
