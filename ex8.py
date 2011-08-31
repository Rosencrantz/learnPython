formatter = "%r %r %r %r" #It looks like this defines a function that takes four values

#Executes the formatter function a number of times with different values
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True) #syntax error
print formatter % (formatter, formatter, formatter, formatter)

#The third item here displays with double instead of single quotes because it contains a single quote as one of the characters.
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
