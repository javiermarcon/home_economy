#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from functools import partial

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from KivyCalendar import DatePicker
from lib.float_input import FloatInput
from lib.hvspinner import HVSpinner

from hecore.model.model import Account, Category

import datetime

#TODO: refactorizar para que get_running_app este en una subclase de BoxLayout

class GuiTransaction(BoxLayout):

    trans_type = "Gasto"

    def __init__(self):
        super(GuiTransaction, self).__init__()
        self.fill_spinners()

    def select_default_value_in_spinners(self):
        app = App.get_running_app()
        default_account = app.config.get('transaction', 'account')
        default_category = app.config.get('transaction', 'category')
        self.ids['spAccount'].select_by_id(default_account)
        self.ids['spCategory'].select_by_id(default_category)

    def fill_spinners(self):
        (ids, names) = Account().get_lists_of_ids_and_names("{}", ["name"])
        self.ids.spAccount.hidden_values = ids
        self.ids.spAccount.values = names
        (ids, names) = Category().get_lists_of_ids_and_names("{}", ["name"])
        self.ids.spCategory.hidden_values = ids
        self.ids.spCategory.values = names
        self.select_default_value_in_spinners()

    def do_add(self, tr_date, ammount, notes, account_id, category_id):
        print(self.trans_type)
        app = App.get_running_app()
        common_operations = app.backend.common_operations
        t_date = datetime.datetime.strptime(tr_date, "%d.%m.%Y")
        errors = common_operations.add_transaction(t_date, account_id, category_id, ammount,
                                                   operation=self.trans_type, notes=notes)
        if errors:
            msg = 'Error al agregar la transaccion. Complete los campos: {}'.format(' '.join(errors))
            self.ids['error_msg'].text = msg
        else:
            self.clearandclose()

    def clearandclose(self):
        self.clear()
        self.return_previous_page()

    def clear(self):
        text_ids = ['error_msg', 'ammount', 'notes']
        for tid in text_ids:
            self.ids[tid].text = ''
        self.select_default_value_in_spinners()

    def return_previous_page(self):
        app = App.get_running_app()
        app.change_panel(app.last_panel)

    def change_trans_type(self, trans_type):
        self.trans_type = trans_type