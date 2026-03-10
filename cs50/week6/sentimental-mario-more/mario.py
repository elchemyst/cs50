from cs50 import get_int

def main():
    while True:
      height = get_int("Enter height: ")
      if (height > 0 and height < 9):
        break
    pyramids(height)


def pyramids(height):
    for i in range(height):
      #1st pyramid
      for j in range(height - (i + 1)):
        print(" ", end="")
      for j in range(i + 1):
        print("#", end="")
        #2 spaces
      for j in range(height, height + 2):
        print(" ", end="")
        #2nd pyramid
      for j in range(height + 3, height + 3 + (i + 1)):
        print("#", end="")
      print("")


main()
