
guessVal = 50
print('Please think of a number between 0 and 100!')
guess = raw_input('Is your secret number '+str(guessVal)+ '? ')
hVal = 100
lVal = 0

while guess!='c':
    if guess == 'h':
        hVal = guessVal
        guessVal = (lVal+hVal)/2
        # need to add a marker stating # is always lower
    elif guess == 'l':
        lVal = guessVal
        guessVal = (hVal+lVal)/2
        # need to add a marker stating # is always higher
    else:
        print('Sorry, I did not understand your input.')
    guess = raw_input('Is your secret number ' + str(guessVal) +'? ')
    