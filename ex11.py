print "How old are you?",
age = raw_input()
print "How tall are you?", 
height = raw_input() 
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)

# Study Drills
# 1. raw_input is a prompt to the user; best to avoid input() 
# 2. 

#Stack Overflow example with int(raw_input()) and enters
#print '\nWhat\'s your name ?',
#name = raw_input('--> ')
#print '\nHow old are you, %s?' % name,
#age = int(raw_input())
#print '\nHow tall are you (in inches), %s?' % name,
#height = int(raw_input())
#print '\nHow much do you weigh (in kgs), %s?' % name,
#weight = int(raw_input())

#print '\nSo, %s is %d years old, %d inches tall and weighs %d kgs.\n' %(
#name, age, height, weight)

# 3. 
birthdate = raw_input("What is your birthday?") 
print "I hope %s is a great day for you!" % birthdate  

# 4. Python uses the quotes to indicate a demarcation. It is escaping the single quote so that the line will print. 
