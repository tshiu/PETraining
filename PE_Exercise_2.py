#Write a script that calculates, for a given district-app connection, 
#how many shared students are associated with multiple schools.

from sys import argv

script, district_id = argv

#print the prompt so that we can verify that the ID is valid 
print district_id 

count = 0

#defining the response; setting a variable?
response = nil

#this is the path/endpoint that will be attached onto the URL to access 
#the students endpoint; this is the initial endpoint that is used
path = /v2.0/students

def get_tokens(district_id):

	#will need to retrieve the tokens for all of the districts as 
	#this is based on each district-app connection
	
	district = district_id 
	
	Construct Authorization header using client_id and client_secret 

   	GET tokens at https://clever.com/oauth/tokens?owner_type=district
    
    	return token

def multi_school_students(district_id):
	
	Use token to hit path 

	Return JSON object 

	Parse through JSON object
	

	#paging through each student in the response body
	For each student in response.data

	If student.schools.len > 1, 
	#looking if the student is associated with more than 1 school, I am looking to add 1 to the count
		count = count + 1 

		print count 
	
def page_through():
		
	#checking to see if the paging link is present
	if response.links[1].uri is present 

	#replacing path with the paging link that is prsent 	
	path = response.links[1].uri 

	#directing user to go back to adding to the total user count with the next path if link
	#is present
	multi_school_student(district_id)

	else print count 

page_through()  
			

#should print the final count
print count 
