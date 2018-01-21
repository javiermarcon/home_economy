#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.properties import StringProperty

from hegui.navigationdrawer import NavigationDrawer
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.actionbar import ActionBar, ActionButton, ActionPrevious

import os

from hegui.login import Login
from hegui.menufunctions import MenuFunctions, SidePanel_AppMenu

RootApp = None
id_AppMenu_METHOD = 0
id_AppMenu_PANEL = 1

class HeGuiApp(App, MenuFunctions):
    kv_directory = os.path.join(os.path.dirname(__file__), "hegui", 'kv')
    # login
    username = StringProperty('')
    password = StringProperty('')
    # runs at server ot not
    runserver = False

    def build(self):

        global RootApp
        RootApp = self

        # NavigationDrawer
        self.navigationdrawer = NavDrawer()

        # SidePanel
        side_panel = SidePanel()
        self.navigationdrawer.add_widget(side_panel)

        # MainPanel
        self.main_panel = Login()

        self.navigationdrawer.anim_type = 'slide_above_anim'
        self.navigationdrawer.add_widget(self.main_panel)

        return self.navigationdrawer

    def toggle_sidepanel(self):
        self.navigationdrawer.toggle_state()

    def do_logout(self):
        Login().resetForm()
        self._switch_main_page('Login', Login)

    def do_quit(self):
        print 'App quit'
        self.stop()

    def _switch_main_page(self, key,  panel):
        self.navigationdrawer.close_sidepanel()
        if not SidePanel_AppMenu[key][id_AppMenu_PANEL]:
            SidePanel_AppMenu[key][id_AppMenu_PANEL] = panel()
        main_panel = SidePanel_AppMenu[key][id_AppMenu_PANEL]
        self.navigationdrawer.remove_widget(self.main_panel)    # FACCIO REMOVE ED ADD perchè la set_main_panel
        self.navigationdrawer.add_widget(main_panel)            # dà un'eccezione e non ho capito perchè
        self.main_panel = main_panel

    def get_application_config(self):
        if(not self.username):
            return super(HeGuiApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(HeGuiApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory)
        )

    # mensajes de sync
    def handle_message(self, msg):
        msg = msg.decode('utf-8')
        self.username = "received: {}\n".format(msg)
        if msg == "ping":
            msg = "Pong"
        if msg == "plop":
            msg = "Kivy Rocks!!!"
        self.username += "responded: {}\n".format(msg)
        return msg.encode('utf-8')

class SidePanel(BoxLayout):
    pass

class MenuItem(Button):
    def __init__(self, **kwargs):
        super(MenuItem, self).__init__( **kwargs)
        self.bind(on_press=self.menuitem_selected)

    def menuitem_selected(self, *args):
        print self.text, SidePanel_AppMenu[self.text], SidePanel_AppMenu[self.text][id_AppMenu_METHOD]
        try:
            function_to_call = SidePanel_AppMenu[self.text][id_AppMenu_METHOD]
        except:
            print 'errore de configuracion del diccionario de menu'
            return
        getattr(RootApp, function_to_call)()

#

class AppActionBar(ActionBar):
    pass

class ActionMenu(ActionPrevious):
    def menu(self):
        print 'ActionMenu'
        RootApp.toggle_sidepanel()

class ActionQuit(ActionButton):
    pass

class NavDrawer(NavigationDrawer):
    def __init__(self, **kwargs):
        super(NavDrawer, self).__init__( **kwargs)

    def close_sidepanel(self, animate=True):
        if self.state == 'open':
            if animate:
                self.anim_to_state('closed')
            else:
                self.state = 'closed'

class AppArea(FloatLayout):
    pass
