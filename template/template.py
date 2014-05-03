#coding=utf-8
import tornado.web
import tornado.ioloop

#template_path=os.path.join(os.path.dirname(file),"templates")

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		items = ["Item 1","Item 2","Item 3"]
		self.render("template.html",title="My title",items=items)


application = tornado.web.Application([
	(r"/",MainHandler),])

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
