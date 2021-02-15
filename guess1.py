# Practicing exercise for "while" loops from week 4 lab
# Author: Andrew Beatty
# Program to prompt the user to guess a number

numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    print ("Wrong")
    guess = int(input("Please guess again:"))

print ("Well done! Yes, the number was ", numberToGuess)