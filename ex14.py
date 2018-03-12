from sys import argv

script, user_name, time_played = argv 
#setting prompt as a variable, so we do not have to
#retype the carrot each time
prompt = '> '

#will insert display the input from the arg
print "Hi %s, I'm the %s script. I hear its your %s time playing" % (user_name, script, time_played)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

#using raw representation instead of display
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)