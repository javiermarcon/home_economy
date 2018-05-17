# -*- coding: utf-8 -*-

import json

# ver https://gist.github.com/kived/610386b5181219622e33 para entry tipo password

settings_data = {
    "Session Settings": json.dumps([
        {"type": "path",
        "title": "database",
        "desc": "Path to the database to use to store data.",
        "section": "last_session",
        "key": "dbpath"
        },
        {"type": "bool",
        "title": "keep me logged in",
        "desc": "If you switch on this option, you will automatically login.",
        "section": "last_session",
        "key": "keeplogged"
        }
    ]),
    "Email Parser Settings": json.dumps([
        {"type": "string",
        "title": "mail account",
        "desc": "Specify the mail account for the email parsing plugins.",
        "section": "mail_parser",
        "key": "email"
        },
        {"type": "string",
        "title": "mail password",
        "desc": "Specify the mail password for the email parsing plugins.",
        "section": "mail_parser",
        "key": "password"
        }
    ]),
}