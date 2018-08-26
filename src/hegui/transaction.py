#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from functools import partial

#from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from KivyCalendar import DatePicker
from libs.float_input import FloatInput
from libs.hvspinner import HVSpinner

from hecore.model.model import Account, Category

#TODO: refactorizar para que get_running_app este en una subclase de BoxLayout

class Transaction(BoxLayout):

    def __init__(self):
        super(Transaction, self).__init__()
        self.fill_spinners()

    def fill_spinners(self):
        (ids, names) = Account().get_lists_of_ids_and_names("{}", ["name"])
        self.ids.spAccount.hidden_values = ids
        self.ids.spAccount.values = names
        (ids, names) = Category().get_lists_of_ids_and_names("{}", ["name"])
        self.ids.spCategory.hidden_values = ids
        self.ids.spCategory.values = names

    def do_add(self, tr_date, ammount, notes, account_id, category_id):
        print tr_date, ammount, notes, account_id, category_id

