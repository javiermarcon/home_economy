# -*- coding: utf-8 -*-

import json

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
    ])
}