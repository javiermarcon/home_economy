"""
This file has been automatically generated with workbench_alchemy v0.2.3
For more details please check here:
https://github.com/PiTiLeZarD/workbench_alchemy
"""

import os
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

if os.environ.get('DB_TYPE', 'MySQL') == 'MySQL':
    from sqlalchemy.dialects.mysql import FLOAT, VARCHAR, ENUM, CHAR, BLOB, DATE, INTEGER
else:
    from sqlalchemy import Enum as ENUM, String as BLOB, Float as FLOAT, String as VARCHAR, Date as DATE, Char as CHAR, \
        Integer

    class INTEGER(Integer):
        def __init__(self, *args, **kwargs):
            super(Integer, self).__init__()


DECLARATIVE_BASE = declarative_base()


class User(DECLARATIVE_BASE):

    __tablename__ = 'User'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(VARCHAR(32), autoincrement=False, primary_key=True, nullable=False)  # pylint: disable=invalid-name
    login = Column(VARCHAR(45), nullable=False)
    password = Column(VARCHAR(45), nullable=False)
    name = Column(VARCHAR(45), nullable=False)
    surname = Column(VARCHAR(45), nullable=False)
    default_account = Column(VARCHAR(32))
    password_type = Column(VARCHAR(32))
    state = Column(CHAR(1))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<User(%(id)s)>" % self.__dict__


class Acounttype(DECLARATIVE_BASE):

    __tablename__ = 'AcountType'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(VARCHAR(32), autoincrement=False, primary_key=True, nullable=False)  # pylint: disable=invalid-name
    name = Column(VARCHAR(45), nullable=False)
    type = Column(ENUM('cash', 'bank', 'credit card', 'investment', 'currency_exchange'), nullable=False)
    module = Column(VARCHAR(45))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Acounttype(%(id)s)>" % self.__dict__


class Accountgroup(DECLARATIVE_BASE):

    __tablename__ = 'AccountGroup'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(VARCHAR(32), autoincrement=False, primary_key=True, nullable=False)  # pylint: disable=invalid-name
    name = Column(VARCHAR(45), nullable=False)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Accountgroup(%(id)s)>" % self.__dict__


class Account(DECLARATIVE_BASE):

    __tablename__ = 'Account'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(VARCHAR(32), autoincrement=False, primary_key=True, nullable=False)  # pylint: disable=invalid-name
    name = Column(VARCHAR(45), nullable=False)
    parent = Column(VARCHAR(32))
    id_account_type = Column(VARCHAR(32), ForeignKey("AcountType.id"), index=True, nullable=False)
    id_currency = Column(VARCHAR(32), ForeignKey("Currency.id"), index=True, nullable=False)
    id_account_group = Column(VARCHAR(32), ForeignKey("AccountGroup.id"), index=True, nullable=False)

    acounttype = relationship("Acounttype", foreign_keys=[id_account_type], backref="account")
    currency = relationship("Currency", foreign_keys=[id_currency], backref="account")
    accountgroup = relationship("Accountgroup", foreign_keys=[id_account_group], backref="account")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Account(%(id)s)>" % self.__dict__


class Category(DECLARATIVE_BASE):

    __tablename__ = 'Category'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(VARCHAR(32), autoincrement=False, primary_key=True, nullable=False)  # pylint: disable=invalid-name
    parent = Column(VARCHAR(32), nullable=False)
    name = Column(VARCHAR(45), nullable=False)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Category(%(id)s)>" % self.__dict__


class Transaction(DECLARATIVE_BASE):

    __tablename__ = 'transaction'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(VARCHAR(32), autoincrement=False, primary_key=True, nullable=False)  # pylint: disable=invalid-name
    origin = Column(VARCHAR(32), nullable=False)
    destiny = Column(VARCHAR(32), nullable=False)
    id_category = Column(VARCHAR(32), nullable=False)
    number = Column(VARCHAR(45), nullable=False)
    id_instrument = Column(VARCHAR(32), nullable=False)
    transaction_member = Column(VARCHAR(32))
    notes = Column(BLOB)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Transaction(%(id)s)>" % self.__dict__


class Currency(DECLARATIVE_BASE):

    __tablename__ = 'Currency'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(VARCHAR(32), autoincrement=False, primary_key=True, nullable=False)  # pylint: disable=invalid-name
    denomination = Column(VARCHAR(3), nullable=False)
    name = Column(VARCHAR(45), nullable=False)
    bid = Column(FLOAT)
    ask = Column(FLOAT)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Currency(%(id)s)>" % self.__dict__


class Currencyhistory(DECLARATIVE_BASE):

    __tablename__ = 'CurrencyHistory'
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

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
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    )

    id = Column(VARCHAR(32), autoincrement=False, primary_key=True, nullable=False)  # pylint: disable=invalid-name
    name = Column(VARCHAR(45), nullable=False)
    denomination = Column(VARCHAR(45))
    notes = Column(VARCHAR(200))
    id_currency = Column(VARCHAR(32), nullable=False)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Instrument(%(id)s)>" % self.__dict__
