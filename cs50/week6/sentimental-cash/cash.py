#!/usr/bin/env python3
import cs50


def main():
    while True:
        cents = cs50.get_float("Enter cash received: ")
        cents_1 = cents * 100
        if cents >= 0:
            break

    quarters = calculate_quarters(cents_1)
    cents_1 = cents_1 % 25

    dimes = calculate_dimes(cents_1)
    cents_1 = cents_1 % 10

    nickels = calculate_nickels(cents_1)
    cents_1 = cents_1 % 5

    pennies = calculate_pennies(cents_1)

    pay_back = int(quarters + dimes + nickels + pennies)
    print(f"{pay_back}")


def calculate_quarters(cents):
    return int(cents / 25)


def calculate_dimes(cents):
    return int(cents / 10)


def calculate_nickels(cents):
    return int(cents / 5)


def calculate_pennies(cents):
    return int(cents)


main()
