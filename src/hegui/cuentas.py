# -*- coding: utf-8 -*-

from hecore.model.model import Account, Acounttype
from lib.treeviewdb import TreeViewDb


class PaginaCuentas(TreeViewDb):

    def __init__(self, **kwargs):
        super(PaginaCuentas, self).__init__(**kwargs)
        mc = self.main_cuentas
        mc.bind(minimum_height=mc.setter('height'))
        self.set_treeview_data(Account, ['name', 'currency.symbol',
                      'balance', 'currency.name'], u'{} ({} {} {})',
                               Acounttype, ['name'], u'{}'
                               )
        self.populate_treeview(mc)
