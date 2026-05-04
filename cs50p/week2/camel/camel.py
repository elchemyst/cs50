def main():
    response = input('camelCase: ')
    print('snake_case: ' + tosnake(response))


def tosnake(word):
    temp = []
    for letter in word:
        if letter.isupper():
            temp.append('_')
            temp.append(letter.lower())
        else:
            temp.append(letter)
    snake_case = ''
    snake_case = snake_case.join(temp)
    return snake_case


main()
