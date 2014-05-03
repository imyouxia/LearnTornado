import tornado.web
import tornado.ioloop

'''

get_cookie()，set_cookie()可以读取和设置cookie值。但是不安全，所以使用get_secure_cookie()和set_secure_cookie()并且使用一个密钥，名字为cookie_secret。

'''
class MainHandler(tornado.web.RequestHandler):
	def get(self):
		if not self.get_secure_cookie("cookievalue"):
			self.set_secure_cookie("cookievalue","myvalue")
			self.write("Your cookie was not set yet!")
		else:
			self.write("Your cookie was set!")

application = tornado.web.Application([
	(r"/",MainHandler),
	],cookie_secret="Thisisatestcookie")


if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()

