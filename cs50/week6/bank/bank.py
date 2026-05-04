#!/usr/bin/env python3
def main():
    bill = 0
    greeting = input("Greeting: ")
    greeting = greeting.strip().lower()
    if (greeting[0] != 'h'):
        bill = 100
    elif (greeting[0:5] != "hello"):
        bill = 20
    print(f"${bill}")


main()

