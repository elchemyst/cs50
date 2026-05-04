import math


def main():
    time = input('What time is it? ')
    time = convert(time)
    if time is None:
        print('Invalid time')
    elif 7 <= time <= 8:
        print('breakfast time')
    elif 12 <= time <= 13:
        print('lunch time')
    elif 18 <= time <= 19:
        print('dinner time')


def convert(time):
    if time.split(':')[-1].isdigit():
        x, y = time.split(':')
        x = int(x)
        y = int(y)
        y = y / 60
        return x + y
    elif time.split(' ')[-1] in ('a.m.', 'A.M.', 'am', 'AM') or time.split(' ')[-1] in ('p.m.', 'P.M.', 'pm', 'PM'):
        x, y = time.split(':')
        x = int(x)
        y = y.split(' ')[0]
        y = int(y)
        y = y / 60
        if x + y >= 13:
            return None
        else:
            return x + y


if __name__ == '__main__':
    main()
