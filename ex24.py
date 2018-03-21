# Print the below lines. The first two escapes allows the ' to show.
# The third escape will allow for the slash to show.
# the \n will add a new line and the \t a tab
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

# Ths is setting variable poem as the the below. The triple " allows to print across
# lines. The \t will tab, the \n will start and new line and the \n\t\t will start
# a new line with two tabs.
poem = """
\t The lovely world 
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none. 
"""

print "----------"
# will print the poem variable
print poem
print "----------"

# the variable 'five' as the numeric value of the below expression which should be 
# 5
five = 10 - 2 + 3 - 6 

# printing the variable within the string
print "This should be five: %s" % five 

# setting the function secret_formula which calls one argument
def secret_formula(started):
	# this sets jelly beans as whatever argument/number was entered as that * 500
    jelly_beans = started * 500 
    # sets jars as the number that jelly_beans was set as divided by 500
    jars = jelly_beans / 1000
    # sets crates as the number that jars was set as divided by 100
    crates = jars / 100 
    # this will return values for three variables; so we started with 1 number (started), 
    # and this function will return 3 values
    return jelly_beans, jars, crates 

# setting the start point as 1000
start_point = 10000

# the function secret_formula will return three values. We are now setting beans as the first
# value as opposed to jelly_beans
beans, jars, crates = secret_formula(start_point)

# setting start_point to print inside the string
print "With a starting point of: %d" % start_point

# setting the three values returned to print inside this string
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# setting a new start_point that will take the previously set value and divide it by 10
start_point = start_point / 10 

print "We can also do that this way:"

# calling the function secret_formual to print the three output values directly in this string
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)