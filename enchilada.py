from sys import argv

name, age = argv

name = raw_input("What is your name? ")
age = raw_input("How old are you? ")

print "%s: %s is %s old." % (name, age) 