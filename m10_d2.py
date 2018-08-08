#Write a function that takes in two lists, sorts each list, then merges two sorted lists into a new sorted list.

#TS I combined the lists first because then the master list would be sorted. Otherwise, we would have to sort again
#after combining the lists to produce a sorted list? 


#combine the lists in a way that they are sorted so you don't have to sort it again 
def sort_lists(list1, list2):

	slist1 = sorted(list1)
	slist2 = sorted(list2)

	while slist1 and slist2:
		
		if  slist1[0] < slist2[0]:
			merged_list.append(slist1.pop(0))
		else:
			merged_list.append(slist2.pop(0))

	print merged_list

merged_list = []
list_1 = [1, 3, 100, 5, 7, 9]
list_2 = [2, 4, 6, 8, 200, 10]

sort_lists(list_1,list_2)
