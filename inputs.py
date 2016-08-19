###inputs and variables
print "how old are you?",
age = raw_input()
name = raw_input("What shall I call you?")
height = raw_input("how tall are you?")
print "how much do you weigh?",
weight = raw_input()

print "so you are %s old, %s tall and %s heavy."  %(age, height, weight)
print "."*10
print "Hi %s, I'm the program." % (name)
lives = raw_input("Where do you live?")
computer = raw_input("What type of computer are you using?")
print """
Alright %s year old, %s, who weighs %s, and lives in %s, 
you are using a %s computer.""" %(age, name, weight, lives, computer)
print "."*10
