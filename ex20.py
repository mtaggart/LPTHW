# importing command argv
from sys import argv

# defining argv variables
script, input_file = argv

# defining the function print_all for variable f
def print_all(f):
# function applies function 'read' to argument f and prints it to the screen
	print f.read()

# applies 'rewind' function to object f 	
def rewind(f):
	f.seek(0) # go to the 1st byte ie. offset to start of file
	
# defines print_a_line function for these two objects, being assigned variables line_count and f
def print_a_line(line_count, f):
# prints variable line_count and applies method readline to object f without any parameters
	print line_count, f.readline()
	
current_file = open(input_file) # defines current_file variable as the opened input file

print "First, let's print the whole file:\n" # prints string and moves to a new line

print_all(current_file) # calls print_all function on the current file (which was defined above)

print "Now let's rewind, kind of like a tape." # prints string

rewind(current_file) # calls rewind function on the current file

print "Let's print three lines:" # prints string

current_line = 1 # defines current_line variable as 1
print_a_line(current_line, current_file) # calls print_a_line function for current_line as variable line_count

current_line += 1 # defines current_line variable as previous current line + 1 (next line), 2
print_a_line(current_line, current_file) # calls print_a_line function for current_line, defined above as former current_line + 1, as variable line_count

current_line += 1 # defines current_line variable as previous current line + 1 (next line), 3
print_a_line(current_line, current_file) # calls print_a_line function for current_line, defined above as former current_line + 1, as variable line_count
