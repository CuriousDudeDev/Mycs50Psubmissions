import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s = s.strip()
    pattern = re.search(r"\d{}",s)


...


if __name__ == "__main__":
    main()
