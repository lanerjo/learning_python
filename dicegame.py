import sys
import random


def rolldice():
    raw_input("Press 'enter' when ready")
    a = random.randrange(1,6)
    b = random.randrange(1,6)
    c = random.randrange(1,6)
    print a
    print b
    print c
    dice = a + b + c
    print "total %r" % (dice)
    return dice

name = raw_input("What is your name?")
print "Hello %s, nice to meet you." % (name)
def playmod():
    play = raw_input("Would you like to play a game?").lower()
    if play == "yes" or play == "y":
        print "Ok we can start playing now."
        return
    elif play == "no" or play == "n":
        print "Thank you... Have a nice day..."
        sys.exit(0)
    else:
        print "You didn't pick Yes or No... Please try again..."
    playmod()

playmod()

print "The game works like this...\n"
print "There are 3 dice that will roll...\n"
print "We will both get a number...\n"
print "The one with the highest number wins...\n"

def myturn():
    print "Rolling my dice!!!"
    rolldice()
    mydice = rolldice()
    return mydice

def playerturn():
    print "Rolling your dice!!!"
    rolldice()
    playerdice = rolldice()
    return playerdice

def playgame():
    myturn()
    playerturn()
    if myturn() > playerturn() :
        print "I win"
        sys.exit(0)
    elif myturn() == playerturn():
        print "Tie"
        sys.exit(0)
    else:
        print "You win"
        sys.exit(0)

    

playgame()
print playerdice


