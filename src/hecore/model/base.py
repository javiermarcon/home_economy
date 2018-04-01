#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# para autenticacion de usuarios
from passlib.context import CryptContext

# The database connection object

DECLARATIVE_BASE = declarative_base()

PWD_CONTEXT = CryptContext(
        # Replace this list with the hash(es) you wish to support.
        # this example sets pbkdf2_sha256 as the default,
        # with additional support for reading legacy des_crypt hashes.
        schemes=["pbkdf2_sha256"],  # "des_crypt"],
        # Automatically mark all but first hasher in list as deprecated.
        # (this will be the default in Passlib 2.0)
        deprecated="auto",
        # Optionally, set the number of rounds that should be used.
        # Appropriate values may vary for different schemes,
        # and the amount of time you wish it to take.
        # Leaving this alone is usually safe, and will use passlib's defaults.
        ## pbkdf2_sha256__rounds = 29000,
    )

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

    def create_db(self, fileName):
        """Crea la base de datos"""
        print ("creando la bd {}".format(fileName))
        DECLARATIVE_BASE.metadata.create_all(self.engine)

        # agrego un usuario llamado admin con clave admin
        hash = PWD_CONTEXT.hash("admin")
        #print(hash)
        id = str(uuid.uuid4())
        from model import User
        user = User(id=id, login='admin', password=hash, name='', surname='',
                    default_account='', password_type='default', state='A')
        self.connection.add(user)
        self.connection.commit()

        # TODO: agregar los registros iniciales como usuario principal y cuentas x defecto

    def create_and_connect_callback(self, fileName):
        self.connect(fileName)
        self.create_db(fileName)

    def get_connection(self):
        if self.connection:
            return self.connection
        else:
            return self.connect()

DB_CONN = Db()
