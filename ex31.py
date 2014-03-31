print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear
		
elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job"
		
else:
	print "You can stay in the room, or you can go back where you came from."
	print "1. Stay in the room."
	print "2. Go back where you came from."
	
	leave = raw_input("> ")
	
	if leave == "1":
		print "You find a genie in a bottle, who gives you one wish."
		print "1. You can be transported to Thailand."
		print "2. You can be transported to Afghanistan."
		print "3. You can watch movies and eat popcorn in this dark room forever."
		
		wish = raw_input("> ")
		
		if "1" <= wish <= "2":
			print "Yay! Vacation! You're the winner!"
#		elif wish == "2":
#			print "You become an international arms dealer. You're the winner!"
		elif wish == "3":
			print "Did he forget to tell you it's Kettle Corn? Gross. You lose."
		else:
			print "That wasn't an option. You burst into flames. You lose." 
			
	elif leave == "2":
		print "Good decision. There's more vitamin D outside. You win!"
		
	else:
		print "Okay, you make all the decisions. You're the decider!"