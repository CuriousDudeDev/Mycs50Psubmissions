import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"(\d{1,2})(:| )?(\d{2})?AM (to|TO) (\d{1,2})(:| )?(\d{2})?PM",s)
    if matches:
        am_hours = matches.group(1)
        am_min = matches.group(3)
        pm_hours = matches.group(4)
        pm_min = matches.group(6)
        if not am_min:
            am_min = '00'
        if not pm_min:
            pm_min = 'oo'
        return f"{am_hours}:{am_min} to {int(pm_hours) + 12}:{pm_min}"


...


if __name__ == "__main__":
    main()
