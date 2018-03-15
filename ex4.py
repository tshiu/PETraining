cars = 100
space_in_a_car = 4
drivers = 30 
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven 

#should print the text in yellow and calculate the variables, 100 will replace cars
print "There are", cars
# drivers will be replaced with 30
print "There are only", drivers, "drivers available."
# cars_not_driven will be replaced with 70
print "There will be", cars_not_driven, "empty cars today,"
# carpool_capacity will be replaced with cars_driven * space_in_car
print "We can transport", carpool_capacity, "people today."
# calculations!
print "We have", passengers, "to carpool today."
# calculations!
print "We need to put about", average_passengers_per_car, "in each car."

#Study Drill
#1. No, this is not neccessary. If you replace it with an integer, then the response will also be 
#   in an integer. 
#2. Floating point numbers are non integers. They written in binary; so fractions are only estimations.
#3. Above
#4. Yes!
#5. Yes! 
#6. Ran in python. Can set variables and then multiply variables
