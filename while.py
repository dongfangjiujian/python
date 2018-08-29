number = 23
running = True

while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('guessed')
        running = False
    elif guess<number:
        print('no 1')
    else:
        print('no 2')
else:
    print('loop is over')

print('done')