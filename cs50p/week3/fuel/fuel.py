while True:
    try:
        fraction = input('Fraction: ')
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)
        z = round(x * 100 / y)
        if z <= 1:
            print('E')
        elif z >= 99:
            print('F')
        else:
            print(str(z) + '%')
        break
    except ValueError:
        print('Enter fraction in the form: x/y')
    except ZeroDivisionError:
        print("Can't divide by 0")
