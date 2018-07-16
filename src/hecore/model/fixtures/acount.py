# -*- coding: utf-8 -*-
import uuid

ad = {}

ad[u"Efectivo dolares"] = [uuid.uuid4(), None, u'Efectivo', u'USD']
ad[u"Efectivo encima"] = [uuid.uuid4(), None, u'Efectivo', u'ARS']
ad[u"Efectivo esther"] = [uuid.uuid4(), None, u'Efectivo', u'ARS']
ad[u"Efectivo guardado"] = [uuid.uuid4(), None, u'Efectivo', u'USD']
ad[u"Rz vacaciones"] = [uuid.uuid4(), None, u'Efectivo', u'BRL']
ad[u"Usd vacaciones"] = [uuid.uuid4(), None, u'Efectivo', u'USD']
ad[u"Ripio"] = [uuid.uuid4(), None, u'Moneda', u'ARS']
ad[u"Ripio pesos"] = [uuid.uuid4(), ad["Ripio"][0], u'Moneda', u'ARS']
ad[u"Ripio btc"] = [uuid.uuid4(), ad["Ripio"][0], u'Moneda', u'BTC']
ad[u"Galicia"] = [uuid.uuid4(), None, u'Banco', u'ARS']
ad[u"Hsbc"] = [uuid.uuid4(), None, u'Banco', u'ARS']
ad[u"Hsbc pesos"] = [uuid.uuid4(), ad["Hsbc"][0], u'Banco', u'ARS']
ad[u"Hsbc dolares"] = [uuid.uuid4(), ad["Hsbc"][0], u'Banco', u'USD']
ad[u"Hsbc cc"] = [uuid.uuid4(), ad["Hsbc"][0], u'Banco', u'ARS']
ad[u"Hsbc visa"] = [uuid.uuid4(), ad["Hsbc"][0], u'Tarjeta', u'ARS']
ad[u"Hsbc master"] = [uuid.uuid4(), ad["Hsbc"][0], u'Tarjeta', u'ARS']
ad[u"Hsbc visa usd"] = [uuid.uuid4(), ad["Hsbc"][0], u'Tarjeta', u'USD']
ad[u"Hsbc master usd"] = [uuid.uuid4(), ad["Hsbc"][0], u'Tarjeta', u'USD']
ad[u"Tarjeta Naranja"] = [uuid.uuid4(), None, u'Tarjeta', u'ARS']
ad[u"Naranja Visa"] = [uuid.uuid4(), ad["Tarjeta Naranja"][0], u'Tarjeta', u'ARS']
ad[u"Naranja Mastercard"] = [uuid.uuid4(), ad["Tarjeta Naranja"][0], u'Tarjeta', u'ARS']
ad[u"Naranja Naranja"] = [uuid.uuid4(), ad["Tarjeta Naranja"][0], u'Tarjeta', u'ARS']
ad[u"Naranja usd"] = [uuid.uuid4(), ad["Tarjeta Naranja"][0], u'Tarjeta', u'USD']
ad[u"Portfolio Personal"] = [uuid.uuid4(), None, u'Inversion', u'ARS']
ad[u"Portfolio pesos"] = [uuid.uuid4(), ad["Portfolio Personal"][0], u'Inversion', u'ARS']
ad[u"Portfolio dolares"] = [uuid.uuid4(), ad["Portfolio Personal"][0], u'Inversion', u'USD']
ad[u"Porfolio dls usa"] = [uuid.uuid4(), ad["Portfolio Personal"][0], u'Inversion', u'USD']
ad[u"Portfolio acciones"] = [uuid.uuid4(), ad["Portfolio Personal"][0], u'Inversion', u'ARS']
ad[u"Portfolio bonos"] = [uuid.uuid4(), ad["Portfolio Personal"][0], u'Inversion', u'ARS']
ad[u"Portfolio lebacs"] = [uuid.uuid4(), ad["Portfolio Personal"][0], u'Inversion', u'ARS']
ad[u"Portfolio letes"] = [uuid.uuid4(), ad["Portfolio Personal"][0], u'Inversion', u'ARS']

acount_table_data = ad

