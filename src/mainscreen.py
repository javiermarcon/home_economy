# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MainPanel(BoxLayout):
    def disconnect(self):
        app = App.get_running_app()
        app.do_logout()
