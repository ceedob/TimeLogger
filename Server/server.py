print "starting"


import tornado, tornado.web
import os
import database

class LoginHandler(tornado.web.RequestHandler):
	def head(self):
		pass
		# Get a session cookie		
		

class APIHandler(tornado.web.RequestHandler):
	def head(self):
		pass
		# used to get metadata about events
		
	def get(self):
		pass
		self.set_header("Content-Type", "text/plain")
		user = 1
		for i in database.events:
			if database.events[i]["USER"] == user:
				self.write(str(i).zfill(6) + " - "+ str(database.events[i]["TIMESTAMP"]) + " " + str(database.events[i]["CLASS"])+ " "  + str( database.events[i]["SUBCLASS"])+ " "  + str(database.events[i]["DATA"] ) + "\n")
		# used to get a list of previous events
		
	def post(self):
		pass
		# used to submit an event now 
		
	def put(self):
		pass
		# used to update existing events
			
	def delete(self):
		pass
		# remove an event
		
	def options(self):
		pass
		# edit options?
		
application = tornado.web.Application([
    (r"/login", LoginHandler),
    (r"/", APIHandler),
])

port = int(os.environ.get('PORT', 5000))
print "Starting on port",port
application.listen(port)
tornado.ioloop.IOLoop.instance().start()