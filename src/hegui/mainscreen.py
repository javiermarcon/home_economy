# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.treeview import TreeViewLabel
from kivy.uix.recycleview import RecycleView

class MainPanel(BoxLayout):

    def __init__(self, **kwargs):
        super(MainPanel, self).__init__(**kwargs)
        mc = self.main_cuentas
        self.populate_treeview(mc)
        mc.bind(minimum_height=mc.setter('height'))

    def populate_treeview(self, tv):
        n = tv.add_node(TreeViewLabel(text='Item 1'))
        for x in xrange(30):
            tv.add_node(TreeViewLabel(text='Subitem %d' % x), n)
        n = tv.add_node(TreeViewLabel(text='Item 2', is_open=True))
        for x in xrange(30):
            tv.add_node(TreeViewLabel(text='Subitem %d' % x), n)
        n = tv.add_node(TreeViewLabel(text='Item 3'))
        for x in xrange(30):
            tv.add_node(TreeViewLabel(text='Subitem %d' % x), n)
        return tv

class RV(RecycleView):
    """ver: https://kivy.org/docs/api-kivy.uix.recycleview.html#kivy.uix.recycleview.RecycleView"""
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': 'Mensaje {}'.format(x)} for x in range(4)]
