def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "let's do some math with functions:"
a = 37
b = 25

age = add(a,b)
height = subtract(a,b)
weight = multiply(a,b)
iq = divide(a,b)

print " age: %d, height: %d, weight: %d, iq: %d" % (age, height, weight, iq)

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "%r" %(what)
