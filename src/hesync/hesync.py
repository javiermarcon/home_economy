#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet import protocol
from kivy.app import App

class EchoServer(protocol.Protocol):
	def dataReceived(self, data):
		app = App.get_running_app()
		response = app.handle_message(data)
		if response:
			self.transport.write(response)

class EchoServerFactory(protocol.Factory):
	protocol = EchoServer

	def __init__ (self, app):
		self.app = app
