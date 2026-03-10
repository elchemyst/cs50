def main():
    try:
        response = input("Reverse: ")
    except TypeError:
        print("Enter valid text.")
    print(reverse(response))


def reverse(response):
    if len(response) <= 1:
        return response
    else:
        blank = ''
        blank = blank.join(response[-1])
        response = response[:-1]
        return reverse(response)


main()


# demo_string = "Microsoft Co-Pilot"

# # Slice out the last character
# last_char = demo_string[-1]        # 't'

# # Remove the last character
# trimmed_string = demo_string[:-1]  # 'Microsoft Co-Pilo'

# print("Last character:", last_char)
# print("Without last character:", trimmed_string)
