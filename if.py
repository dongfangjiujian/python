number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    #new block
    print('you guessed it.')
    #new block end
elif guess<number:
    # anthor block
    print('no, it is a little higher than that')
else:
    print('no, it is a little lower than that')

print('Done')
