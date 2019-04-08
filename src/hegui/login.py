#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import partial

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from hegui.mainscreen import MainPanel
from hecore.model.model import User

import os

from hecore.crypt_functions import encryptDecrypt
from hegui.settings_data import get_pw_path


class Login(BoxLayout):

    def run_autologin(self, placeholder=None):
        '''runs the automatic login'''
        app = self.get_running_app()
        if app.config.get('autologin', 'do_autologin'):
            username = app.config.get('autologin', 'username')
            encrypted_password = app.config.get('autologin', 'password')
            db_filename = app.config.get('last_session', 'dbpath')
            pwpath = get_pw_path()
            if not os.path.isfile(pwpath):
                self.ids['loginErrors'].text = "Please configure password path to use autologin"
                return
            if not app.backend.check_file_exists(db_filename):
                password = encryptDecrypt(pwpath).decrypt(encrypted_password)
                self.do_db_create_msg(app, db_filename, username, password)
            #enters as a user
            self.switch_main(username, app)

    def get_running_app(self):
        return App.get_running_app()

    def do_login(self, loginText, passwordText, fileName):
        app = self.get_running_app()
        #fileName = self.ids['dbpath'].text
        if app.backend.check_file_exists(fileName):
            self.finish_login(loginText, passwordText)
        else:
            self.do_db_create_msg(app, fileName, loginText, passwordText)

    def no_action(self):
        pass

    def do_db_create_msg(self, app, fileName, loginText, passwordText):
        strmsg = "La base de datos {} no existe, desea crearla?".format(fileName)
        login_finish = self.make_db_and_finish_login
        app.popups.open_confirm_popup(strmsg, action_yes=partial(login_finish, loginText,
                                                                 passwordText, True, fileName),
                                                                 action_no=self.no_action)

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
        #print(verif)
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