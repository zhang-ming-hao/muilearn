#!/usr/bin/env python
# coding:utf-8

"""
"""

from sessionRH5 import SessionRH


class Home(SessionRH):
    """首页"""

    def get(self):
        self.render("index.html")


class Mui(SessionRH):
    """控件首页"""

    def get(self):
        self.render("ctrl_index.html")


class Api(SessionRH):
    """API首页"""

    def get(self):
        self.render("api_index.html")


class Login(SessionRH):
    """API首页"""

    def get(self):
        self.render("login.html")

