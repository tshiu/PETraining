# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
     'CA': 'San Francisco',
     'MI': 'Detroit',
     'FL': 'Jacksonville'
}

# add some more cities
#adding new entries to the dictionary cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities 
print '-' * 10
#will print the string and then will call for the entry/definition associated with NY in cities
print "NY State has: ", cities['NY']
#will print the string and call for the entry/definition associated with OR in cities
print "OR state has: ", cities['OR']

# print some states 
print '-' * 10 
#will print the definition associated with Michigan in the states dictionary
print "Michigan's abbreviation is: ", states['Michigan']
#will print the definition associated with Florida in the state dictionary
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
#first we return teh definitation associated with Michigan in states (MI), then we return
#the definition associated with MI in cities (Detroit)
print "Michigan has: ", cities[states['Michigan']]
#first we return the definition associated with Florida in states (FL,) then we return the
#definition associated with FL in cities (Jacksonville)
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
# return the definition associated with Michigan in states
print "Michigan's abbreviation is: ", states['Michigan']
# return the definition associated with Florida in states 
print "Florida's abbreviation is: ", states['Florida']

# print every state abbreviation
print '-' * 10
#setting a for loop that executes the tabbed function for each item in the list
#for each state, abbrev pair in the states dictionary, print the string with
#the nested variable 
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10 
#setting a for loop that executes the tabbed function for each item in the list
#for each abbrev,city pair in the cities dictionary, print the string with the
#nest variables of the pairs
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
#setting a for-loop
#for each state,abbrev pair in the states dictionary 
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '-' * 10 
# safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city 


#SD
#1

neighborhoods = {
	'Manhattan':'Soho',
	'Brooklyn':'Park Slope',
	'Queens':'Astoria', 
	'Bronx':'Riverdale',
	'Staten Island':'?',
}

boroughs = {
	'Manhattan':'NY',
	'Brooklyn':'BK',
	'Bronx':'BX'
}

print neighborhoods['Manhattan']

#2 https://docs.python.org/3/tutorial/datastructures.html#dictionaries

print neighborhoods

for k, v in neighborhoods.items(): 
	print (v, " is located in ",te k)

#3 This was helpful: https://stackoverflow.com/questions/3489071/in-python-when-to-use-a-dictionary-list-or-set 
# Dictionaries do not keep order


