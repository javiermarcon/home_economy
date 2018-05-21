#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from model.model import *
from plugin_logic import plugin_logic

class HecoreBackend:
    """
    Esta clase se encarga de hacer todas las operaciones que pide la gui
    coordinado las acciones de todos los módulos.
    """

    db = DB_CONN
    config = None
    plugins = None

    def launch_server(self):
        """
        Lanza el servidor twisted para escuchar pedidos de syncro
        :return: None
        """
        from twisted.internet import reactor
        from hesync.hesync import EchoServerFactory
        reactor.listenTCP(8000, EchoServerFactory(self))
        return

    def check_file_exists(self, filePath):
        return os.path.isfile(filePath)

    def set_ini_location(self, location):
        self.ini_location = location

    def run_plugins(self, options):
        pluginrun = plugin_logic(options)
        ret = pluginrun.run_plugins()
        if ret:
            for plugin_iter in ret:
                for p in plugin_iter:
                    print "zzz ", p


