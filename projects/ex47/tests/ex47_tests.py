from nose.tools import *
from ex47.game import Room 

#creating a function named test_room
def test_room():
	#creating a instance of Room entitled gold that takes in the parameters name "GoldRoom"
	#and description the string below
	gold = Room("GoldRoom",
				"""This room has gold in it you can grab. There's a
				door to the north.""")
	#the assert function tests if the parameters are true, it not, then it will throw
	#up an error
	#asserting that the name of the Class gold is 'GoldRoom'
	assert_equal(gold.name, "GoldRoom")
	#asserting that the class Gold has an empty dictionary set as paths
	assert_equal(gold.paths, {})

#creating a function named test_room_paths
def test_room_paths():
	#creating an instance of class Room entitled center that has the name Center and the
	#description is the following string 'Test room in the center'
	center = Room("Center", "Test room in the center.")
	#creating an instance of class Room entitled north that has the name North and the 
	#description is 'Test room in the center'
	north = Room("North", "Test room in the north.")
	#creating an instance of the class Room entitled south that has the name 'South' and the
	#description is 'Test room in the south'
	south = Room("South", "Test room in the south.")

	#call the module/function add_paths from the Room class 
	#on center and adding the dictionary below
	center.add_paths({'north': north, 'south': south})

	#asserting that the when the function/module 'go' is called with the parameter north
	#in the Class center, what is returned is north
	#if not then this test will throw up and error
	assert_equal(center.go('north'), north)
	#asserting that when the function/moduel 'go' is called with the parameter south in the
	#Class center, then what is returned is south
	assert_equal(center.go('south'), south)

#creating a function/module named test_map
def test_map():
	#creating an instance of class Room start that has the name 'Start' and the description is
	#'You can go west and down a hole'
	start = Room("Start", "You can go west and down a hole.")
	#creating an instance of class Room west that has the name 'West' and the description is
	#'There are trees here, you can go east.'
	west = Room("Trees", "There are trees here, you can go east.")
	#creating an instance of class Room down that has the name 'Dungeon' and the description 
	#is 'It's dark down here, you can go up.''
	down = Room("Dungeon", "It's dark down here, you can go up.")

	#calling the function add_paths on the class start with the dictionary
	start.add_paths({'west': west, 'down': down})
	west.add_paths({'east': start})
	down.add_paths({'up':start})

	assert_equal(start.go('west'), west)
	assert_equal(start.go('west').go('east'), start)
	assert_equal(start.go('down').go('up'), start)