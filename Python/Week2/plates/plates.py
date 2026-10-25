def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
            return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    if not (s[-1].isdigit()):
        return False
    for i in s:
        if i.isdigit():
            first_num = i
            break
    if first_num == 0:
        return False

    return True

main()

