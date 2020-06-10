#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os, sys
import multiprocessing
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import parse_command_line

from configparser import ConfigParser
from collections import OrderedDict

from handlers import *

PROJECT_PATH = os.path.dirname(__file__)
CONFIG_FILE = os.path.join(PROJECT_PATH, 'config.ini')


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/",          Home),              # 主页
            (r"/mui",       Mui),               # 演示UI组件
            (r"/plus",      Api),               # 演示与原生API交互
            (r"/login",     Login),             # 演示登录功能
        ]

        settings = dict(
            template_path=os.path.join(PROJECT_PATH, 'templates'),  # 模板地址
            static_path=os.path.join(PROJECT_PATH, 'static'),  # 静态文件地址
            cookie_secret='98saf38s0-je3290sc8s-3ds83eios',  # cookie加密因子，可以任意修改
            session_expiry='1',  # session有效期（天）
            session_path='/session',  # session后端路径
            login_url='/login',  # 默认的登录地址
            debug=1,  # 调试开关
        )
        
        tornado.web.Application.__init__(self, handlers, **settings)


def main(port):
    parse_command_line()

    http_server = tornado.httpserver.HTTPServer(Application(), xheaders=True,  max_buffer_size=504857600)
    http_server.listen(port)
    print('Web server is started on port %d.' % port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        main(80)
    else:
        try:
            ports = [int(port) for port in sys.argv[1].split(',')]
        except:
            try:
                a, b = sys.argv[1].split('-')
                ports = range(int(a), int(b)+1)
            except:
                ports = list()
                print ('Parameter error.')

        for port in ports:
            p = multiprocessing.Process(target=main, args=(port,))
            p.start()
