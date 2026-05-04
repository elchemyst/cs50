#!/usr/bin/env python3
import re



def main():
    number = input("Enter card number: ")
    number = prep(number)
    regex_1 = '^(?:\d{13}|\d{15}|\d{16})$'

    match = re.match(regex_1, number)
    if not match:
        print("INVALID")
        exit(1)
    matched_string = match.group(0)
    length = len(matched_string)

    num = number
    #verification by Luhn's Algorithm
    products = list()
    for char in num[-2::-2]:
        products.append(str(int(char) * 2))
    sum_1 = 0
    #add the digits of the products (not the products themselves)
    for product in products:
        for digit in product:
            sum_1 += int(digit)
    #add sum to sum of digits that weren't multiplied by 2
    sum_2 = 0
    for char in num[-1::-2]:
        sum_2 += int(char)
    sum = sum_1 + sum_2
    #if total's last digit is 0, number is valid
    if sum % 10 == 0:
        if length == 13 or length == 16:
            if num[0] == '4':
                print("VISA")
            regex_2 = '[1-5]'
            if num[0] == '5' and re.match(regex_2, num[1]) is not None:
                print("MASTERCARD")
        if length == 15:
            if num[0] == '3' and (num[1] == '4' or num[1] == '7'):
                print("AMEX")
    else:
        print("INVALID")


def prep(number):
    for char in number:
        if char.isalpha():
            print("INVALID")
            exit(1)
    number = number.replace('-', '')
    number = number.replace(',', '')
    number = number.replace(' ', '')
    return number


main()
