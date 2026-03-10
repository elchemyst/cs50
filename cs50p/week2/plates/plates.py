def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[0:2].isalpha():
        return False
    elif len(s) < 2 or len(s) > 6:
        return False
    elif check_num(s) is False:
        return False
    elif not s.isalnum():
        return False
    return True


def check_num(s):
    a_list = []
    for l in s:
        if l.isdigit():
            a_list.append(l)
        if l.isdigit() & s[-1].isalpha():
            return False
    if len(a_list) != 0:
        if a_list[0] == '0':
            return False


main()
