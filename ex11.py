print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
age, height, weight)

# Input tries to read inputs like they're python code, which can cause problems. 
# For example, if for height I put in 5'5" the next line won't run, because the " is taken as a closure of the string.
print "How old are you?",
age = input()
print "How tall are you?",
height = input()
print "How much do you weigh?",
weight = input()

print "So, you're %r old, %r tall and %r heavy." % (
age, height, weight)
