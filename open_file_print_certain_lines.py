filename = raw_input("Name of file to open?")

inputfile = open(filename)

def printall(f):
    print f.read()

def rewind(f):
    f.seek(0)

def printline(line_count, f):
    print line_count, f.readline()

print "first lets print the whole file: \n"
printall(inputfile)

print "now lets rewind, kind of like a tape"
rewind(inputfile)

print "lets print 3 lines:"
current_line = 1
printline(current_line, inputfile)

current_line = current_line + 1
printline(current_line, inputfile)

current_line = current_line + 1
printline(current_line, inputfile)

