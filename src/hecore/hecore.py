#!/usr/bin/env python
# -*- coding: utf-8 -*-

# absolute_import para compatibilidad entre python 2 y 3
from __future__ import absolute_import
from hecore.model.model import *
from hecore.plugin_logic import plugin_logic
import os
import uuid

class CommonOperations:
    """Hace las operaciones comunes como transacciones en db por ejemplo"""

    def add_transaction(self, tr_date, destiny, id_category, ammount, operation='Gasto', origin=None, number=None,
                        id_instrument=None, transaction_member=None, notes=None):

        """Agrega una transaccion a la base de datos"""
        conn = DB_CONN.get_connection()
        trans = Transaction()
        tr_id = unicode(uuid.uuid4())
        trans.id = tr_id
        trans.date = tr_date
        trans.origin = origin
        trans.destiny = destiny
        trans.id_category = id_category
        trans.number = number
        trans.id_instrument = id_instrument
        trans.transaction_member = transaction_member
        # Si es gasto es negativo, si es ingreso es positivo
        if operation == "Gasto":
            ammount = abs(float(ammount)) * -1.0
        elif operation == "Ingreso":
            ammount = abs(float(ammount))
        trans.ammount = ammount
        trans.notes = notes
        errors = trans.validate_required()
        if errors:
            return errors
        conn.add(trans)
        conn.commit()


class HecoreBackend:
    """
    Esta clase se encarga de hacer todas las operaciones que pide la gui
    coordinado las acciones de todos los módulos.
    """
    db = DB_CONN
    config = None
    plugins = None
    common_operations = CommonOperations()

    def launch_server(self):
        """
        Lanza el servidor twisted para escuchar pedidos de syncro
        :return: None
        """
        from twisted.internet import reactor
        from hesync.hesync import EchoServerFactory
        reactor.listenTCP(8000, EchoServerFactory(self))
        return

    def check_file_exists(self, filePath):
        return os.path.isfile(filePath)

    def set_ini_location(self, location):
        self.ini_location = location

    def run_plugins(self, options):
        pluginrun = plugin_logic(options)
        ret = pluginrun.run_plugins()
        if ret:
            for plugin_iter in ret:
                for p in plugin_iter:
                    print("zzz {} ".format(p))
