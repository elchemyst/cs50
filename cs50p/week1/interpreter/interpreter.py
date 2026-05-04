x, y, z = input('Expression: ').split(' ')
x = float(x)
z = float(z)
match y:
    case '+':
        add = x + z
        print(f'{add:.1f}')
    case '-':
        difference = x - z
        print(f'{difference:.1f}')
    case '*':
        product = x * z
        print(f'{product:.1f}')
    case '/':
        quotient = x / z
        print(f'{quotient:.1f}')


