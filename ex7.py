# print out the first line of the poem
print "Mary had a little lamb."

#print out the second line and pass in the string value 'snow'
print "Its fleece was white as %s." % 'snow'

#print out the third line
print "And everywhere that Mary went."

print "." * 10 #What'd that do? (repeats the '.' character the specified number of times (..........)

#create a variable for each letter of the word cheeseburger
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
# the comma at the end of the line seems to work as a continuation of the line, inserting a space then printing everything from the line below
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

#The lines above concatenate the variables and print them to the screen
