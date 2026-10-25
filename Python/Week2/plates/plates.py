def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (s[0] isalpha() and s[1] is alpha()):
        return False
    if len(s) > 6 or len(s) < 2:
        return False
    if s[-1].isdigit():
        return False

main()

