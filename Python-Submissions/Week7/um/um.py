import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.strip().lower()
    match = re.findall(r'\bum\b' ,  s)
    if match:
        return len(match)
    else:
        return 0


...


if __name__ == "__main__":
    main()
