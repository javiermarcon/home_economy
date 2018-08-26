# -*- coding: utf-8 -*-

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.treeview import TreeViewLabel
from util.recursive_attributes import rec_getattr

class TreeViewDb(BoxLayout):

    nodos_cuenta = {}
    nodos_tipo = {}
    dbparentclass = None
    dbparentargs = None
    dbparenttext = None
    dbchildclass = None
    dbchildargs = None
    dbchildtext = None

    def populate_treeview(self, tv):
        """
        Llena el tree view
        :param tv: kivy tree view
        :return: None
        """
        if self.dbparentclass:
            tipos_cuenta = self.dbparentclass.get_all()
            for act in tipos_cuenta:
                act_params = [rec_getattr(act, attr) for attr in self.dbparentargs]
                txt_act = self.dbparenttext.format(*act_params)
                nodo = tv.add_node(TreeViewLabel(text=txt_act, is_open=True))
                self.nodos_tipo[act.id] = nodo
        cuentas = self.dbchildclass.get_all()

        for cuenta in cuentas:
            c_params = [rec_getattr(cuenta, attr) for attr in self.dbchildargs]
            txt_cuenta = self.dbchildtext.format(*c_params)

            if cuenta.parent:
                nodo = tv.add_node(TreeViewLabel(text=txt_cuenta, is_open=True),
                                   self.nodos_cuenta[cuenta.parent])
            else:
                if self.dbparentclass:
                    nodo = tv.add_node(TreeViewLabel(text=txt_cuenta, is_open=True),
                                       self.nodos_tipo[cuenta.acounttype.id])
                else:
                    nodo = tv.add_node(TreeViewLabel(text=txt_cuenta, is_open=True))
            self.nodos_cuenta[cuenta.id] = nodo
        return tv

    def set_treeview_data(self, dbchildclass, dbchildargs, dbchildtext,
                          dbparentclass=None, dbparentargs=None, dbparenttext=None):
        self.dbchildclass = dbchildclass()
        self.dbchildargs = dbchildargs
        self.dbchildtext = dbchildtext
        if dbparentclass:
            self.dbparentclass = dbparentclass()
            self.dbparentargs = dbparentargs
            self.dbparenttext = dbparenttext

