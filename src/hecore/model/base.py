#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# para autenticacion de usuarios
from hecore.crypt_functions import PWD_CONTEXT

# The database connection object

DECLARATIVE_BASE = declarative_base()

class Db:
    """Maneja las conexiones y model ode la base de datos con sqlalchemy"""
    connection = None
    engine = None
    default_path = None

    def set_default_path(self, filePath):
        self.default_path = filePath

    def connect(self, fileName=None):
        """Se conecta a la base de datos"""
        if not fileName:
            fileName = self.default_path
        cnnstr = "sqlite:///{}".format(fileName)
        #print (cnnstr)
        self.engine = create_engine(cnnstr)
        DBSession = sessionmaker()
        DBSession.configure(bind=self.engine)
        session = DBSession()
        self.connection = session
        return self.connection

    def create_and_connect_callback(self, fileName):
        self.connect(fileName)
        print ("creando la bd {}".format(fileName))
        # crear base de datos
        from db_creation import create_and_populate_db
        create_and_populate_db(self.engine, self.connection)

    def get_connection(self):
        if self.connection:
            return self.connection
        else:
            return self.connect()

DB_CONN = Db()
