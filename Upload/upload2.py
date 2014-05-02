#coding=utf-8
import tornado.web
import tempfile
import Image
import time
import logging

'''
request.files中会记录下你上传的信息，格式为：
{"mypicture":[{'filename':'','content':'','body':''}]}

'''

class UploadHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("upload-file.html")

	def post(self):
		if self.request.files == {} or 'mypicture' not in self.request.files:
			""" 看是否有文件且name为picture，跟HTML代码对应 """
			self.write('<script>alert("请选择图片")</script>')
			return 

		# 有文件，判断是否为我们需要的格式
		# 常用的图片格式有：image/jpeg,image/bmp,image/pjpeg,image/gif,image/x-png,image/png
		image_type_list = ['image/gif','image/jpeg','image/pjpeg','image/bmp','image/png','image/x-png']
		send_file = self.request.files['mypicture'][0]
		if send_file['content_type'] not in image_type_list:
			self.write('<script>alert("仅支持jpg,jpeg,bmp,gif,png格式的图片！")</script>')
			return

		# 上述判断含有很大的上传漏洞，可以通过PIL来避免这些
		# 限制上传文件的大小，通过len获取字节数
		if len(send_file['body']) > 4 * 1024 * 1024:
			self.write('<script>alert("请上传4M以下的图片");</script>')
			return

		# 满足要求后，将图片存储
		# 存储也就是将send_file['body']内容进行存储，type(send_file['body'])为str
		# 先将文件写入临时文件，然后再用PIL对这个临时文件进行处理。
		tmp_file = tempfile.NamedTemporaryFile(delete=True) #创建临时文件，当文件关闭时自动删除
		tmp_file.write(send_file['body']) # 写入临时文件
		tmp_file.seek(0) # 将文件指针指向文件头部，因为上面的操作将指针指向了尾部

		# 此时用PIL再处理进行存储，PIL打开不是图片的文件会出现IOERROR错误，这就可以识别后缀虽然是图片格式，但内容并非是图片。
		try:
			image_one = Image.open(tmp_file.name)
		except IOError,error:
			logging.info(error) # 进行日志记录，因为这些操作大多数是破坏者的做法。
			logging.info('+'*30+'\n')
			logging.info(self.request.headers)
			tmp_file.close()
			self.write('<script>alert("图片不合法")</script>')
			return 

		# 判断图片尺寸，不再尺寸内拒绝操作
		if image_one.size[0] < 250 or image_one.size[1] < 250 or \
				image_one.size[0] > 2000 or image_one.size[1] > 2000:
					tmp_file.close()
					self.write('<script>alert("图片长宽在250px~2500px之间！")</script>')
					return 
		# 进行存储
		# 指定存储目录，产生新的文件名
		# 获取文件格式，用PIL获得的format不一定正确，所以用原文件名获得
		
		image_path = "./picture/" #存储地址
		image_format = send_file['filename']
		#image_format = send_file['filename'].split('.').pop().lower()
		tmp_name = image_path + str(int(time.time())) + image_format
		image_one.save(tmp_name)
		
		# 关闭临时文件，关闭后临时文件自动删除
		tmp_file.close()
		self.write('<script>alert("文件上传成功！")</script>')
		return 

application = tornado.web.Application([
	(r"/",UploadHandler),
	])

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()


	
		
