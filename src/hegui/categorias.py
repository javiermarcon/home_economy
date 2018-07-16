# -*- coding: utf-8 -*-

from hecore.model.model import Category
from hegui.treeviewdb import TreeViewDb


class PaginaCategorias(TreeViewDb):

    def __init__(self, **kwargs):
        super(PaginaCategorias, self).__init__(**kwargs)
        mc = self.main_categorias
        mc.bind(minimum_height=mc.setter('height'))
        self.set_data(Category, ['name'], u'{}')
        self.populate_treeview(mc)
