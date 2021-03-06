# -*- coding: utf-8 -*-
import uuid

ad = {}

ad[u"Ingresos"] = [uuid.uuid4(), None, 0]
ad[u"Sueldos"] = [uuid.uuid4(), ad[u"Ingresos"][0], 0]
ad[u"Honorarios"] = [uuid.uuid4(), ad[u"Ingresos"][0], 0]
ad[u"Dividendos"] = [uuid.uuid4(), ad[u"Ingresos"][0], 0]
ad[u"Intereses"] = [uuid.uuid4(), ad[u"Ingresos"][0], 0]
ad[u"Ventas Esther"] = [uuid.uuid4(), ad[u"Ingresos"][0], 0]
ad[u"alquileres"] = [uuid.uuid4(), ad[u"Ingresos"][0], 0]
ad[u"Comisiones"] = [uuid.uuid4(), ad[u"Ingresos"][0], 0]
ad[u"Otros Ingresos"] = [uuid.uuid4(), ad[u"Ingresos"][0], 0]
ad[u"Egresos Comunes"] = [uuid.uuid4(), None, 0]
ad[u"Supervivencia"] = [uuid.uuid4(), ad[u"Egresos Comunes"][0], 0]
ad[u"Supermercado"] = [uuid.uuid4(), ad[u"Supervivencia"][0], 0]
ad[u"Inversiones"] = [uuid.uuid4(), ad[u"Supervivencia"][0], 0]
ad[u"Farmacia"] = [uuid.uuid4(), ad[u"Supervivencia"][0], 0]
ad[u"Comida Trabajo"] = [uuid.uuid4(), ad[u"Supervivencia"][0], 0]
ad[u"otros gastos supervivencia"] = [uuid.uuid4(), ad[u"Supervivencia"][0], 0]
ad[u"Impuestos"] = [uuid.uuid4(), ad[u"Egresos Comunes"][0], 0]
ad[u"Ganancias"] = [uuid.uuid4(), ad[u"Impuestos"][0], 0]
ad[u"Ingresos Brutos"] = [uuid.uuid4(), ad[u"Impuestos"][0], 0]
ad[u"Inmobiliario"] = [uuid.uuid4(), ad[u"Impuestos"][0], 0]
ad[u"Municipal"] = [uuid.uuid4(), ad[u"Impuestos"][0], 0]
ad[u"Otros Impuestos"] = [uuid.uuid4(), ad[u"Impuestos"][0], 0]
ad[u"Proveedores"] = [uuid.uuid4(), ad[u"Egresos Comunes"][0], 0]
ad[u"Compras Feria"] = [uuid.uuid4(), ad[u"Proveedores"][0], 0]
ad[u"Otros"] = [uuid.uuid4(), ad[u"Proveedores"][0], 0]
ad[u"Seguros"] = [uuid.uuid4(), ad[u"Egresos Comunes"][0], 0]
ad[u"Seguro Auto"] = [uuid.uuid4(), ad[u"Seguros"][0], 0]
ad[u"Otro Seguro"] = [uuid.uuid4(), ad[u"Seguros"][0], 0]
ad[u"Créditos"] = [uuid.uuid4(), ad[u"Egresos Comunes"][0], 0]
ad[u"Cuotas Auto"] = [uuid.uuid4(), ad[u"Créditos"][0], 0]
ad[u"Otros creditos"] = [uuid.uuid4(), ad[u"Créditos"][0], 0]
ad[u"Servicios"] = [uuid.uuid4(), ad[u"Egresos Comunes"][0], 0]
ad[u"Gas"] = [uuid.uuid4(), ad[u"Servicios"][0], 0]
ad[u"Agua"] = [uuid.uuid4(), ad[u"Servicios"][0], 0]
ad[u"Electricidad"] = [uuid.uuid4(), ad[u"Servicios"][0], 0]
ad[u"Teléfono"] = [uuid.uuid4(), ad[u"Servicios"][0], 0]
ad[u"Celular"] = [uuid.uuid4(), ad[u"Teléfono"][0], 0]
ad[u"Internet / TV"] = [uuid.uuid4(), ad[u"Servicios"][0], 0]
ad[u"Contador"] = [uuid.uuid4(), ad[u"Servicios"], 0]
ad[u"Otros servicios"] = [uuid.uuid4(), ad[u"Servicios"][0], 0]
ad[u"Gastos médicos"] = [uuid.uuid4(), ad[u"Egresos Comunes"][0], 0]
ad[u"Obra social"] = [uuid.uuid4(), ad[u"Gastos médicos"][0], 0]
ad[u"Remedios"] = [uuid.uuid4(), ad[u"Gastos médicos"][0], 0]
ad[u"Tratamientos"] = [uuid.uuid4(), ad[u"Gastos médicos"][0], 0]
ad[u"Otros gastos medicos"] = [uuid.uuid4(), ad[u"Gastos médicos"][0], 0]
ad[u"Auto"] = [uuid.uuid4(), ad[u"Egresos Comunes"][0], 0]
ad[u"Nafta"] = [uuid.uuid4(), ad[u"Auto"][0], 0]
ad[u"Service / Repuestos"] = [uuid.uuid4(), ad[u"Auto"][0], 0]
ad[u"Taller"] = [uuid.uuid4(), ad[u"Auto"][0], 0]
ad[u"Peaje"] = [uuid.uuid4(), ad[u"Auto"][0], 0]
ad[u"Multas"] = [uuid.uuid4(), ad[u"Auto"][0], 0]
ad[u"Otros gastos Auto"] = [uuid.uuid4(), ad[u"Auto"][0], 0]
ad[u"Hogar"] = [uuid.uuid4(), ad[u"Egresos Comunes"][0], 0]
ad[u"Reformas"] = [uuid.uuid4(), ad[u"Hogar"][0], 0]
ad[u"Otros gastos hogar"] = [uuid.uuid4(), ad[u"Hogar"][0], 0]
ad[u"Ropa"] = [uuid.uuid4(), ad[u"Egresos Comunes"][0], 0]
ad[u"Regalos"] = [uuid.uuid4(), ad[u"Egresos Comunes"][0], 0]
ad[u"Educación"] = [uuid.uuid4(), ad[u"Egresos Comunes"][0], 0]
ad[u"Entretenimiento"] = [uuid.uuid4(), ad[u"Egresos Comunes"][0], 0]
ad[u"Peluqueria"] = [uuid.uuid4(), ad[u"Egresos Comunes"][0], 0]
ad[u"Útiles"] = [uuid.uuid4(), ad[u"Educación"][0], 0]
ad[u"Libros"] = [uuid.uuid4(), ad[u"Educación"][0], 0]
ad[u"Universidad"] = [uuid.uuid4(), ad[u"Educación"][0], 0]
ad[u"Colegio"] = [uuid.uuid4(), ad[u"Educación"][0], 0]
ad[u"Otros"] = [uuid.uuid4(), ad[u"Educación"][0], 0]
ad[u"Cine / Teatro"] = [uuid.uuid4(), ad[u"Entretenimiento"][0], 0]
ad[u"Salir a comer"] = [uuid.uuid4(), ad[u"Entretenimiento"][0], 0]
ad[u"Hobbies"] = [uuid.uuid4(), ad[u"Entretenimiento"][0], 0]
ad[u"Otros entretenimientos"] = [uuid.uuid4(), ad[u"Entretenimiento"][0], 0]
ad[u"Gastos no categorizados"] = [uuid.uuid4(), ad[u"Egresos Comunes"][0], 0]

category_table_data = ad