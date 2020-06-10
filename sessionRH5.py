# -*- coding: utf-8 -*-

#   RequestHandler的session版，支持Tornado6.0及更高版本
#
#   1. 以Cookie形式实现session字典
#   2. 重写了get_current_user()
#   3. 用装饰器引入db（引用application.db）
#
#   Update: 2020-01-13
#

import tornado.web

version = "5.0"
version_info = (5, 0, 0, 0)

import tornado.web
import json

class SessionRH(tornado.web.RequestHandler):
    def initialize(self):
        if 'Content-Type' in self.request.headers and 'application/json' in self.request.headers['Content-Type'] and len(self.request.body):
            try:
                arguments = json.loads(self.request.body)
                for key in arguments:
                    self.request.arguments[key] = [arguments[key]]
            except:
                pass
        
        self.session = self.current_user
        
    
    def set_session(self, **kwds):
        """设置session"""
        
        expiry = int(self.settings['session_expiry'])
        if not expiry:
            expiry = None
        
        self.set_secure_cookie('session', json.dumps(kwds), expires_days=expiry)
    
    def clear_session(self):
        """清除session"""
        
        self.clear_cookie('session')
    
    def get_current_user(self):
        user_cookie = self.get_secure_cookie('session')
        if user_cookie:
            return json.loads(user_cookie)
        return None

    @property
    def db(self):
        return self.application.db