#Prompt: Write a script that calculates, for a given application, how many total 
#teachers are shared across all of its districts.

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
	
	print tokens 
	
	return tokens


def get_count():

	object = raw_input("What object would you like to sum? \n(districts, schools, school_admins, teachers, students, sections)\n>")

	count = 0

	path = '/v2.0/%s' % object

	for token in tokens: 

		headers = {'Authorization': 'Bearer %s' % token}

		url = "https://api.clever.com"+path

		r = requests.request("GET", url, headers=headers).json()

		count += len(r['data'])

		while len(r['data']) > 1:

			last_id = r['data'][len(r['data'])-1]['data']['id'] 

			path = "/v2.0/%s?starting_after=%s" % (object, last_id)

			url = "https://api.clever.com"+path

			r = requests.request("GET", url, headers=headers).json()

			count += len(r['data'])

	count += len(r['data'])

	print "Total shared %s is %d " % (object, count)


get_tokens()

get_count()