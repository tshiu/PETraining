# this puts a tab on the line
tabby_cat = "\tI'm tabbed in."

# this 'enters' the line, puts in on a new space
persian_cat = "I'm split\non a line."

# this escapes the slashes so that the slashes will actually
# show and aren't doing a command
backslash_cat = "I'm \\ a \\ cat."

# this allows you to pring across multiple rows
# the tabs work as tabs
# the \n will enter a new line
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# this will print the above variables
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat