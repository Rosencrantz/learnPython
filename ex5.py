# -*- coding: utf-8 -*-

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
lbs_in_kg = 2.20462262185
cm_in_inch = 2.54;
print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
print "My weight in Kg is %f" % (weight / lbs_in_kg)
print "My height in cm is %f" % (height * cm_in_inch)

#String conversion types
#'d'	Signed integer decimal.	 
#'i'	Signed integer decimal.	 
#'o'	Signed octal value.	(1)
#'u'	Obsolete type – it is identical to 'd'.	(7)
#'x'	Signed hexadecimal (lowercase).	(2)
#'X'	Signed hexadecimal (uppercase).	(2)
#'e'	Floating point exponential format (lowercase).	(3)
#'E'	Floating point exponential format (uppercase).	(3)
#'f'	Floating point decimal format.	(3)
#'F'	Floating point decimal format.	(3)
#'g'	Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.	(4)
#'G'	Floating point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.	(4)
#'c'	Single character (accepts integer or single character string).	 
#'r'	String (converts any Python object using repr()).	(5)
#'s'	String (converts any Python object using str()).	(6)
#'%'	No argument is converted, results in a '%' character in the result.
