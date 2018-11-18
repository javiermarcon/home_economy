# -*- coding: utf-8 -*-

from kivy.uix.boxlayout import BoxLayout
from libs.kivydatagridplugin.Datagrid import DataGrid
from kivy.core.window import Window
#from kivy.graphics import Color
from hecore.model.model import Currency

class PaginaMonedas(BoxLayout):

    def __init__(self, **kwargs):
        super(PaginaMonedas, self).__init__(**kwargs)
        self.rellenar_tabla()

    def rellenar_tabla(self):
        curriencies = Currency().get_all()
        for currency in curriencies:
            tempData = [{'text': currency.denomination, 'type': 'BorderLabel'},
                        {'text': currency.name, 'type': 'BorderLabel'},
                        {'text': currency.symbol, 'type': 'BorderLabel'},
                        {'text': str(currency.bid), 'type': 'BorderLabel'},
                        {'text': str(currency.ask), 'type': 'BorderLabel'},
                        {'text': str(currency.conversion), 'type': 'BorderLabel'},
                        {'text': 'Modificar', 'type': 'BorderButton'},
                        {'text': 'Eliminar', 'type': 'BorderButton'}]
            #print(tempData)
            self.tabla.addRow(tempData)

class tablaMonedas(DataGrid):
    def __init__(self, **kwargs):
        super(tablaMonedas, self).__init__(**kwargs)
        self.setupGrid([{'text':"Denom.", 'type':'BorderLabel', 'width': 70},
			{'text':"Description", 'type':'BorderLabel', 'width': 280},
			{'text':"Symbol", 'type':'BorderLabel', 'width': 80},
			{'text':"Bid", 'type':'BorderLabel', 'width': 70},
			{'text':"Ask", 'type':'BorderLabel', 'width': 70},
			{'text':"Conv.", 'type':'BorderLabel', 'width': 70},
            {'text': "", 'type': 'Label', 'width': 80},
            {'text': "", 'type': 'Label', 'width': 80}], Window.width, 46)
