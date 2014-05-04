'''
$ siege http://localhost:8000/?q=pants -c10 -t10s
使用python的yield关键字以及tornado.gen.Task对象的一个实例，将我们想要的调用和传给该调用函数的参数传递给那个函数。
这里，yield的使用返回程序对Tornado的控制，允许在HTTP请求进行中执行其他任务，当HTTP请求完成时，RequestHandler方法在其停止的地方恢复，即所有请求相关的逻辑位于同一个位置，而HTTP请求依然是异步执行的。

'''
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen

import urllib
import json
import datetime
import time

from tornado.options import define,options
define("port",default=8000,help="run on the given port",type=int)

class IndexHandler(tornado.web.RequestHandler):
	@tornado.web.asynchronous
	@tornado.gen.engine
	def get(self):
		query = self.get_argument('q')
		client = tornado.httpclient.HTTPClient()
		response = yield tornado.gen.Task(client.fetch,
				"http://serach.twitter.com/search.json?" + \
						urllib.urlencode({"q":query,"result_type":"recent","rpp":100}))
		body = json.loads(response.body)
		result_count = len(body['results'])
		now = datetime.datetime.utcnow()
		raw_oldest_tweet_at = body['result'][-1]['created_at']
		oldest_tweet_at = datetime.datetime.strptime(raw_oldest_tweet_at,"%a,%d %b %Y %H:%M:%S +0000")
		seconds_diff = time.mktime(now.timetuple()) - \
				time.mktime(oldest_tweet_at.timetuple())
		tweets_per_second = float(result_count) / seconds_diff
		self.write("""
		<div style="text-aligin:center">
		<div style="font-size:72px">%s</div>
		<div style="font-size:144px">%.02f</div>
		<div style="font-size:24px">tweets per second</div>
		</div>""" %(query,tweets_per_second))

		self.finish()

if __name__ == "__main__":
	tornado.options.parse_command_line()
	app = tornado.web.Application(handlers=[(r"/",IndexHandler)])
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()


