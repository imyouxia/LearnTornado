tornado-exercise
================

学习Tornado Web 框架，按照教程写的一些示例。

下载和安装：

下载地址：https://pypi.python.org/pypi/tornado

安装：

tar xzvf tornado-3.2.tar.gz
cd tornado-3.2
python setup.py build
sudo python setup.py install

模块索引：
最重要的一个模块是web， 它就是包含了 Tornado 的大部分主要功能的 Web 框架。其它的模块都是工具性质的， 以便让 web 模块更加有用。

主要模块
web - 包含了 Tornado 的大多数重要的功能
escape - XHTML, JSON, URL 的编码/解码方法
database - 对 MySQLdb 的简单封装，使其更容易使用
template - 基于 Python 的 web 模板系统
httpclient - 非阻塞式 HTTP 客户端，它被设计用来和 web 及 httpserver 协同工作
auth - 第三方认证的实现（包括 Google OpenID/OAuth、Facebook Platform、Yahoo BBAuth、FriendFeed OpenID/OAuth、Twitter OAuth）
locale - 针对本地化和翻译的支持
options - 命令行和配置文件解析工具，针对服务器环境做了优化

底层模块
httpserver - 服务于 web 模块的一个非常简单的 HTTP 服务器的实现
iostream - 对非阻塞式的 socket 的简单封装，以方便常用读写操作
ioloop - 核心的 I/O 循环

