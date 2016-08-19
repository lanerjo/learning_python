print "hello world"
print "Hello again"
print "i like typing this"
print "this is fun"
print "\'yay printing."
print "."*10
#
#how to use variables in printing
cars = 100 #this sets the variable cars = to 100
spaceinacar = 4.0 #this sets the variable spaceinacar to the floating point integer 4.0
drivers = 30 #this sets the variable drivers to integer
passengers = 90
carsnotdriven = cars - drivers #this subtracts the value for cars from value for drivers and sets it as a new variable carsnotdriven
carsdriven = drivers
carpoolcapacity = carsdriven * spaceinacar
averagepassengerpercar = passengers / carsdriven

print "there are ", cars, " cars available."
print "there are only ", drivers, " drivers available"
print "there will be ", carsnotdriven, "empty cars today"
print "we can transport ", carpoolcapacity, " people today"
print "we have ", passengers, "to carpool today"
print "we need to put about ", averagepassengerpercar, "in each car"
print "."*10
#
#how to embed variables inside a string
#varname = "lance"
#varage = "37"
#print "lets talk about %s." % varname
#print "lets talk about %s who is %s" % (varname, varage)

myname = 'lance zukel'
myage = 37 #the age i started learning python
myheight = 6
myweight = 180
myeyes = 'brown'
myhair = "brown"
myteethe = "white"

print "lets talk about %s" % myname
print "he is %s feet tall" % myheight
print "he's %s pounds heavy" %myweight
print "his hair is %s, and his eyes are %s" % (myhair, myeyes)
print "if i add my age %s, height %s, and weight %s i get %s" % (myage, myheight, myweight, myage + myheight + myweight)
print "."*10
""" 
this lesson shows different ways of combining strings and variables 
"""
x = "there are %s types of people." %10
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s." % (binary, do_not)
print x
print y
print "i said %r." % x
print "i also said '%s'." % y
hilarious = False
jokeevaluation = "ins't that joke so funny? %r"

print jokeevaluation % hilarious

w = "this is the left side of a string"
e = "this is the right side of a string"

print w + e
print "."*10
# new lesson - teaching how to add a space using a comma continuing the following print command on the same output line
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end of 6.  try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
print "." *10
#new Lesson

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
print "."*10
""" you should see
1 2 3 4
'one' 'two' 'three' 'four'
True False False True
'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'
You should use %s and only use %r for getting debugging information about something. The %r will give you the "raw programmer's" version of variable, also known as the "representation."
"""

# Here's some new strange stuff, remember type it exactly.
#use \n to place variable on new line
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
print "."*10

"""
\\	Backslash (\)
\'	Single-quote (')
\"	Double-quote (")
\a	ASCII bell (BEL)
\b	ASCII backspace (BS)
\f	ASCII formfeed (FF)
\n	ASCII linefeed (LF)
\N{name}	Character named name in the Unicode database (Unicode only)
\r	Carriage Return (CR)
\t	Horizontal Tab (TAB)
\uxxxx	Character with 16-bit hex value xxxx (Unicode only)
\Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (Unicode only)
\v	ASCII vertical tab (VT)
\ooo	Character with octal value ooo
\xhh	Character with hex value hh
"""
