#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')                 #Printed Intro
colors = ['red','orange','yellow','green','blue','violet','purple']  #A list of colors
play_again = ''                         # A variable to keep track if the player wants to try again.
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'):       #Loop tracking if the player chose to not try again
    match_color = random.choice(colors)    #Setting a random color for the player to guess
    count = 0                       #Starting the count variable
    color = ''                      #Starting the input color variable
    while (color != match_color):   #A While loop that will end when the player guesses correctly
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip()      #Removing cases and spaces from the input
        count += 1                          #Adding to the color variable
        if (color == match_color):          #Checking if the player guessed right
            print('Correct!')               #Printing result
        else:                               #If the player didn't guess right
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))     #Printing results and number of tries
    print('\nYou guessed it in {0} tries!'.format(count))   #When the color matches the random one, this prints
    if (count < best_count):                #if the player guessed in the least tries...
        print('This was your best guess so far!')   #this will print
        best_count = count                  #reassigning the record
    play_again = input("\nWould you like to play again? ").lower().strip()  #Takes input on if the player wants to play again, while remmoving cases and spaces.
print('Thanks for playing!')        #Printed Outro