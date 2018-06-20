#Write a script that calculates, for a given district-app connection, 
#how many shared students are associated with multiple schools.

import requests
import base64
import json
import urllib

client_secret = "e5e704106c712eadf4f6:dc9c9e1c23fc29548886d58f61c0e8b89a7dbb97"
#current Leland Labs token

def get_tokens(): 

	global tokens

	tokens = []

	url = "https://clever.com/oauth/tokens"

	encoded_val = base64.b64encode(client_secret)

	headers = {'Authorization': 'Basic %s' % encoded_val}

	querystring = {'owner_type':'district'}

	json_object = requests.request("GET", url, headers=headers, params=querystring).json()

	for i in range(0, len(json_object)):

		tokens.append(json_object['data'][i]['access_token'])
	
	return tokens

get_tokens()

def map_district_tokens(): 

	global districts

	districts = []
	
	for token in tokens: 

		headers = {'Authorization': 'Bearer %s' % token}

		url = "https://api.clever.com/v2.0/districts"

		r = requests.request("GET", url, headers=headers).json()

		districts.append(r['data'][0]['data']['name'])

		print r['data'][0]['data']['name']

	global mapping 

	mapping = dict(zip(districts,tokens))

map_district_tokens()

def count_obj(): 

	pick = raw_input("Which above districts would like to elect? \n>")
	
	object = raw_input("What object would you like to sum? \n(districts, schools, school_admins, teachers, students, sections)\n>")
	
	token = mapping[pick]

	headers = {'Authorization': 'Bearer %s' % token}

	url = "https://api.clever.com/v2.0/%s" % object

	r = requests.request("GET", url, headers=headers).json()

	count = len(r['data'])

	while len(r['data']) > 1:

		last_id = r['data'][len(r['data'])-1]['data']['id'] 

		path = "/v2.0/%s?starting_after=%s" % (object, last_id)

		url = "https://api.clever.com"+path

		r = requests.request("GET", url, headers=headers).json()

		count += len(r['data'])

	print "%d %s are shared with your app" % (count, object)

count_obj()


