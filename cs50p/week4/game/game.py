import random


# Prompt user for level
while True:
    try:
        n = int(input('Level: '))
        if n > 0:
            break
    except ValueError:
        pass

# Set a target number
levels = [1]
while len(levels) < n:
    levels.append(len(levels) + 1)
target = random.choice(levels)

# Prompt user to guess
while True:
    try:
        guess = int(input('Guess: '))
        if guess > 0:
            if guess < target:
                print('Too small!')
            elif guess > target:
                print('Too large!')
            else:
                print('Just right!')
                break
    except ValueError:
        pass
