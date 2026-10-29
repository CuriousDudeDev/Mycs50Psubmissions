import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    before_and_after_iframe = s.split('</iframe>')
    before = before_and_after_iframe[0]
    after = before_and_after_iframe[1]
    






if __name__ == "__main__":
    main()
