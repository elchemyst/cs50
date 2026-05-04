#!/usr/bin/env python3


def main():
    response = input("Input: ")
    response = convert(response)
    print(response)


def convert(response):
    response = response.replace(":)", "🙂").replace(":(", "🙁")
    return response


main()
