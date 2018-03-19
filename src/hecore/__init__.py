# -*- coding: utf-8 -*-
""" Clases que va a exponer el módulo core:

Login: (user, password)
- do_login
- is_authenticated

User: (id, login, password, name, surname, default_account, pass_type, state)
- add
- remove
- modify
- list
- info

Account_Type:
- add
- remove
- modify
- list
- info

Account:
- add
- remove
- modify
- list
- info

Category: (id, parent, name)
- add
- remove
- modify
- list
- info

Transaction: (id, parent, origin, destiny, category, notes, number)
- add
- remove
- modify
- list
- info

Currenciy: (id, name, bid, ask)
- add
- remove
- modify
- list
- info

Instrument:
- add
- remove
- modify
- list
- info

Instrument_option:
- add
- remove
- modify
- list
- info

Instrument_value:
- add
- remove
- modify
- list
- info

Transaction:
- add
- remove
- modify
- list
- info

Currency:
- add
- remove
- modify
- list
- info

Configuration:
- read_all
- set
- get

Plugin:
- list
- add
- remove
- info
- enable
- disable
- is_enabled
- module_plugins

Translation:
- add
- remove
- modify
- list
- info

"""
