from sys import argv
script, filename = argv

# this opens the filename and returns a txt file object
txt = open(filename)
print "Here's your file %r:" % filename
print txt

# this calls the read command on the txt file object
print txt.read()

print "type the filename again:"
file_again = raw_input("> ")

# this again opens the file_again string which is what we get from the input
txt_again = open(file_again)
print txt_again.read()
