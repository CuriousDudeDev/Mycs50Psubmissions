import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"(\d{1,2}):?(\d{2})?AM to (\d{1,2}):?(\d{2})?PM",s)


...


if __name__ == "__main__":
    main()
