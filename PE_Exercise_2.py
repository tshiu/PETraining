#Write a script that calculates, for a given district-app connection, 
#how many shared students are associated with multiple schools.

print "What is the district_id?"
district_id = raw_input()

#print the prompt so that we can 
#verify that the ID is valid; perhaps we can write in a check here against another call 
print district_id 

#I want to retrieve the district specific token at this endpoint
GET token at https://clever.com/oauth/tokens?owner_type=district&district={district_id}'

#starting the count at 0 and defining count
count = 0

#defining the response; setting a variable?
response = nil

#this is the path/endpoint that will be attached onto the URL to access the students endpoint; 
#this is the initial endpoint that is used
path = /v2.0/students

#setting a loop-like function so that we can repeat the steps below until 
do {
	#looking to retrieve the response from the students endpoint which will return a JSON response
	response = GET https://api.clever.com+path

	#paging through each student in the response body
	For each student in response.data

		If student.schools.length > 1, 
			#looking if the student is associated with more than 1 school, I am looking to add 1 to the count
			then count++ 

			#check to see if count is a real number, or if we have an actual response
			print count 
	#will need to modify this path as the URI is respnonse.link[2].uri after the initial response		
	path = response.links[1].uri 
	
	#print path after the retrieval to confirm the uri is correct
	print path 

#if the response has the path present, then we will want to take the URI, 
#attached this to the endpoint and make another call, once it is not present, we want to stop this loop
} while (path is present);

#should print the final count

print count
