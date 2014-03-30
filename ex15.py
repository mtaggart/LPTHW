# This line imports module argv through the sys stored modules
from sys import argv

# This line assigns variables to be held by argv
script, filename = argv

# Defines txt by asking that the specified file is opened.
txt = open(filename)

# Prints the filename.
print "Here's your file %r:" % filename
# Commands that txt within the previously specified file is read to the screen without any parameters.
print txt.read()

# Prints the string
print "Type the filename again:"
# Defines the variable "file_again" as whatever filename is typed in by the user
file_again = raw_input('>')

# Defines the variable and opens raw input file
txt_again = open(file_again)

# Reads and prints to the screen the new file without any parameters
print txt_again.read()

txt_again.close()
txt.close()