# -*- coding: utf-8 -*-

# absolute_import para compatibilidad entre python 2 y 3
from __future__ import absolute_import
from hecore.mail_reader import manage_email
#import re
import plugins

class plugin_logic:

    def __init__(self, options):
        self.options = options
        self.parser_functions = {
            "mail_parser": self.parse_mail_plugins,
            "http_parser":self.parse_http_plugin
        }

    def get_plugin_names(self):
        return plugins.modus

    def run_plugins(self):
        for modu in plugins.modus:
            current_mod = getattr(plugins, modu)
            if hasattr(current_mod, "run"):
                plugin_output = current_mod.run()
                for parser in self.parser_functions:
                    if parser in plugin_output.keys():
                        yield self.parser_functions[parser](plugin_output)


    def parse_mail_plugins(self, plugin_output):
        plugin_options = plugin_output["mail_parser"]
        patterns = plugin_options["mail_filters"]
        mail = manage_email(self.options["mail_plugins"]["email"], self.options["mail_plugins"]["password"])
        mail.select_folder()
        msgl = mail.search_messages(patterns=patterns)
        mails = mail.get_emails(msgl)
        for msg in mails:
            r = self._parse_mail_body(msg, plugin_options)
            yield r

    def _parse_mail_body(self, msg, plugin_options):
        body = msg['body']
        ret = {}
        for key in plugin_options["regex_parsers"]:
            rc = plugin_options["regex_parsers"][key]
            rm = rc.search(body)
            if rm:
                ret[key] = rm.group(1)
        return plugin_options["transform_values"](ret)

    def parse_http_plugin(self, plugin_output):
        #plugin_return = run()
        print(plugin_output)
        yield
