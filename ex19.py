# this section defines the function in pink, starting with variables and text to print
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
# this section prints text, then directly feeds information to the function previously defined
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# this section prints text, then feeds information to the previously defined function by creating
# and defining new variables to feed to the function
print "OR we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# this section uses math to feed data to the function 
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# this section uses variables defined in a previous loop combined with math to feed
# data to the function
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)