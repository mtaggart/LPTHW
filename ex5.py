name = 'Meredith L Taggart'
age = 28 # not a lie
height = 65.5 # inches
weight = 115 # lbs
eyes = 'brown'
teeth = 'white'
hair = 'brown'

print "Let's talk about %s." % name
print "She's %f inches tall." % height
print "She's %f pounds heavy." % weight
print "Actually that's not too heavy."
print "She's got %r eyes and %r hair." % (eyes, hair)
print "Her teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (age, height, weight, age + height + weight)