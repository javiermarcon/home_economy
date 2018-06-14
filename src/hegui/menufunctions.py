# -*- coding: utf-8 -*-

import os

from kivy.uix.boxlayout import BoxLayout

from hegui.dbscreen import PaginaBd
from hegui.mainscreen import MainPanel
from hegui.cuentas import PaginaCuentas
from hegui.monedas import PaginaMonedas
from hegui.plugin_scr import PaginaPlugins

#--------------------------------------------------------------------------
'''dictionary that contains the correspondance between items descriptions
and methods that actually implement the specific function and panels to be
shown instead of the first main_panel
'''
SidePanel_AppMenu = {'Login': ['Login', None],
                     'MainPanel': ['MainPanel', None],
                     'Inicio': ['menu_inicio', None],
                     'Base de datos': ['menu_basedatos', None],
                     'Sincronizar': ['menu_sincro', None],
                     'Cuentas': ['menu_cuentas', None],
                     'Monedas': ['menu_monedas', None],
                     'Categorías': ['menu_categorias', None],
                     'Usuarios': ['menu_usuarios', None],
                     'Presupuestos': ['menu_presupuestos', None],
                     'Plugins': ['menu_plugins', None],
                     'Reportes': ['menu_reportes', None],
                     'Opciones': ['menu_opciones', None],
                     'Ayuda General': ['menu_ayuda', None],
                     'Preguntas frecuentes': ['menu_preguntas', None],
                     'Acerca de...': ['menu_acercade', None],
                     'Cerrar sesión': ['do_logout', None],
                     'Salir': ['do_quit', None],

                     }

#--------------------------------------------------------------------------

class MenuFunctions:

    def menu_inicio(self):
        #print 'UNO... exec'
        self._switch_main_page('MainPanel', MainPanel)

    def menu_basedatos(self, dbPath=''):
        # TODO: al hacer click en menu -> base de datos, se tiene que abrir popup de aviso, hacer logout y ponerte pantalla de login
        # TODO: simplificar llamadas de menu y que cargue menu en forma dinamica
        pag_bd = PaginaBd()
        conf_path = self.config.get('last_session', 'dbpath')
        if not dbPath == conf_path and dbPath.startswith('/'):
            conf_path = dbPath
        if not conf_path:
            conf_path = os.path.dirname(os.path.expanduser('~'))
        pag_bd.ids['lvl_bd'].text = conf_path
        pag_bd.ids['filechooser'].path = conf_path

        self._switch_main_page('Base de datos', pag_bd)

    def menu_cuentas(self):
        #print 'DUE... exec'
        self._switch_main_page('Cuentas', PaginaCuentas)
    def menu_monedas(self):
        #print 'TRE... exec'
        self._switch_main_page('Monedas',  PaginaMonedas)
    def menu_sincro(self):
        #print 'TRE... exec'
        self._switch_main_page('Sincronizar',  PaginaSincro)
    def menu_plugins(self):
        #print 'TRE... exec'
        self._switch_main_page('Plugins',  PaginaPlugins)
    def menu_opciones(self):
        self.open_settings()
    def menu_categorias(self):
        pass
    def menu_usuarios(self):
        pass
    def menu_presupuestos(self):
        pass
    def menu_reportes(self):
        pass
    def menu_ayuda(self):
        pass
    def menu_preguntas(self):
        pass
    def menu_acercade(self):
        pass


class PaginaSincro(BoxLayout):
    pass

