from kivy.uix.boxlayout import BoxLayout

#--------------------------------------------------------------------------
'''dictionary that contains the correspondance between items descriptions
and methods that actually implement the specific function and panels to be
shown instead of the first main_panel
'''
SidePanel_AppMenu = {'Login': ['Login',None],
                     'MainPanel': ['MainPanel',None],
                     'Inicio':['on_uno',None],
                     'Cuentas':['on_due',None],
                     'Sincronizar':['on_tre',None],
                     }

#--------------------------------------------------------------------------

class MenuFunctions:

    def on_uno(self):
        print 'UNO... exec'
        self._switch_main_page('Inicio', PaginaInicio)

    def on_due(self):
        print 'DUE... exec'
        self._switch_main_page('Cuentas', PaginaCuentas)
    def on_tre(self):
        print 'TRE... exec'
        self._switch_main_page('Sincronizar',  PaginaSincro)

class PaginaInicio(BoxLayout):
    pass

class PaginaCuentas(BoxLayout):
    pass

class PaginaSincro(BoxLayout):
    pass
