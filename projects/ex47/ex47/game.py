#creating a class Room that is a object
class Room(object):
	#creating an init that takes in the parameter self, name, and description
	def __init__(self, name, description):
		#in class Room, name = name
		self.name = name
		#in class Room, description = description
		self.description = description
		#in class Room, paths is an empty dictionary
		self.paths = {}
	#creating a function called go within the class room that takes in parameters self and direction
	def go(self, direction):
		#the get function returns the value for a key that is given
		#setting the value to None as the default
		return self.paths.get(direction, None)
	#creating a function called add_paths that takes in the values self and paths 
	def add_paths(self, paths):
		#the update function updates the value of a key pair if the key is the same or adds a new
		#key value pair
		self.paths.update(paths)
