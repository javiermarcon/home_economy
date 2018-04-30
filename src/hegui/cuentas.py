# -*- coding: utf-8 -*-

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.treeview import TreeViewLabel

class PaginaCuentas(BoxLayout):

    def __init__(self, **kwargs):
        super(PaginaCuentas, self).__init__(**kwargs)
        mc = self.main_cuentas
        self.populate_treeview(mc)
        mc.bind(minimum_height=mc.setter('height'))

    def populate_treeview(self, tv):
        n = tv.add_node(TreeViewLabel(text='Item 1'))
        for x in xrange(3):
            tv.add_node(TreeViewLabel(text='Subitem %d' % x), n)
        n = tv.add_node(TreeViewLabel(text='Item 2', is_open=True))
        for x in xrange(3):
            tv.add_node(TreeViewLabel(text='Subitem %d' % x), n)
        n = tv.add_node(TreeViewLabel(text='Item 3'))
        for x in xrange(3):
            tv.add_node(TreeViewLabel(text='Subitem %d' % x), n)
        return tv

