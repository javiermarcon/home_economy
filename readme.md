# Economia Casera

Sistema que permita llevar la economía de la casa en forma fácil e intuitiva permitiendo que cada integrante del grupo familiar cargue las transacciones desde su celular sin necesidad de estar conectado y se pueda llevar una economía ordenada tanto de la casa como de los gastos personales de cada uno.

## Características

### Principales

- Que sea multi-plataforma (Linux, Windows, Android, etc.)
- Que permita sincronizar diferentes dispositivos y mantenga una base de datos en cada terminal.
- Que permita el uso sin estar conectado a internet y al obtener conexión permita sincronizar con las demás terminales.
- Que tenga sistema de plugins para agregar funcionalidades en forma fácil.
- Que permita guardar y transmitir los datos en forma encriptada,
- Que maneje múltiples monedas y la conversión de las mismas (con o sin comisión).
- Que maneje gastos tanto recurrentes (impuestos x ejemplo) como no recurrentes.
- Que maneje ingresos incluyendo valores futuros (cheque diferido x ejemplo).
- Que maneje transacciones con comisiones fijas y/o variables
- Que maneje inversiones (bonos, acciones, crowfunding, crowlending,  criptomonedas, metales, etc).
- Que cada transacción permita guardar uno o varios archivos de comprobante.
- Que permita importar y exportar datos en QIF y otros formatos.

### Whishlist

- Que permita importar datos de bancos, tarjetas de crédito, brokers, etc.

## Diseño

Las versiones para Linux y Windows se harían en Python con Django, y las versiones para IOS y Android se harían en javascript/html/css con cordova/phonegap.

Para almacenamiento de datos se puede usar sqlite ya que es compatible tanto con python como con phonegap (usando Cordova-sqlite-storage), permite encriptar y no necesita la instalación de un motor de base de datos separado.