# -*- coding: utf-8 -*-

from hecore.model.model import User, Acounttype, Account, Category, Currency, Transaction, Currencyhistory, Instrument
from hecore.model.base import DECLARATIVE_BASE
from hecore.crypt_functions import PWD_CONTEXT
from hecore.model.fixtures.currency import currency_table_data
from hecore.model.fixtures.acount import acount_table_data
from hecore.model.fixtures.category import category_table_data
from collections import OrderedDict
import sys
import uuid
# para compatibilidad de unicode con python 3
from builtins import str as unicode

def get_table_creation_funcs():
    ret = OrderedDict()
    ret["User"] = create_user
    ret["Acounttype"] = create_account_types
    ret["Currency"] = create_currencies
    ret["Account"] = create_accounts
    ret["Category"] = create_categories
    ret["Instrument"] = dummy_function
    ret["Transaction"] = dummy_function
    ret["Currencyhistory"] = dummy_function
    return ret

def create_and_populate_db(dbclass):
    create_database(dbclass.engine)
    populate_db(dbclass, False)

def populate_db(dbclass, only_empty_tables=True):
    print("Lenando las tablas iniciales..")
    funcs = get_table_creation_funcs()
    for func in funcs:
        tbl_func = getattr(sys.modules[__name__], func)
        if not only_empty_tables or dbclass.check_empty_table(tbl_func):
            print("llenando la tabla {}".format(func))
            funcs[func](dbclass.connection)
    dbclass.connection.commit()

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
    account_types = ['Efectivo','Banco','Tarjeta','Inversion','Moneda'] #,'Acciones'
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

def create_categories(connection):
    for linea in category_table_data:
        if category_table_data[linea][1] is not None:
            ac = Category(id=unicode(category_table_data[linea][0]), name=linea,
                     parent=unicode(category_table_data[linea][1]),
                     balance=0)
        else:
            ac = Category(id=unicode(category_table_data[linea][0]), name=linea,
                         balance=0)
        connection.add(ac)

def create_id():
    return str(uuid.uuid4())

def dummy_function(connection):
    pass
