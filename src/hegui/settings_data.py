# -*- coding: utf-8 -*-

import os
from kivy.app import App
from kivy.uix.settings import SettingString
from kivy.uix.label import Label
from kivy.config import ConfigParser

from hecore.crypt_functions import AESCipher, password_file, get_random_chars
from hecore.model.model import Account, Category

# ver https://gist.github.com/kived/610386b5181219622e33 para entry tipo password

settings_data = {
    "Session Settings": [
        {"type": "path",
         "title": "database",
         "desc": "Path to the database to use to store data.",
         "section": "last_session",
         "key": "dbpath"
         },
    ],
    "Automatic login": [
        {"type": "bool",
         "title": "Automatically login",
         "desc": "If you switch on this option, you will automatically login.",
         "section": "autologin",
         "key": "keeplogged"
         },
    ],
    "Configuration": [
        {"type": "path",
         "title": "password filename",
         "desc": "Path to the file to use to store password for encrypted ini settings.",
         "section": "configuration",
         "key": "pwd_filename"
         },

    ],
    "Email Parser Settings": [
        {"type": "string",
         "title": "mail account",
         "desc": "Specify the mail account for the email parsing plugins.",
         "section": "mail_parser",
         "key": "email"
         },
        {"type": "password",
         "title": "mail password",
         "desc": "Specify the mail password for the email parsing plugins.",
         "section": "mail_parser",
         "key": "password"
         }
    ],
    "Transaction Settings": [
        {
        "type": "title",
        "title": "Default Values"
        },
        {"type": "optionmapping",
         "title": "default account",
         "desc": "Specify the account to default in a transaction.",
         "section": "transaction",
         "key": "account",
         "options": Account
         },
         {"type": "optionmapping",
         "title": "default category",
         "desc": "Specify the category to default in a transaction.",
         "section": "transaction",
         "key": "category",
         "options": Category
         },
    ],
}


# this classes are for using a password field in settings
class SettingPassword(SettingString):
    def _create_popup(self, instance):
        super(SettingPassword, self)._create_popup(instance)
        self.textinput.password = True

    def _validate(self, instance):
        self._dismiss()
        value = self.textinput.text.strip()
        pwd_text = password_file().get(self._get_pw_path())
        aci = AESCipher(pwd_text, 32)
        self.value = aci.encrypt(value)
        print(self.value)  # Just for debugging

    def add_widget(self, widget, *largs):
        if self.content is None:
            super(SettingString, self).add_widget(widget, *largs)
        if isinstance(widget, PasswordLabel):
            return self.content.add_widget(widget, *largs)

    def _get_pw_path(self):
        app = App.get_running_app()
        pwpath = app.config.get('configuration', 'pwd_filename')
        if not os.path.isfile(pwpath):
            Config = ConfigParser.get_configparser("kivy")
            folder = os.path.dirname(Config.filename)
            rand_name = get_random_chars(10)
            pwpath = os.path.join(folder, rand_name)
            app.config.set('configuration', 'pwd_filename', pwpath)
        return pwpath


class PasswordLabel(Label):
    pass
