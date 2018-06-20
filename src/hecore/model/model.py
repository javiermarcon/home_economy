# -*- coding: utf-8 -*-

#import os
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import Session, relationship, backref, joinedload_all
from sqlalchemy.orm.collections import attribute_mapped_collection
#from sqlalchemy.ext.orderinglist import ordering_list
import itertools
#from kivy.app import App

from base import DB_CONN, DECLARATIVE_BASE
from hecore.crypt_functions import PWD_CONTEXT

from sqlalchemy.sql.expression import func
from sqlalchemy import Enum as ENUM, String as BLOB, Float as FLOAT, String as VARCHAR, Date as DATE, Integer

class INTEGER(Integer):
    def __init__(self, *args, **kwargs):
        super(Integer, self).__init__()

def sort_db(obj):
    return obj.name


class TreeClass():
    def get_all(self):
        result = []
        rootNodes = sorted(DB_CONN.get_connection().query(self.__class__). \
            options(joinedload_all("children", "children",
                                   "children", "children")). \
            filter(self.__class__.parent == None).all(), key=sort_db)
        for node in rootNodes:
            result.extend(node.get_with_childrens())

        return result

    def get_with_childrens(self):
        res = [self]
        childs = [c.get_with_childrens() for c in sorted(self.children.values(), key=sort_db)]
        if childs:
            ret_flat = list(itertools.chain.from_iterable(childs))
            res.extend(ret_flat)
        return res


class User(DECLARATIVE_BASE):
    """
    Maneja un usuario y sus acciones.
    """
    __tablename__ = 'User'

    id = Column(VARCHAR(32), autoincrement=False, primary_key=True, nullable=False)  # pylint: disable=invalid-name
    login = Column(VARCHAR(45), nullable=False)
    password = Column(VARCHAR(256), nullable=False)
    name = Column(VARCHAR(45), nullable=False)
    surname = Column(VARCHAR(45), nullable=False)
    default_account = Column(VARCHAR(32))
    password_type = Column(VARCHAR(32))
    state = Column(VARCHAR(1))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<User(%(id)s)>" % self.__dict__

    def verify_login(self, username, password):
        """
        Performs login verification
        :param user: nombre de usuario
        :param password: contraseña de usuario
        :return: Booleano si se autentifica o no
        """
        result = DB_CONN.get_connection().query(User).filter_by(login=username).first()
        #print(result)
        if not result:
            return False
        #print (password)
        return PWD_CONTEXT.verify(password, result.password)


class Acounttype(DECLARATIVE_BASE):

    __tablename__ = 'AcountType'

    id = Column(VARCHAR(32), autoincrement=False, primary_key=True, nullable=False)  # pylint: disable=invalid-name
    name = Column(VARCHAR(45), nullable=False)
    module = Column(VARCHAR(45))

    def get_one(self, name):
        result = DB_CONN.get_connection().query(Acounttype).filter(Acounttype.name == name).one_or_none()
        return result

    def get_all(self):
        result = DB_CONN.get_connection().query(Acounttype).order_by(Acounttype.name).all()
        return result

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Acounttype(%(id)s)>" % self.__dict__


class Account(DECLARATIVE_BASE, TreeClass):

    __tablename__ = 'Account'

    id = Column(VARCHAR(32), autoincrement=False, primary_key=True, nullable=False)  # pylint: disable=invalid-name
    name = Column(VARCHAR(45), nullable=False)
    parent = Column(VARCHAR(32), ForeignKey(id))
    id_account_type = Column(VARCHAR(32), ForeignKey("AcountType.id"), index=True, nullable=False)
    id_currency = Column(VARCHAR(32), ForeignKey("Currency.id"), index=True, nullable=False)

    acounttype = relationship("Acounttype", foreign_keys=[id_account_type], backref="account")
    currency = relationship("Currency", foreign_keys=[id_currency], backref="account")
    balance = Column(FLOAT, nullable=False)
    children = relationship(
        "Account",
        # cascade deletions
        cascade="all, delete-orphan",
        # many to one + adjacency list - remote_side
        # is required to reference the 'remote'
        # column in the join condition.
        backref=backref("r_parent", remote_side=id),
        # children will be represented as a dictionary
        # on the "name" attribute.
        collection_class=attribute_mapped_collection('name'))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Account(%(id)s)>" % self.__dict__


class Category(DECLARATIVE_BASE, TreeClass):

    __tablename__ = 'Category'

    id = Column(VARCHAR(32), autoincrement=False, primary_key=True, nullable=False)  # pylint: disable=invalid-name
    parent = Column(VARCHAR(32), ForeignKey(id))
    name = Column(VARCHAR(45), nullable=False)
    balance = Column(FLOAT, nullable=False)
    children = relationship(
        "Category",
        # cascade deletions
        cascade="all, delete-orphan",
        # many to one + adjacency list - remote_side
        # is required to reference the 'remote'
        # column in the join condition.
        backref=backref("r_parent", remote_side=id),
        # children will be represented as a dictionary
        # on the "name" attribute.
        collection_class=attribute_mapped_collection('name'))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Category(%(id)s)>" % self.__dict__


class Transaction(DECLARATIVE_BASE):

    __tablename__ = 'transaction'

    id = Column(VARCHAR(32), autoincrement=False, primary_key=True, nullable=False)  # pylint: disable=invalid-name
    origin = Column(VARCHAR(32), nullable=False)
    destiny = Column(VARCHAR(32), nullable=False)
    id_category = Column(VARCHAR(32), nullable=False)
    number = Column(VARCHAR(45), nullable=False)
    id_instrument = Column(VARCHAR(32), nullable=False)
    transaction_member = Column(VARCHAR(32))
    ammount = Column(FLOAT, nullable=False)
    notes = Column(BLOB)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Transaction(%(id)s)>" % self.__dict__


class Currency(DECLARATIVE_BASE):

    __tablename__ = 'Currency'

    id = Column(VARCHAR(32), autoincrement=False, primary_key=True, nullable=False)  # pylint: disable=invalid-name
    denomination = Column(VARCHAR(3), nullable=False)
    name = Column(VARCHAR(45), nullable=False)
    bid = Column(FLOAT)
    ask = Column(FLOAT)
    symbol = Column(VARCHAR(10))
    conversion = Column(FLOAT)
    dec_places = Column(INTEGER)

    def get_one(self, denom):
        result = DB_CONN.get_connection().query(Currency).filter(Currency.denomination == denom).one_or_none()
        return result

    def get_all(self):
        result = DB_CONN.get_connection().query(Currency).order_by(Currency.denomination).all()
        return result

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Currency(%(id)s)>" % self.__dict__

class Currencyhistory(DECLARATIVE_BASE):

    __tablename__ = 'CurrencyHistory'

    id = Column(INTEGER, autoincrement=False, primary_key=True, nullable=False)  # pylint: disable=invalid-name
    id_currency = Column(VARCHAR(32), ForeignKey("Currency.id"), index=True, nullable=False)
    date = Column(DATE)
    bid = Column(FLOAT)
    ask = Column(FLOAT)

    currency = relationship("Currency", foreign_keys=[id_currency], backref="currencyhistory")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Currencyhistory(%(id)s)>" % self.__dict__


class Instrument(DECLARATIVE_BASE):

    __tablename__ = 'Instrument'

    id = Column(VARCHAR(32), autoincrement=False, primary_key=True, nullable=False)  # pylint: disable=invalid-name
    name = Column(VARCHAR(45), nullable=False)
    denomination = Column(VARCHAR(45))
    notes = Column(VARCHAR(200))
    id_currency = Column(VARCHAR(32), nullable=False)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Instrument(%(id)s)>" % self.__dict__
