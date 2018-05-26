# -*- coding: utf-8 -*-

#import os
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey

#from kivy.app import App

from base import DB_CONN, DECLARATIVE_BASE, PWD_CONTEXT

#if os.environ.get('DB_TYPE', 'MySQL') == 'MySQL':
#    from sqlalchemy.dialects.mysql import FLOAT, VARCHAR, ENUM, CHAR, BLOB, DATE, INTEGER
#else:
from sqlalchemy import Enum as ENUM, String as BLOB, Float as FLOAT, String as VARCHAR, Date as DATE, Integer

class INTEGER(Integer):
    def __init__(self, *args, **kwargs):
        super(Integer, self).__init__()

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

    tipos = ['cash', 'bank', 'credit card', 'investment', 'stock','currency_exchange']

    id = Column(VARCHAR(32), autoincrement=False, primary_key=True, nullable=False)  # pylint: disable=invalid-name
    name = Column(VARCHAR(45), nullable=False)
    type = Column(ENUM(tipos), nullable=False)
    module = Column(VARCHAR(45))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Acounttype(%(id)s)>" % self.__dict__


class Account(DECLARATIVE_BASE):

    __tablename__ = 'Account'

    id = Column(VARCHAR(32), autoincrement=False, primary_key=True, nullable=False)  # pylint: disable=invalid-name
    name = Column(VARCHAR(45), nullable=False)
    parent = Column(VARCHAR(32))
    id_account_type = Column(VARCHAR(32), ForeignKey("AcountType.id"), index=True, nullable=False)
    id_currency = Column(VARCHAR(32), ForeignKey("Currency.id"), index=True, nullable=False)

    acounttype = relationship("Acounttype", foreign_keys=[id_account_type], backref="account")
    currency = relationship("Currency", foreign_keys=[id_currency], backref="account")
    balance = Column(FLOAT, nullable=False)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Account(%(id)s)>" % self.__dict__


class Category(DECLARATIVE_BASE):

    __tablename__ = 'Category'

    id = Column(VARCHAR(32), autoincrement=False, primary_key=True, nullable=False)  # pylint: disable=invalid-name
    parent = Column(VARCHAR(32), nullable=False)
    name = Column(VARCHAR(45), nullable=False)

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

"""
class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # Use default=func.now() to set the default hiring time
    # of an Employee to be the current time when an
    # Employee record was created
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer, ForeignKey('department.id'))
    # Use cascade='delete,all' to propagate the deletion of a Department onto its Employees
    department = relationship(
        Department,
        backref=backref('employees',
                        uselist=True,
                        cascade='delete,all'))
"""