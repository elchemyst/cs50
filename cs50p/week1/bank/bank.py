response = input('Greet: ').lower().lstrip()
if response.startswith('hello'):
    print('$0')
elif response[0] == 'h':
    print('$20')
else:
    print('$100')
