#Write a script that calculates, for a given application, how many total teachers are shared across all of its districts.

#Get input as to what record we are looking to query
print "What record type would you like to query?"
record_type = raw_input()

#print the prompt so that we can verify that the record type 
#is valid (e.g. if they wrote in teacher ID instead of teahcer)
print record_type 

#will need to retrieve the tokens for all of the districts as this is based on each district-app connection
GET tokens at https://clever.com/oauth/tokens?owner_type=district

#setting count at 0 to start
count = 0

#setting response as nil now so that it can be called within the loop-like function
response = nil 

#setting path as the endpoint, looking to put record_type from prompt into the endpoint
path = /v2.0/record_type

#for each district-app connection
For each token

do {
	#using token to ping the API to retrieve the JSON response
	response = GET https://api.clever.com+path
	
	#counting the length of the json response objects, assuming 
	#that if there are 4 teachers shared, there will be four responses so just counting those data blobs
	count = count + response.data.length
	
	#looking to maybe print here to see what might be happening in case there is a mistake 
	#would like to see how this final number is tallied to avoid looping through the data indefinitely
	print count

	#taking the pagination link and appending that to the end of the URI in case there are more responses
	path = response.links[1].uri 

#would like to continue to count until there is no pagination link at the end
} while (path is present);

#print the final tally
print final count


