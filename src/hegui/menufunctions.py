# -*- coding: utf-8 -*-

import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from hegui.dbscreen import PaginaBd
from hegui.mainscreen import MainPanel
from hegui.cuentas import PaginaCuentas
from hegui.categorias import PaginaCategorias
from hegui.monedas import PaginaMonedas
from hegui.plugin_scr import PaginaPlugins

from hecore.model.db_creation import populate_db

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
                     'Tareas de mantenimiento': ['menu_mantenimiento', None],
                     'Ayuda General': ['menu_ayuda', None],
                     'Preguntas frecuentes': ['menu_preguntas', None],
                     'Acerca de...': ['menu_acercade', None],
                     'Cerrar sesión': ['do_logout', None],
                     'Transaction': ['menu_transaction', None],
                     'Salir': ['do_quit', None],

                     }

#--------------------------------------------------------------------------

class MenuFunctions:

    def menu_inicio(self):
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
        self._switch_main_page('Cuentas', PaginaCuentas)
    def menu_monedas(self):
        self._switch_main_page('Monedas',  PaginaMonedas)
    def menu_sincro(self):
        self._switch_main_page('Sincronizar',  PaginaSincro)
    def menu_plugins(self):
        self._switch_main_page('Plugins',  PaginaPlugins)
    def menu_opciones(self):
        self.open_settings()
    def menu_categorias(self):
        self._switch_main_page('Categorías', PaginaCategorias)
    def menu_usuarios(self):
        pass

    def menu_mantenimiento(self):
        # llenar las tablas vacias si se upgradeo de version
        app = App.get_running_app()
        populate_db(app.backend.db, True)

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

