## Animal is-a object(yes, sort of confusing) look at the extra credit
class Animal(object):
	def __init___(self, name):
		self.name = name
		
	def numberLegs(self, legs):
		print "This animal has %s legs" % legs

## Dog is-a Animal 
class Dog(Animal):

	def __init__(self, name, legs):
		## class Dog has-a init that takes the parameter self and name 
		self.name = name 
	
	

## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## class Animal has-a init that takes the parameter self and anme
		self.name = name 
	def cat_scratch(self):
		print "Only cats scratch."

## Person is-a object
class Person(object):
	def __init__(self, name):
		## class Person has-a init that takes the parameter self and name
		self.name = name 

		## Person has-a pet of some kind 
		self.pet = None 

## Employee is-a person
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		# from python docs "super can be used to refer to parent classes without 
		#naming them explicitly, thus making the code more maintainable."
		#second use case stated is that it support cooperative multiple inheritance
		super(Employee, self).__init__(name)
		## Employee has a salary attribute
		self.salary = salary 

## Fish is-a object
class Fish(object):
	def __init__(self, name, fins):
		self.name = name
		self.fins = fins
	

## Salmon is-a Fish
class Salmon(Fish):
	def __init__(self, name, fins):
		self.name = name
		self.fins = fins
	def has_fins(self):
		print "Fish have fins." 

## Hailbut is-a Fish 
class Halibut(Fish):
	def __init__(self, name, fins):
		self.name = name
		self.fins = fins 

## rover is-a Dog
#Set rover to an instance of Class Dog which has-a attribute of name set to Rover.
#Class Dog has-a init that takes the parameters of self and name. 
rover = Dog("Rover", 4)

##Set satan to an instance of Class Cat which has-a attribute name set to Satan. 
#Class Cat has a init that takes the parameter of self and name.
satan = Cat("Satan")

##Set mary to an instance of Class Person which has-a attribute name set to Mary.
#Class Person has-a init that takes hte parameter of self and name. 
#Class Persom has-a pet of some kind. 
mary = Person("Mary")

##from mary(an instnance of Class Person) get attribute pet and set it to 'Satan'
mary.pet = satan 

##Frank is-a Employee instance which has-a attribute name "Frank" and 
#a salary attribute 120000
frank = Employee("Frank", 120000)

##from Frank (Employee instance)get the attribute pet and set it to rover
#pet attribute is-a rover
frank.pet = rover 

## flipper is-a Fish instance
flipper = Fish("Flipper", 5)

## crouse is-a Salmon instance
crouse = Salmon("Crouse", 2)

## harry is-a Halibut instance 
harry = Halibut("Harry", 3)

#SD
#1. Python has the class object so that one can create a new type of objects
#and each new instance can have their own attributes. For example, Dog and Cat
#are both instances of of the animal object which is a class. Each instance
#can then be modified independently. 
#2. Yes, because class is-a object inherently.
#3. 
#This will print "This animal has 4 legs". becaause the function is defined in
#Animal and the rover is-a Dog which is-a animal so from rover, we can call
#the function numberLegs because it was inherited from animal.
rover.numberLegs(4)
#The below function is only in the Cat instance of the animal object so we can
#call it with the satan instance but not with rover. If we attempt to call it 
#with rover, it will state that the Dog object has no attribute of cat_scratch.
#rover.cat_scratch()
satan.cat_scratch()
crouse.has_fins()
#4. Squidword! 
#5. 
class Cleverite(object):
	def __init__(self, name, facts):
		self.name = name
		self.facts = ['height','age']
	def age(self):
		print self.facts[1]
T = Cleverite("Tracey", (['65 inches', '26 years']))

print T.name
print T.facts[1]

#6. 
#Read https://docs.python.org/2/tutorial/classes.html#multiple-inheritance 
#https://www.python-course.eu/python3_multiple_inheritance.php
#but am still quite confused about what this meams. Would love to discuss! 