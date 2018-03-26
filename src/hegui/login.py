#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from hegui.mainscreen import MainPanel

from hecore.model.model import User

class Login(BoxLayout):

    def get_running_app(self):
        return App.get_running_app()

    def do_login(self, loginText, passwordText, dbPath):
        app = self.get_running_app()
        app.db.create_and_connect(self.ids['dbpath'].text, loginText, passwordText)

    def reset_form(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""

    def make_db_and_finish_login(self, loginText, passwordText, create=False, fileName=''):
        '''
        LLama al login de la aplicacion. Puede llamarse desde el inicio del login
        o desde el evento del popup para crear la base de datos
        (en cuyo caso tambien crea la db).
        :param app: la aplicación kyvy que estoy ejecutando
        :param loginText: texto ingresado en login
        :param passwordText: password ingresada en login
        :param create: crear o no la base de datos
        :param fileName: nombre con ruta completa de la base de datos
        :return: None
        '''
        app = self.get_running_app()
        if create:
            app.db.create_and_connect_callback(fileName)
        self.finish_login(loginText, passwordText)

    def finish_login(self, loginText, passwordText):
        '''
        Si la autenticación es correcta finaliza el login
        y cambia a la pantalla principal, levantando la api
        de sincro si la app se corrio como server.
        :param app: la aplicación kyvy que estoy ejecutando
        :param loginText: texto ingresado en login
        :param passwordText: password ingresada en login
        :return: None
        '''
        app = self.get_running_app()
        verif = User().verify_login(loginText, passwordText)
        if verif:
            app.username = loginText

            if app.runserver:
                from twisted.internet import reactor
                from hesync.hesync import EchoServerFactory
                reactor.listenTCP(8000, EchoServerFactory(self))

            app._switch_main_page('MainPanel', MainPanel)
        print (verif)
