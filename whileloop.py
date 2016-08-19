i= 0
numbers = []

while i < 6:
    print "at the top i is %d" % i
    numbers.append(i)
    
    i += 1
    print "numbers so far: ", numbers
    print "at this bottom i is %d " % i

print "the numbers: "

for num in numbers:
    print num