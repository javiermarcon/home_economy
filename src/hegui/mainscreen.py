# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.recycleview import RecycleView
#from kivy.clock import Clock
from hegui.transaction import GuiTransaction
from libs.treeviewdb import TreeViewDb
from hecore.model.model import Account, Acounttype

class MainPanel(TreeViewDb):

    transaction_screen = None

    def __init__(self, **kwargs):
        super(MainPanel, self).__init__(**kwargs)
        #self.execute_initial_tasks()
        mc = self.main_cuentas
        self.set_treeview_data(Account, ['name', 'currency.symbol',
                                'balance', 'currency.name'], u'{} ({} {} {})',
                               Acounttype, ['name'], u'{}'
                               )
        self.populate_treeview(mc)
        mc.bind(minimum_height=mc.setter('height'))
        # Open the pop up
        app = App.get_running_app()
        app.popups.show_popup('Running some tasks...')

        # Call some method that may take a while to run.
        # I'm using a thread to simulate this
        self.execute_initial_tasks()

    def execute_initial_tasks(self):
        print("Ejecutando tareas iniciales")
        app = self.get_running_app()
        options = { "mail_plugins": {
            "email": app.config.get('mail_parser', 'email'),
            "password": app.config.get('mail_parser', 'password')
            }}
        if app.runserver:
            app.backend.launch_server()
        #app.backend.run_plugins(options)
        #trigger = Clock.create_trigger(my_callback)
        ## later
        #trigger()
        print("Listo")
        app.popups.close_popup()


    def add_transaction(self):
        if not self.transaction_screen:
            self.transaction_screen = GuiTransaction()
        app = self.get_running_app()
        app._switch_main_page('Transaction', self.transaction_screen)
        sn =  self.ids.main_cuentas.selected_node
        if sn:
            self.transaction_screen.ids.spAccount.select_by_id(sn.value)

    def get_running_app(self):
        return App.get_running_app()


class RV(RecycleView):
    """
    Muestra mensajes en la pantalla, poniendo los ultimos arriba.
    Si ingreso el mismo mensaje 2 veces, se muestra una sola vez, pero en la posicion que le corresponde
    a la ultima vez que se ingreso.
    ver:
        para funcionamiento general:
        https://kivy.org/docs/api-kivy.uix.recycleview.html#kivy.uix.recycleview.RecycleView
        para ocultarlo si no hay mensajes:
        https://stackoverflow.com/questions/41985573/hiding-and-showing-a-widget-in-kivy
    """

    messages = {} # the messages holded by the recicleview
    last_msg_num = 0 # number of the last message holded

    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.redraw_messages()
        """
        [ self.add_message("msg {}".format(x)) for x in range(4) ]
        [self.add_message("ASD {}".format(x)) for x in range(3,6)]
        num1 = self.add_message("weeeriz")
        num2 = self.add_message("weeeriz1")
        [self.add_message("msg {}".format(x)) for x in range(3,6)]
        self.remove_message_by_text("msg 2")
        self.remove_message_by_num(num1)
        pprint.pprint(self.messages)
        """

    def add_message(self, message):
        self.last_msg_num = self.last_msg_num + 1
        self.messages[message] = self.last_msg_num
        self.redraw_messages()
        return self.last_msg_num

    def remove_message_by_num(self, message_num):
        message = self.get_message_by_number(message_num)
        if message:
            self.remove_message_by_text(message)

    def remove_message_by_text(self, message):
        del self.messages[message]
        self.redraw_messages()

    def redraw_messages(self):

        if self.messages:
            dt = [{'text': x} for x in sorted(self.messages,
                                              key=self.messages.__getitem__,
                                              reverse=True)]
            self.data = dt
        else:
            self.data = []

    def get_message_by_number(self, number):
        val = [k for k, v in self.messages.iteritems() if v == number]
        if val:
            return val[0]
        return None