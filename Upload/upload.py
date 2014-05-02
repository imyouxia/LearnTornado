import tornado.ioloop
import tornado.web

class UploadFileHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("upload-file.html")
	
	def post(self):
		file_dict_list = self.request.files['mypicture']
		for file_dict in file_dict_list:
			filename = file_dict["filename"]
			f = open("/home/linuxer/github/tornado-exercise/picture/%s" % filename,"wb")
			f.write(file_dict["body"])
			f.close()
		self.write("finish")

application = tornado.web.Application([
	(r"/",UploadFileHandler),
	])

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()

