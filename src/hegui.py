#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

import os

from login import Login
from mainscreen import MainScreen

class HeGuiApp(App):
    #kv_directory = os.path.join(__file__, 'kv')
    username = StringProperty('')
    password = StringProperty('')

    def build(self):

        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        manager.add_widget(MainScreen(name='mainscreen'))

        return manager

    def get_application_config(self):
        if(not self.username):
            return super(HeGuiApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(HeGuiApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory)
        )

if __name__ == '__main__':
    HeGuiApp().run()