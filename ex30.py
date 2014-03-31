people = 10
cars = 10
buses = 15

# if branch is carried out if the Boolean Statement is True.
if cars > people:
	print "We should take the cars."
# elif branch is carried out if the Boolean Statement is True
elif cars < people:
	print "We should not take the cars."
# else branch prints if neither if nor elif branches are True
else:
	print "We can't decide."
	
if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."
	
if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."