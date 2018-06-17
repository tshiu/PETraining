import web

#normally you get a list of URLs (/) and the classes (index) that they match
#currently, we only have '/' and 'index' and this means that whenever someone
#goes to / witn a browser, lpthw.web will find the class index to load the request
urls = (
	'/', 'index'
)

app = web.application(urls,globals())

#render is a function where the render sees that you're asking for an index,
#goes into the emplates directory, looks for a page named index.html
#and then converts it
render = web.template.render('templates/')

class index(object):
	def GET(self):
		greeting = "Hello World!"
		return render.index(greeting = greeting)

if __name__ == "__main__":
	app.run()

#What's going on
#1. Browser makes a network connection to own computer that is called localhoust
#2. Once it connects, it makes an HTTP request to the bin/ex50.py application
#and asks for the / URL, which is the first URL on a website
