# -*- coding: utf-8 -*-

#from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView

from kivy.app import App
#from kivy.lang import Builder
#from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
#from kivy.metrics import dp
from hecore.crypt_functions import AESCipher, password_file

import os
from random import sample
from string import ascii_lowercase

class PaginaPlugins(BoxLayout):

    def __init__(self, **kwargs):
        super(PaginaPlugins, self).__init__(**kwargs)
        self.rvp.layout_manager.bind(selected_nodes=self.selectionChange)

    def selectionChange(self, inst, val):
        print("{} {}".format(inst, val))

    def run_all_plugins(self):
        app = App.get_running_app()
        pwpath = app.config.get('last_session', 'pwd_filename')
        if not os.path.isfile(pwpath):
            print("Please configure pw path")
            return
        pwd_text = password_file().get(pwpath)
        aci = AESCipher(pwd_text, 32)
        password = aci.decrypt(app.config.get('mail_parser', 'password'))
        options = {"mail_plugins": {
            "email": app.config.get('mail_parser', 'email'),
            "password": password
        }}
        #print options
        app.backend.run_plugins(options)

    def run_selected_plugin(self):
        print("Not implemented...")

class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': '_'.join(sample(ascii_lowercase, 6))} for x in range(20)]