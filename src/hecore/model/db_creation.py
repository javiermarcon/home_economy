# -*- coding: utf-8 -*-

from model import * #User, Acounttype, Account, Category, Transaction, Currency, Currencyhistory, Instrument
from fixtures.currency import currency_table_data
from fixtures.acount import acount_table_data
import uuid

def create_and_populate_db(engine, connection):
    create_database(engine)
    create_user(connection)
    create_account_types(connection)
    create_currencies(connection)
    create_accounts(connection)
    connection.commit()
    #print Account().get_tree()

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
    account_types = ['Efectivo','Banco','Tarjeta','Inversion','Acciones','Moneda']
    for acc_name in account_types:
        act = Acounttype(id=create_id(), name=acc_name)
        connection.add(act)

def create_currencies(connection):
    for linea in currency_table_data:
        cu = Currency(id=create_id(), denomination=linea[0], name=linea[1],
                      bid=linea[2], ask=linea[3], symbol=linea[4],
                      conversion=linea[5], dec_places=linea[6])
        connection.add(cu)

def create_accounts(connection):
    for linea in acount_table_data:
        id_acc_type = unicode(Acounttype().get_one(acount_table_data[linea][2]).id)
        id_currency = unicode(Currency().get_one(acount_table_data[linea][3]).id)
        if acount_table_data[linea][1] is not None:
            ac = Account(id=unicode(acount_table_data[linea][0]), name=linea,
                     parent=unicode(acount_table_data[linea][1]),
                     id_account_type=id_acc_type, id_currency=id_currency,
                     balance=0)
        else:
            ac = Account(id=unicode(acount_table_data[linea][0]), name=linea,
                         id_account_type=id_acc_type, id_currency=id_currency,
                         balance=0)
        connection.add(ac)

def create_id():
    return str(uuid.uuid4())