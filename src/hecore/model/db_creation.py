# -*- coding: utf-8 -*-

from model import * #User, Acounttype, Account, Category, Transaction, Currency, Currencyhistory, Instrument
from fixtures.currency import currency_table_data
import uuid

def create_and_populate_db(engine, connection):
    create_database(engine)
    create_user(connection)
    create_account_types(connection)
    create_currencies(connection)
    connection.commit()
    # TODO: agregar los registros iniciales como cuentas x defecto

def create_database(engine):
    DECLARATIVE_BASE.metadata.create_all(engine)


def create_user(connection):
    # agrego un usuario llamado admin con clave admin
    hashs = PWD_CONTEXT.encrypt("admin")
    # print hashs
    user = User(id=create_id(), login='admin', password=hashs, name='', surname='',
                default_account='', password_type='default', state='A')
    connection.add(user)

def create_account_types(connection):
    account_types = ['Efectivo','Banco','Tarjeta','Inveersion','Acciones','Moneda']
    for acc_name in account_types:
        act = Acounttype(id=create_id(), name=acc_name)
        connection.add(act)

    accounts = {

    }

def create_currencies(connection):
    for linea in currency_table_data:
        cu = Currency(id=create_id(), denomination=linea[0], name=linea[1],
                      bid=linea[2], ask=linea[3], symbol=linea[4],
                      conversion=linea[5], dec_places=linea[6])
        connection.add(cu)

def create_id():
    return str(uuid.uuid4())