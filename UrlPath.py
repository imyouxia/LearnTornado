#coding=utf-8
import tornado.web
import tornado.ioloop

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('<html><body><form action= "/" method = "post">'
				   '<input type="text" name="message">'
				   '<input type="submit" value="submit">'
				   '</form></body></html>'
				   )
	def post(self):
		message = self.get_argument("message",None)
		print message
		self.write('<html><body>我把get的数据post下来了！</body></html>')

class UserHandler(tornado.web.RequestHandler):
	def get(self,name):
		print name
		self.write('your name is ' + name)
	
class UserAboutHandler(tornado.web.RequestHandler):
	def get(self,name):
		print name
		self.write('your name is ' + name + 'this is your about info!')

class ErrorHandler(tornado.web.RequestHandler):
	def get(self,para):
		self.write('404 not found!')

application = tornado.web.Application([
	(r"/",MainHandler),
	(r"/user/(\w+)",UserHandler),
	(r"/user/([0-9]+)/about",UserAboutHandler),
	(r"/user/(.*)",ErrorHandler),
	])

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()

