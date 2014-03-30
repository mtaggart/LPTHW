# Here's some new strange stuff. Remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
# I first typed these backslashes as forward slashes. It didn't work and just printed the literal string, ns included. 
# The \n advances the next character(s) to a new line. \n is a "new line character"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
