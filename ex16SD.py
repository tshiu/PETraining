from sys import argv 

script, filename = argv

print "We are just going to print the file: %s" % filename 

txt = open(filename)
print txt.read()