tabby_cat = "\tI'm tabbed in"
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#Escape Sequence	Meaning	Notes
#\newline	Ignored	
#\\	Backslash (\)	
#\'	Single quote (')	
#\"	Double quote (")	
#\a	ASCII Bell (BEL)	
#\b	ASCII Backspace (BS)	
#\f	ASCII Formfeed (FF)	
#\n	ASCII Linefeed (LF)	
#\N{name}	Character named name in the Unicode database (Unicode only)	
#\r	ASCII Carriage Return (CR)	
#\t	ASCII Horizontal Tab (TAB)	
#\uxxxx	Character with 16-bit hex value xxxx (Unicode only)	(1)
#\Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (Unicode only)	(2)
#\v	ASCII Vertical Tab (VT)	
#\ooo	Character with octal value ooo	(3,5)
#\xhh	Character with hex value hh	(4,5)
