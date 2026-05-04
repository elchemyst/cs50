import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x, y = generate_integer(level), generate_integer(level)
        x, y = int(x), int(y)
        z = x + y
        for attempt in range(3):
            try:
                sum = int(input(f'{x} + {y} = '))
            except ValueError:
                pass
            if sum == z:
                score += 1
                break
            elif attempt != 2:
                print('EEE')
            else:
                print('EEE')
                print(f'{x} + {y} = {z}')

    print('Score: ' + str(score))

def get_level():
    level = str()
    while level not in ('1', '2', '3'):
        level = input('Level: ')
    return level

def generate_integer(level):
    if level == '1':
        return random.randint(0, 9)
    elif level == '2':
        return random.randint(10, 99)
    elif level == '3':
        return random.randint(100, 999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()
