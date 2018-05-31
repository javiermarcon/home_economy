# -*- coding: utf-8 -*-
import uuid

ad = {}

ad[u"Efectivo dolares"] = [unicode(uuid.uuid4()), None, u'Efectivo', u'USD']
ad[u"efectivo encima"] = [uuid.uuid4(), None, u'Efectivo', u'ARS']
ad[u"efectivo esther"] = [uuid.uuid4(), None, u'Efectivo', u'ARS']
ad[u"efectivo guardado"] = [uuid.uuid4(), None, u'Efectivo', u'USD']
ad[u"rz_vacaciones"] = [uuid.uuid4(), None, u'Efectivo', u'BRL']
ad[u"ripio"] = [uuid.uuid4(), None, u'Moneda', u'ARS']
ad[u"ripio pesos"] = [uuid.uuid4(), ad["ripio"][0], u'Moneda', u'ARS']
ad[u"ripio btc"] = [uuid.uuid4(), ad["ripio"][0], u'Moneda', u'BTC']
ad[u"galicia"] = [uuid.uuid4(), None, u'Banco', u'ARS']
ad[u"hsbc"] = [uuid.uuid4(), None, u'Banco', u'ARS']
ad[u"hsbc pesos"] = [uuid.uuid4(), ad["hsbc"][0], u'Banco', u'ARS']
ad[u"hsbc dolares"] = [uuid.uuid4(), ad["hsbc"][0], u'Banco', u'USD']
ad[u"hsbc cc"] = [uuid.uuid4(), ad["hsbc"][0], u'Banco', u'ARS']
ad[u"hsbc visa"] = [uuid.uuid4(), ad["hsbc"][0], u'Tarjeta', u'ARS']
ad[u"hsbc master"] = [uuid.uuid4(), ad["hsbc"][0], u'Tarjeta', u'ARS']
ad[u"hsbc visa usd"] = [uuid.uuid4(), ad["hsbc"][0], u'Tarjeta', u'USD']
ad[u"hsbc master usd"] = [uuid.uuid4(), ad["hsbc"][0], u'Tarjeta', u'USD']
ad[u"tarjeta naranja"] = [uuid.uuid4(), None, u'Tarjeta', u'ARS']
ad[u"naranja visa"] = [uuid.uuid4(), ad["tarjeta naranja"][0], u'Tarjeta', u'ARS']
ad[u"naranja mastercard"] = [uuid.uuid4(), ad["tarjeta naranja"][0], u'Tarjeta', u'ARS']
ad[u"naranja naranja"] = [uuid.uuid4(), ad["tarjeta naranja"][0], u'Tarjeta', u'ARS']
ad[u"naranja usd"] = [uuid.uuid4(), ad["tarjeta naranja"][0], u'Tarjeta', u'USD']
ad[u"portfolio personal"] = [uuid.uuid4(), None, u'Inversion', u'ARS']
ad[u"portfolio pesos"] = [uuid.uuid4(), ad["portfolio personal"][0], u'Inversion', u'ARS']
ad[u"portfolio dolares"] = [uuid.uuid4(), ad["portfolio personal"][0], u'Inversion', u'USD']
ad[u"porfolio dls usa"] = [uuid.uuid4(), ad["portfolio personal"][0], u'Inversion', u'USD']
ad[u"portfolio acciones"] = [uuid.uuid4(), ad["portfolio personal"][0], u'Acciones', u'ARS']
ad[u"portfolio bonos"] = [uuid.uuid4(), ad["portfolio personal"][0], u'Acciones', u'ARS']
ad[u"portfolio lebacs"] = [uuid.uuid4(), ad["portfolio personal"][0], u'Acciones', u'ARS']
ad[u"portfolio letes"] = [uuid.uuid4(), ad["portfolio personal"][0], u'Acciones', u'ARS']

acount_table_data = ad

