from cs50 import get_int


def main():
    height = 0
    while height <= 0 or height >= 9:
        height = get_int("Enter height: ")
    pyramid(height)


def pyramid(height):
    for i in range(height):
        for j in range(height - (i + 1)):
            print(" ", end="")
        for j in range(i + 1):
            print("#", end="")
        print("")


main()
