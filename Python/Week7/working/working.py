import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s = s.strip()
    pattern = re.search(r"(\d{1,2})(:| )?(/d{2})?(| )AM to (\d{1,2})(:| )?(/d{2})?(| )PM)",s)
    if pattern:
        return True
    else:
        return False


...


if __name__ == "__main__":
    main()
