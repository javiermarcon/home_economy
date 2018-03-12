# -*- coding: utf-8 -*-

import os

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App

from hegui.mainscreen import MainPanel
from hegui.login import Login

#--------------------------------------------------------------------------
'''dictionary that contains the correspondance between items descriptions
and methods that actually implement the specific function and panels to be
shown instead of the first main_panel
'''
SidePanel_AppMenu = {'Login': ['Login', None],
                     'MainPanel': ['MainPanel', None],
                     'Inicio': ['menu_inicio', None],
                     'Base de datos': ['menu_basedatos', None],
                     'Sincronizar': ['menu_sincro', None],
                     'Cuentas': ['menu_cuentas', None],
                     'Monedas': ['menu_cuentas', None],
                     'Categorías': ['menu_cuentas', None],
                     'Usuarios': ['menu_cuentas', None],
                     'Presupuestos': ['menu_cuentas', None],
                     'Reportes': ['menu_cuentas', None],
                     'Opciones': ['menu_opciones', None],
                     'Ayuda General': ['menu_cuentas', None],
                     'Preguntas frecuentes': ['menu_cuentas', None],
                     'Acerca de...': ['menu_cuentas', None],
                     'Cerrar sesión': ['do_logout', None],
                     'Salir': ['do_quit', None],

                     }

#--------------------------------------------------------------------------

class MenuFunctions:

    def menu_inicio(self):
        print 'UNO... exec'
        self._switch_main_page('MainPanel', MainPanel)

    def menu_basedatos(self, dbPath=''):
        pag_bd = PaginaBd()
        conf_path = self.config.get('last_session', 'dbpath')
        if not dbPath == conf_path and dbPath.startswith('/'):
            conf_path = dbPath
        if not conf_path:
            conf_path = os.path.dirname(os.path.expanduser('~'))
        pag_bd.ids['lvl_bd'].text = conf_path
        pag_bd.ids['filechooser'].path = conf_path

        self._switch_main_page('Base de datos', pag_bd)

    def menu_cuentas(self):
        print 'DUE... exec'
        self._switch_main_page('Cuentas', PaginaCuentas)
    def menu_sincro(self):
        print 'TRE... exec'
        self._switch_main_page('Sincronizar',  PaginaSincro)
    def menu_opciones(self):
        print 'DUE... exec'
        self._switch_main_page('Opciones', PaginaOpciones)

class PaginaCuentas(FloatLayout):
    pass

class PaginaSincro(FloatLayout):
    pass

class PaginaOpciones(FloatLayout):
    pass

class PaginaBd(BoxLayout):
    """
    Esta es la ventana para abrir la base de datos a utilizar.
    """

    def open(self, path, filename):
        print filename
        filePath = os.path.join(path, filename[0])
        if self.check_fileDb(filePath):
            self.change_db_label(filePath)
            self.save_dbpath(filePath)
            with open(filePath) as f:
                print f.read()
        self.go_previous_panel()

    def selected(self, filename):
        self.change_db_label(filename)

    def cancel(self):
        self.go_previous_panel()

    def go_previous_panel(self):
        app = App.get_running_app()
        app.change_panel(app.last_panel)

    def check_fileDb(self, dbPath):
        # TODO: chequear que sea una base de datos sqlite
        return os.path.isfile(dbPath)

    def save_dbpath(self, dbPath):
        app = App.get_running_app()
        app.config.set('last_session', 'dbpath', dbPath)
        app.config.write()

    def change_db_label(self, filePath):
        Login().ids['dbpath'].text = filePath
        self.ids['lvl_bd'].text = filePath