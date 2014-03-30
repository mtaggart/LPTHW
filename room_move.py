# Generic room class

class Room():
# This class represents any area of the created world.

	def __init__(self, name="", descr=""):
		self.name     = name		# Name of the room
		self.descr    = descr		# Description displayed on entry
		self.populace = []			# List of people-type things in the room
		self.choices  = []			# Options in the room, some of which move to other rooms

# 		
	def move_to(self, person):
	
		# Delete person (self) from old room, add to new room
		old_room = person.location
		self.   populace.append(person)
		old_room.populace.remove(person)

		# Change person's knowledge of where s/he is
		person.location = self
	
	def display(self):
		print "Room", self.name, "contains",
#		print "POPULACE = ", self.populace
		if self.populace:
			for person in self.populace:
				print person.name,
		else:
			print "nobody",
		print ""
	

	
class Person():
# This class represents a non-player character
	
	def __init__(self, name = "", age = 0, location = None):
		self.name     = name
		self.age      = age
		self.location = location	# Room that contains the person

	#--------------------

	def move_to(self, new_room):
	
		# Delete person (self) from old room, add to new room
		old_room = self.location
		new_room.populace.append(self)
		old_room.populace.remove(self)

		# Change person's knowledge of where s/he is
		self.location = new_room
		
	#--------------------
	
	def display(self):
		print "Person", self.name, "is age", self.age, "and at", self.location.name

#===================================================================================

# Make three rooms: home, club, and Playground.
# Make a character named Brett; start him at the Playground

print "\n***   SETUP   ***"
Brett = Person("Brett", 12)

home = Room("home", "Welcome home")
home.display()

play = Room("Playground", "The place for swingers")
play.display()

club = Room("club", "You've found the hot spot of Portland")
club.display()

play.populace.append(Brett)
Brett.location = play
play.display()
Brett.display()
assert (play.populace[0] == Brett)

print "\n***   Brett GOES home   ***"
home.move_to(Brett)
home.display()
play.display()
Brett.display()
assert (play.populace    == [])
assert (home.populace[0] == Brett)
assert (Brett.location   == home)

print "\n***   Brett GOES TO THE club   ***"
Brett.move_to(club)
home.display()
club.display()
Brett.display()
assert (home.populace    == [])
assert (club.populace[0] == Brett)
assert (Brett.location   == club)
