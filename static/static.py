#coding=utf-8
import os
import tornado.web
import tornado.ioloop

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('<html><body>Hello World!</body>'
			       '</html>')
		#self.write(os.path.join(os.path.dirname(__file__),"picture"))

settings = {
		"static_path":os.path.join(os.path.dirname(__file__),"picture"),
		"cookie_secret":"Thisisatestcookie",
		"login_url":"/login",
		"xsrf_cookies":True,
		}

application = tornado.web.Application([
	(r"/",MainHandler),
	#(r"/login",LoginHandler),
	(r"/(hello\.png)",tornado.web.StaticFileHandler,
		dict(path=settings['static_path'])),
	],**settings)


if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()

	
