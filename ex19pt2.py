def cat_toys(cats_count, toys_count):
	print "We have %d cats." % cats_count
	print "They each have %d cat toys." % toys_count
	print "That means we have %d cat toys total." % (cats_count * toys_count)
	print "That's a lot of cats and toys!\n"
	
print "Direct input numbers:"
cat_toys(2, 3)

print "Using math:"
cat_toys(1 + 1, 2 + 1)

print "Using new variables:"
number_of_cats = 2
number_of_toys = 3

cat_toys(number_of_cats, number_of_toys)

print "Using variables and math:"
cat_toys(number_of_cats + 1, number_of_toys + 2)

print "Using more variables and math:"
new_cats = 1
new_toys = 1

cat_toys(number_of_cats + new_cats, number_of_toys + new_toys)

print "Using more variables:"
new_number_of_cats = (number_of_cats + new_cats)
new_number_of_toys = (number_of_toys + new_toys)

cat_toys(new_number_of_cats, new_number_of_toys)

print "Adding a new toy a week:"
week1_cats = (number_of_cats)
week1_toys = (number_of_toys)
print "To start, we have %d cats." % week1_cats
print "To start, we have %d toys.\n" % week1_toys

week2_cats = (week1_cats + 1)
week2_toys = (week1_toys + (week2_cats * 1))

print "Next week, if we get a new cat and toy for each, we will have %d cats." % (week2_cats)
print "Next week, if we get a new cat and a toy for each, we will have %d toys.\n" % (week2_toys)

cat_toys(week2_cats, week2_toys)

print "Using user inputs:"

my_cats = raw_input("How many cats do you have?: ")
my_cattoys = raw_input("How many cat toys do each of them have?: ")

cat_toys(int(my_cats), int(my_cattoys))

