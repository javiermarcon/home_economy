# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView

class MainPanel(BoxLayout):
    def disconnect(self):
        app = App.get_running_app()
        app.do_logout()

class RV(RecycleView):
    """ver: https://kivy.org/docs/api-kivy.uix.recycleview.html#kivy.uix.recycleview.RecycleView"""
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(100)]
