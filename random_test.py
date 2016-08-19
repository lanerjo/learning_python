from random import randint
from sys import exit
name = raw_input("Hello! What's your name? ")
print "Well %s, I'm thinking of a number between 1 and 20." % name
print "Since I'm a benevolent computer program, I'll give you 6 guesses."
secret_number = randint(1, 20)

guesses_left = 6
already_guessed = []

while guesses_left > 0:
    try:
        guess = int(raw_input("Take a guess: "))

        if guess <= 1 and guess >= 20 and guess not in already_guessed:
            already_guessed.append(guess)
            guesses_left -= 1

        elif guess == secret_number:
            print "You win! %d was my secret number!" % secret_number
            exit(0)
        elif guess < secret_number:
            print "Your guess is too low!"
        elif guess > secret_number:
            print "Your guess is too high!"

        elif guess in already_guessed:
            print "You already guessed that!"

        else:
            print "Not a number between 1 - 20!"
            print "Please try again!"

        print "You have %d guesses left!" % guesses_left

    except ValueError:
        print "Invalid input! Please try again!" 