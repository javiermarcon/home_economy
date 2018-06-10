# -*- coding: utf-8 -*-

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.treeview import TreeViewLabel

from hecore.model.model import Account, Acounttype


class TreeCuentas(BoxLayout):

    nodos_cuenta = {}
    nodos_tipo = {}

    def populate_treeview(self, tv):
        """
        Llena el tree view
        :param tv:
        :return:
        """
        tipos_cuenta = Acounttype().get_all()
        for act in tipos_cuenta:
            nodo = tv.add_node(TreeViewLabel(text=act.name, is_open=True))
            self.nodos_tipo[act.id] = nodo
        cuentas = Account().get_all()
        for cuenta in cuentas:
            txt_cuenta = u'{} ({} {} {})'.format(cuenta.name, cuenta.currency.symbol,
                                                 cuenta.balance, cuenta.currency.name)
            if cuenta.parent:
                nodo = tv.add_node(TreeViewLabel(text=txt_cuenta, is_open=True),
                                   self.nodos_cuenta[cuenta.parent])
            else:
                nodo = tv.add_node(TreeViewLabel(text=txt_cuenta, is_open=True),
                                   self.nodos_tipo[cuenta.acounttype.id])
            self.nodos_cuenta[cuenta.id] = nodo
        return tv


class PaginaCuentas(TreeCuentas):

    def __init__(self, **kwargs):
        super(PaginaCuentas, self).__init__(**kwargs)
        mc = self.main_cuentas
        mc.bind(minimum_height=mc.setter('height'))
        self.populate_treeview(mc)
