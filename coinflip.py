import random

print "This is the coin flip guessing game!!!"
print "I am going to flip a coin 100 times,"
print "Can you guess how many time the coint will land on heads?"
guess = int(input("Your Guess>>>"))
flips = 0
heads = 0
while flips < 100:
    if random.randint(0,1) ==1:
        heads = heads + 1
    flips += 1
print heads
if heads == guess:
    print ("That must've been a lucky guess!!!")
elif heads < guess - 10 and heads > guess + 10:
    print "You were close"
else:
    print "Sorry but that is incorrect"
