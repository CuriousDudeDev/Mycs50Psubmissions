import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    before_and_after_iframe = s.split('</iframe>')
    before = before_and_after_iframe[0]
    if 'youtube.com' not in before:
        return None







if __name__ == "__main__":
    main()
