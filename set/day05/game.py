import random


while True:
    try:
        n =int(input('Level: '))
    except ValueError:
        continue
    if n > 0:
        break

right = random.randint(1,n)

while True:
    try:
        guess = int(input('Guess: '))
    except ValueError:
        continue
    if guess <= 0:
        continue
    elif guess > right:
        print('Too large!')
    elif guess < right:
        print('Too small!')
    else:
        print('Just right!')
        break