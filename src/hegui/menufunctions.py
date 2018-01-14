# -*- coding: utf-8 -*-

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from hegui.mainscreen import MainPanel

#--------------------------------------------------------------------------
'''dictionary that contains the correspondance between items descriptions
and methods that actually implement the specific function and panels to be
shown instead of the first main_panel
'''
SidePanel_AppMenu = {'Login': ['Login', None],
                     'MainPanel': ['MainPanel', None],
                     'Inicio': ['menu_inicio', None],
                     'Base de datos': ['menu_cuentas', None],
                     'Sincronizar': ['menu_sincro', None],
                     'Cuentas': ['menu_cuentas', None],
                     'Monedas': ['menu_cuentas', None],
                     'Categorías': ['menu_cuentas', None],
                     'Usuarios': ['menu_cuentas', None],
                     'Presupuestos': ['menu_cuentas', None],
                     'Reportes': ['menu_cuentas', None],
                     'Ayuda General': ['menu_cuentas', None],
                     'Preguntas frecuentes': ['menu_cuentas', None],
                     'Acerca de...': ['menu_cuentas', None],
                     'Cerrar sesión': ['do_logout', None],
                     'Salir': ['do_quit', None],

                     }

#--------------------------------------------------------------------------

class MenuFunctions:

    def menu_inicio(self):
        print 'UNO... exec'
        self._switch_main_page('MainPanel', MainPanel)

    def menu_cuentas(self):
        print 'DUE... exec'
        self._switch_main_page('Cuentas', PaginaCuentas)
    def menu_sincro(self):
        print 'TRE... exec'
        self._switch_main_page('Sincronizar',  PaginaSincro)

class PaginaCuentas(FloatLayout):
    pass

class PaginaSincro(FloatLayout):
    pass
