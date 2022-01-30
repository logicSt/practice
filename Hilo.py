#creating a variable and defining of variable
low = 1
high = 1000

#Telling the user to think of a number between 1 and 1000 
#then press Enter to continue
print('Please think of a number between {} and {}'.format(low, high))
input('Press ENTER to start')

#Counting Variables
guesses = 1

#looping condition
while low != high:
    #formula for calculating the user guess
    guess = low + (high - low) // 2
    #asking the user if the computer guess was correct,
    #Or the computer should higher or lower.
    high_low = input('my guess is {}, Should i guess higher or lower?'
                    'Enter h or l, or c if your guess is correct '
                    .format(guess)).casefold()
    #condition to test the character the user inputs
    if high_low == 'h':
        #assigning low a new value
        low = guess + 1
    elif high_low == 'l':
        #assigning high a new value
        high = guess - 1
    elif high_low == 'c':
        #output to the user that his guess was correct
        print('I got it in {} guesses'.format(guesses))
        break   
    #if the user input any other character
    else:
        print('Please enter h, l, or c')
    #counting the number of guesses
    guesses += 1
#when low equals high the guess is correct
else:
    print('You thought of the number {}'.format(low)) 
    print('I got it in {} guesses'.format(guesses))
