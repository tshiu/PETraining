#Write a function that takes in two lists, sorts each list, then merges two sorted lists into a new sorted list.


#combine the lists in a way that they are sorted so you don't have to sort it again 
#I wasn't sure how to complete the above? Not quite sure how to combine and sort without actually
#just sorting.

def sort_lists(list1, list2):

	print sorted(list1 + list2)

list_1 = [1, 3, 100, 5, 7, 9]
list_2 = [2, 4, 6, 8, 200, 10]

sort_lists(list_1,list_2)
