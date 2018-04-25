#Write a function that takes in two lists, sorts each list, then merges two sorted lists into a new sorted list.

#TS I combined the lists first because then the master list would be sorted. Otherwise, we would have to sort again
#after combining the lists to produce a sorted list? 


#combine the lists in a way that they are sorted so you don't have to sort it again 
def sort_lists(list1, list2):

	print sorted(list1 + list2)

list_1 = [1, 3, 100, 5, 7, 9]
list_2 = [2, 4, 6, 8, 200, 10]

sort_lists(list_1,list_2)