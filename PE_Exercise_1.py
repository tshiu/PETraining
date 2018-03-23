#Prompt: Write a script that calculates, for a given application, how many total teachers are shared across all of its districts.

#Would like to get input as to what record we are looking to query, will probably change this to argv module
record_type = raw_input("Which record type to query? (district_admins, teachers, students, sections, school_admins)")

#printing this input as a debugging so that we can see if the user typed in the right format
print record_type 

#adding this step so user can confirm if the record_type is correct and then move forward 
print """
You would like to retrieve the total number of %s in the district. 
Is this correct? Press enter to proceed or CTRL-C to escape.
""" % record_type

raw_input()

#setting count at 0 to start
count = 0

#setting response as nil now so that it can be called within the loop-like function
response = nil 

#setting path as the endpoint to put record_type from prompt into the endpoint
path = /v2.0/{record_type}

#will set client ID
client_ID = [Client_ID_for_district]
#will set client secret 
client_secret = [Client_Secret_for_district]

def get_tokens():

	#will need to retrieve the tokens for all of the districts as 
	#this is based on each district-app connection
	owner_type = district 
	
	Construct Authorization header using client_id and client_secret 

    GET tokens at https://clever.com/oauth/tokens?owner_type=district
    
    return list_of_tokens

get_tokens()

for token in list_of_tokens:

def total_users(record_type):

	
	#using token to ping the API to retrieve the JSON response
	response = GET https://api.clever.com+path
	
	#counting the length of the json response objects, assuming that if there are 4 teachers shared, 
	#there will be four responses so just counting those data blobs
	count = count + response.data.len
	
	#would like to see how this final number is 
	#tallied to avoid looping through the data indefinitely
	print count 

total_users(record_type)

#will need to 
def page_through():
#checking to see if the paging link is present
	if response.links[1].uri is present 

	#replacing path with the paging link that is prsent 	
		path = response.links[1].uri 

	#directing user to go back to adding to the total user count with the next path if link
	#is present
		total_users()
			
	else:

		move on to the next token in the list 

page_through()

