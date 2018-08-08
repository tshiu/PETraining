#Write a program that asks the user to enter in numbers separated by spaces. 
#Your program should print the numbers sorted largest -> smallest

print "Please enter in list of numbers separated by spaces."
string_list = str(raw_input("> "))

list = string_list.split(' ')

print sorted(list, reverse=True)


