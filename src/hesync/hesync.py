#!/usr/bin/env python
# -*- coding: utf-8 -*-

# install_twisted_rector must be called before importing and using the reactor
from kivy.support import install_twisted_reactor

install_twisted_reactor()

from twisted.internet import reactor
from twisted.internet import protocol


class EchoServer(protocol.Protocol):
	def dataReceived(self, data):
		response = self.factory.app.handle_message(data)
		if response:
			self.transport.write(response)

class EchoServerFactory(protocol.Factory):
	protocol = EchoServer

	def __init__ (self, app):
		self.app = app


class HEsyncApp:
    pass


if __name__ == '__main__':
    HEsyncApp().run()