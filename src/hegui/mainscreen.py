# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.treeview import TreeViewLabel
from kivy.uix.recycleview import RecycleView
#from kivy.clock import Clock
from cuentas import TreeCuentas

import time, threading

class MainPanel(TreeCuentas):

    def __init__(self, **kwargs):
        super(MainPanel, self).__init__(**kwargs)
        #self.execute_initial_tasks()
        mc = self.main_cuentas
        self.populate_treeview(mc)
        mc.bind(minimum_height=mc.setter('height'))
        # Open the pop up
        app = App.get_running_app()
        app.popups.show_popup('Running some tasks...')

        # Call some method that may take a while to run.
        # I'm using a thread to simulate this
        mythread = threading.Thread(target=self.execute_initial_tasks)
        mythread.start()

    def execute_initial_tasks(self):
        print("Ejecutando tareas iniciales")
        app = App.get_running_app()
        options = { "mail_plugins": {
            "email": app.config.get('mail_parser', 'email'),
            "password": app.config.get('mail_parser', 'password')
            }}
        if app.runserver:
            app.backend.launch_server()
        #app.backend.run_plugins(options)
        #trigger = Clock.create_trigger(my_callback)
        ## later
        #trigger()
        print("Listo")
        app.popups.close_popup()

class RV(RecycleView):
    """ver: https://kivy.org/docs/api-kivy.uix.recycleview.html#kivy.uix.recycleview.RecycleView"""
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': 'Mensaje {}'.format(x)} for x in range(4)]
