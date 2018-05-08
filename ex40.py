#Make a class named Song that is-a object
#Object is the most basic kind of thing and any instance of some thing
class Song(object):
	#class song has-a __init___ that takes self and lyrics parameter 
	#inside the functions of a class (in this case, Song) self is a variable for the 
	#instance/object being acessed 
    def __init__(self, lyrics):
    	#from self get lyrics and set it to lyrics
    	self.lyrics = lyrics 

    #class Song has-a function named sing_me_a_song that takes parameter self
    def sing_me_a_song(self):
    	#for each line in the lyrics in self, print the line
    	for line in self.lyrics:
    		print line
#setting happy_bday to an instance of Song(the class), with the 
#the lyrics in the parameter
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])
#setting bulls_on_parade to an instance of Song(the class), with
#lyrics in the parameter
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])
#from happy_bday, call the function sing_me_a_song 
happy_bday.sing_me_a_song()
#from bulls_on_parade (the instance of song), call the sing_me_a_song function
bulls_on_parade.sing_me_a_song()

#SD
#1. 
#setting KOD to an instance of Song, with the lyrics in the parameter
KOD = Song(["This here's what you call a flip",
			"Ten keys from a quarter brick"])
#setting Pynk to an instance of Song witht he lyrics in the parameter
Pynk = Song(["Pynk like the folds of your brain",
			 "Pynk as we all go insane"])
#from Pynk, call the function sing me a song
Pynk.sing_me_a_song()
#from KOD, call the function sing me a song
KOD.sing_me_a_song()

#2. 
#from KOD1 set the attribute lyrics to 
KOD1lyrics = ["These are test lyrics",
				"Testy lyrics"]

#set KOD1 to an instance of Song
KOD1 = Song(KOD1lyrics)

#from KOD1, call the function sing me a song
KOD1.sing_me_a_song()

#3. 

Newlyrics = "will this work?"

KOD1 = Song('%s') % Newlyrics

KOD1.sing_me_a_song() 

#4. Did some more reading here on init and self. Think I'm getting a better grasp. 




