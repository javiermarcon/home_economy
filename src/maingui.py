#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.app import App
#from kivy.properties import StringProperty
from kivy.config import ConfigParser

from hegui.navigationdrawer import NavigationDrawer
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.actionbar import ActionBar, ActionButton, ActionPrevious
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.settings import SettingsWithSidebar
from kivy.properties import StringProperty

import os
import random
import string

from hegui.login import Login
from hegui.menufunctions import MenuFunctions, SidePanel_AppMenu
from hegui.settings_data import settings_data, SettingPassword

from hecore.hecore import HecoreBackend
#from hecore.crypt_functions import password_file

RootApp = None
id_AppMenu_METHOD = 0
id_AppMenu_PANEL = 1


class HeGuiApp(App, MenuFunctions):
    kv_directory = os.path.join(os.path.dirname(__file__), "hegui", 'kv')
    # login
    username = StringProperty('')

    # runs at server ot not
    runserver = False
    # database connection object
    backend = HecoreBackend()
    # response of a popup
    popup_actions = None
    crypt_pwd_text = None

    def build_config(self, config):
        config.setdefaults('last_session', {
            'dbpath': '',
            'lastuser': '',
            'keeplogged': False,
            'pwd_filename': ""
        })
        config.setdefaults("mail_parser", {
            "email": "",
            "password": ""
        })

    def build_settings(self, settings):
        settings.register_type('password', SettingPassword)
        for panel_name in settings_data:
            settings.add_json_panel(panel_name, self.config, data=settings_data[panel_name])

    #def on_config_change(self, config, section, key, value):
    #    print config, section, key, value

    def build(self):
        # settings
        self.settings_cls = SettingsWithSidebar
        #self.use_kivy_settings = False
        #self.set_crypt_pwd_path()

        global RootApp
        RootApp = self

        # NavigationDrawer
        self.navigationdrawer = NavDrawer()

        # SidePanel
        side_panel = SidePanel()
        self.navigationdrawer.add_widget(side_panel)

        # MainPanel
        self.main_panel = Login()
        # last_panel stores the previous window to know which panel to choose
        # when we want to retun to previous window
        self.last_panel = self.main_panel

        self.navigationdrawer.anim_type = 'slide_above_anim'
        self.navigationdrawer.add_widget(self.main_panel)

        # set defailt path for db
        default_db_path = self.config.get('last_session', 'dbpath')
        self.backend.db.set_default_path(default_db_path)
        self.main_panel.ids['dbpath'].text = default_db_path

        return self.navigationdrawer

    def toggle_sidepanel(self):
        self.navigationdrawer.toggle_state()

    def do_logout(self):
        Login().reset_form()
        self._switch_main_page('Login', Login)

    def do_quit(self):
        #print 'App quit'
        self.stop()

    def open_popup(self, message, title='Confirmar', action_yes=None,
                   action_no=None, size=(480, 400), size_hint=(None, None)):
        self.popup_actions = {'action_yes': action_yes,
                              'action_no': action_no}
        content = ConfirmPopup(text=message)
        content.bind(on_answer=self._on_popup_answer)
        self.popup = Popup(title=title,
                           content=content,
                           size_hint=size_hint,
                           size=size,
                           auto_dismiss=False)
        self.popup.open()

    def _on_popup_answer(self, instance, answer):
        self.popup.dismiss()
        if answer:
            self.popup_actions['action_yes']()
        else:
            self.popup_actions['action_no']()

    def _switch_main_page(self, key,  panel):
        # last_panel stores the previous window to know which panel to choose
        # when we want to retun to previous window
        self.last_panel = self.main_panel
        self.navigationdrawer.close_sidepanel()
        if not SidePanel_AppMenu[key][id_AppMenu_PANEL]:
            if callable(panel):
                SidePanel_AppMenu[key][id_AppMenu_PANEL] = panel()
            else:
                SidePanel_AppMenu[key][id_AppMenu_PANEL] = panel
        main_panel = SidePanel_AppMenu[key][id_AppMenu_PANEL]
        self.change_panel(main_panel)

    def change_panel(self, panel):
        self.navigationdrawer.remove_widget(self.main_panel)  # saco la ventana anterior
        self.navigationdrawer.add_widget(panel)  # cargo la ventana nueva
        self.main_panel = panel

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

    def set_crypt_pwd_path(self):
        pwpath = self.config.get('last_session', 'pwd_filename')
        if not os.path.isfile(pwpath):
            #Config = ConfigParser.get_configparser('kivy')
            folder = os.path.dirname(ConfigParser.filename)
            rand_name = ''.join(random.choice(string.ascii_letters) for x in range(10))
            pwpath = os.path.join(folder, rand_name)
            self.config.set('last_session', 'pwd_filename', pwpath)
        self.crypt_pwd_path = pwpath
        return

class SidePanel(BoxLayout):
    pass

class MenuItem(Button):
    def __init__(self, **kwargs):
        super(MenuItem, self).__init__( **kwargs)
        self.bind(on_press=self.menuitem_selected)

    def menuitem_selected(self, *args):
        #print self.text, SidePanel_AppMenu[self.text], SidePanel_AppMenu[self.text][id_AppMenu_METHOD]
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
        #print 'ActionMenu'
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

class ConfirmPopup(GridLayout):
    text = StringProperty()

    def __init__(self, **kwargs):
        self.register_event_type('on_answer')
        super(ConfirmPopup, self).__init__(**kwargs)

    def on_answer(self, *args):
        pass

