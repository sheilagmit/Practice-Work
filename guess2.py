# Practicing exercise for "while" loops from week 4 lab
# Author: Andrew Beatty
# Program to prompt the user to guess a number (with hint)


numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print ("Too low")
    else: # I know it can't be equal or too low, so it must be too high
        print ("Too high")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was ", numberToGuess)
