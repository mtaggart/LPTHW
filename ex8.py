formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
# on the below line, I didn't close the last set of quotes
print formatter % ("one", "two", "three", "four")
# I don't need quotes around True & False because python recognizes them as keywords meaning True or False. Quotes would turn them into a string.
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
"I had this thing.",
"That you could type up right.",
# this line prints using double instead of single quotes around this line because there is an apostrophe, which it reads as a single quote, within the string
"But it didn't sing.",
"So I said goodnight."
)	