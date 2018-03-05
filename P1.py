
Write a script that calculates, for a given application, how many total teachers are shared across all of its districts.

var {record_type} = prompt("What record type would you like to query?")

GET tokens at https://clever.com/oauth/tokens?owner_type=district

count = 0

response = nil 

path = /v2.0/{record_type}

For each token

do {
	response = GET https://api.clever.com+path

	count = count + response.data.length

	path = response.links[1].uri 

} while (path is present);


console.log(count)


