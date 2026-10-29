import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)\.(\d+)" , ip)

    if not matches:
        return False
    if matches:
        if not len(matches.group()) > 4 :
            return False
        for num in range(1 , 5):
            if not (0 <= int(matches.group(num)) <= 255):
                return False
            elif matches.group(num).startswith('00'):
                return False
    return True





if __name__ == "__main__":
    main()
