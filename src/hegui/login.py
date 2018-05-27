#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import partial

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from hegui.mainscreen import MainPanel
from hecore.model.model import User

class Login(BoxLayout):

    def get_running_app(self):
        return App.get_running_app()

    def do_login(self, loginText, passwordText, fileName):
        app = self.get_running_app()
        #fileName = self.ids['dbpath'].text
        if app.backend.check_file_exists(fileName):
            self.finish_login(loginText, passwordText)
        else:
            strmsg = "La base de datos {} no existe, desea crearla?".format(fileName)
            login_finish = self.make_db_and_finish_login
            app.popups.open_confirm_popup(strmsg, action_yes=partial(login_finish, loginText,
                                          passwordText, True, fileName),
                                          action_no=self.no_action)

    def no_action(self):
        pass

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
        if not create:
            self.finish_login(loginText, passwordText)
        else:
            # TODO: verificar opciones x defecto y crearlas
            app.backend.db.create_and_connect_callback(fileName)
            self.save_dbpath(fileName, app)
            self.switch_main(loginText, app)

    def finish_login(self, loginText, passwordText):
        '''
        Si la autenticación es correcta finaliza el login
        y cambia a la pantalla principal, levantando la api
        de sincro si la app se corrio como server.
        Si la autenticacion no es correcta, te lleva de nuevo
        a la pantalla de login
        :param loginText: texto ingresado en login
        :param passwordText: password ingresada en login
        :return: None
        '''
        app = self.get_running_app()
        verif = User().verify_login(loginText, passwordText)
        #print (verif)
        if verif:
            self.switch_main(loginText, app)
            return
        #print("Login Failed")
        self.ids['loginErrors'].text = "El usuario y/o contraseña no son correctos para la base de datos elegida."
        app._switch_main_page('Login', self)
        return

    def switch_main(self, loginText, app):
        app.username = loginText
        # print("Login Ok")
        self.ids['loginErrors'].text = ""
        app._switch_main_page('MainPanel', MainPanel)

    def save_dbpath(self, dbPath, app):
        app.config.set('last_session', 'dbpath', dbPath)
        app.config.write()