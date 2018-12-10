# -*- coding: utf-8 -*-

import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.filebrowser import FileBrowser

from hegui.login import Login

class PaginaBd(BoxLayout):
    """
    Esta es la ventana para abrir la base de datos a utilizar.
    """

    def open(self, path, filename):
        #print(filename)
        if len(filename) > 0:
            filePath = os.path.join(path, filename[0])
            self.change_db_label(filePath)
            self.save_dbpath(filePath)
        self.go_previous_panel()

    def selected(self, filename):
        self.change_db_label(filename)

    def cancel(self):
        self.go_previous_panel()

    def go_previous_panel(self):
        app = App.get_running_app()
        app.change_panel(app.last_panel)

    def save_dbpath(self, dbPath):
        app = App.get_running_app()
        app.config.set('last_session', 'dbpath', dbPath)
        app.config.write()

    def change_db_label(self, filePath):
        if isinstance(filePath, list):
            filePath = filePath[0]
        Login().ids['dbpath'].text = filePath
        self.ids['lvl_bd'].text = filePath