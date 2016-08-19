filename = raw_input("Please input name of file to open...")
txt = open(filename)

print "here's your file %s:" % (filename)
print txt.read()


txt.close()

print "now we are going to erase the contents of the file"
target = open(filename, 'w')
target.truncate()
print "truncating file"

target.truncate()

	
		
print "Now you are going to type in three lines to write to the file"
line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")
print "Now I am writing them to the file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write('\n')
print "Now I am going to close the file"
target.close()
print "now we check our work"
targetnew = open(filename)
print "here is the new content of your file..."

print targetnew.read()
targetnew.close()