#Define a string and pass a number into it
x = "There are %d types of people" % 10

#Define another string variable
binary = "binary"

#define another string variable
do_not = "don't"

#Define a string variable and pass the two preceeding string variables into it
#string in string (1)
y = "Those who know %s and and those who %s." % (binary, do_not)

#print the x and y variables to the screen
print x
print y

#print two strings and pass the x/y strings into them
#string in string (2 & 3)
print "I said: %r." % x
print "I also said: '%s'." % y

#Define a boolean value
hilarious = False;

#Define a string which takes a boolean values
joke_evaluation = "Isn't that joke so funny?! %r"

#Display the previous string passing in the hilarous boolean value
#string in string (4)
print joke_evaluation % hilarious

#Define two more strings
w = "This is the left side of..."
e = "a string with a right side."

#concat the w and e strings and print to the screen
print w + e
