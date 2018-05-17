# -*- coding: utf-8 -*-

import datetime
import re

def run():
    price_regexp = "{}:\s+\$([0-9,.]+)"
    return {
        "mail_parser": {
            "mail_filters": ['SUBJECT "OXI Trade Notice -"', 'FROM noreply@optionsxpress.com'],
            "regex_parsers": {
                "symbol": re.compile("Symbol:\s+([a-zA-Z0-9\/_\-]+)\s*\n", re.M),
                "date": re.compile("The following transaction has been completed on (\d{1,2}\/\d{1,2}\/\d{2,4})\s*", re.M),
                "description": re.compile("Description:\s+([a-zA-Z0-9\/_\-\ ]+)\s*\n", re.M),
                "action": re.compile("Action:\s+([a-zA-Z]+)\s*\n", re.M),
                "quantity": re.compile("Quantity:\s+(\d+)\sshare", re.M),
                "price": re.compile(price_regexp.format("Price"), re.M),
                "commission": re.compile(price_regexp.format("Commission"), re.M),
                "reg_fee": re.compile(price_regexp.format("Reg Fees"), re.M),
                "total": re.compile(price_regexp.format("Net Amt"), re.M)
            },
            "transform_values": transform_values
        }
    }

def transform_values(values):
    """
    Transforms the searched values in the text to the actual values that will be stored
    :param values: values to transform
    :return: transformed values
    """
    if values["action"] == "Bought":
        operacion = "Compra"
    else:
        operacion = "Venta"
    ret = {
        "fecha": datetime.datetime.strptime(values["date"], "%m/%d/%Y"),
        "detalle": "{} ({})".format(values["description"], values["symbol"]),
        "tipo_operacion": operacion,
        "moneda": "USD",
        "gastos_trnasferencia": 0,
        "comision": float(values["commission"]) + float(values["reg_fee"]),
        "cantidad": int(values["quantity"]),
        "cotizacion": float(values["price"]),
        "tipo_cambio": 0
    }
    return ret