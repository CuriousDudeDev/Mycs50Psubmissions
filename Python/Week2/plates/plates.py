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
    total_nums = 0
    for i in s:
        if i.isdigit():
            total_nums += 1
    if total_nums > 1:
        for j in range((0-total_nums) , -1):
            if not s[j].isdigit():
                return False
    for i in s:
        if i.isdigit():
            first_num = int(i)
            break
    if first_num == 0:
        return False
    puncts = ['' , '.' , '/' , '-' , '_']
    for i in s:
        if i in puncts:
            return False

    return True

main()

