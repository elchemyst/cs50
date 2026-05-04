response = input('Input: ')
a_list = []
for letter in response:
    if letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
        a_list.append(letter)
reply = ''.join(a_list)
print(reply)
