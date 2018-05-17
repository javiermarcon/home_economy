# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.treeview import TreeViewLabel
from kivy.uix.recycleview import RecycleView

from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.clock import Clock

import time, threading

class MainPanel(BoxLayout):

    def __init__(self, **kwargs):
        super(MainPanel, self).__init__(**kwargs)
        #self.execute_initial_tasks()
        mc = self.main_cuentas
        self.populate_treeview(mc)
        mc.bind(minimum_height=mc.setter('height'))
        # Open the pop up
        self.show_popup()

        # Call some method that may take a while to run.
        # I'm using a thread to simulate this
        mythread = threading.Thread(target=self.execute_initial_tasks)
        mythread.start()

    def show_popup(self):
        self.pop_up = Factory.PopupBox()
        self.pop_up.update_pop_up_text('Running some task...')
        self.pop_up.open()

    def execute_initial_tasks(self):
        print("Ejecutando tareas iniciales")
        app = App.get_running_app()
        options = { "mail_plugins": {
            "email": app.config.get('mail_parser', 'email'),
            "password": app.config.get('mail_parser', 'password')
            }}
        if app.runserver:
            app.backend.launch_server()
        app.backend.run_plugins(options)
        print("Listo")
        self.pop_up.dismiss()

    def populate_treeview(self, tv):
        n = tv.add_node(TreeViewLabel(text='Item 1'))
        for x in xrange(30):
            tv.add_node(TreeViewLabel(text='Subitem %d' % x), n)
        n = tv.add_node(TreeViewLabel(text='Item 2', is_open=True))
        for x in xrange(30):
            tv.add_node(TreeViewLabel(text='Subitem %d' % x), n)
        n = tv.add_node(TreeViewLabel(text='Item 3'))
        for x in xrange(30):
            tv.add_node(TreeViewLabel(text='Subitem %d' % x), n)
        return tv

class RV(RecycleView):
    """ver: https://kivy.org/docs/api-kivy.uix.recycleview.html#kivy.uix.recycleview.RecycleView"""
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': 'Mensaje {}'.format(x)} for x in range(4)]

class PopupBox(Popup):
    pop_up_text = ObjectProperty()
    def update_pop_up_text(self, p_message):
        self.pop_up_text.text = p_message