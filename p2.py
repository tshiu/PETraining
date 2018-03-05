Write a script that calculates, for a given district-app connection, how many shared students are associated with multiple schools.

var {district_id} = prompt("What is the district_id?");

GET token at https://clever.com/oauth/tokens?owner_type=district&district={district_id}'

count = 0

response = nil

path = /v2.0/students

do {
	response = GET https://api.clever.com+path

	For each student in response.data

		If student.schools.length > 1, 
			then count++ 

	path = response.links[1].uri 

} while (path is present);


console.log(count) 
