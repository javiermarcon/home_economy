# -*- coding: utf-8 -*-

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.treeview import TreeViewLabel

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

    def set_data(self, dbchildclass, dbchildargs, dbchildtext,
                      dbparentclass=None, dbparentargs=None, dbparenttext=None):
        self.dbchildclass = dbchildclass()
        self.dbchildargs = dbchildargs
        self.dbchildtext = dbchildtext
        if dbparentclass:
            self.dbparentclass = dbparentclass()
            self.dbparentargs = dbparentargs
            self.dbparenttext = dbparenttext


def rec_getattr(obj, attr):
    """Get object's attribute. May use dot notation.

    >>> class C(object): pass
    >>> a = C()
    >>> a.b = C()
    >>> a.b.c = 4
    >>> rec_getattr(a, 'b.c')
    4
    """
    if '.' not in attr:
        return getattr(obj, attr)
    else:
        L = attr.split('.')
        return rec_getattr(getattr(obj, L[0]), '.'.join(L[1:]))

def rec_setattr(obj, attr, value):
    """Set object's attribute. May use dot notation.

    >>> class C(object): pass
    >>> a = C()
    >>> a.b = C()
    >>> a.b.c = 4
    >>> rec_setattr(a, 'b.c', 2)
    >>> a.b.c
    2
    """
    if '.' not in attr:
        setattr(obj, attr, value)
    else:
        L = attr.split('.')
        rec_setattr(getattr(obj, L[0]), '.'.join(L[1:]), value)