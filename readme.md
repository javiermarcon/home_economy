# Economia Casera

Sistema que permita llevar la economía de la casa en forma fácil e intuitiva permitiendo que cada integrante del grupo familiar cargue las transacciones desde su celular sin necesidad de estar conectado y se pueda llevar una economía ordenada tanto de la casa como de los gastos personales de cada uno.

## Características

### Principales

#### Seguridad:
- Usuarios con contraseña estatica o dinamica (que la contraseña incluya calculos con variables como fecha y hora para que cambie cada 5 minutos por ejemplo).
- Que se puedan usar varios patrones de contraseña en forma secuencial o por horarios.
- Que haya un comando para deshabilitar el login hasta el proximo cambio de contraseña.

#### Usabilidad
- Que sea facil de usar para personas sin conocimientos de computación ni de economia.
- Que sea multi-plataforma (Linux, Windows, Android, etc.)
- Que permita sincronizar diferentes dispositivos y mantenga una base de datos en cada terminal.
- Que permita el uso sin estar conectado a internet y al obtener conexión permita sincronizar con las demás terminales.
- Que tenga sistema de plugins para agregar funcionalidades en forma fácil.
- Que permita guardar y transmitir los datos en forma encriptada,
- Que cada transacción permita guardar uno o varios archivos de comprobante.
- Que permita importar y exportar datos en QIF y otros formatos.
- Que tenga backward-compatibility permitiendo la sincronización entre distintas versiones.
- Que tenga un parser de mails para incorporar automaticamente transacciones que se informan por mail (pagos con débito automático, valorización de cartera, acreditación de dividendos, etc).

#### Economia
- Que maneje múltiples monedas y la conversión de las mismas (con o sin comisión).
- Que maneje gastos tanto recurrentes (impuestos x ejemplo) como no recurrentes.
- Que maneje ingresos incluyendo valores futuros (cheque diferido x ejemplo).
- Que maneje transacciones con comisiones fijas y/o variables.
- Que maneje inversiones (bonos, acciones, crowfunding, crowlending,  criptomonedas, metales, etc).
- Que maneje presupuesto de gastos.
- Que tenga un modo "avanzado" que permita calcular y registrar operaciones mas complejas (como swaption por ejemplo).

### Whishlist

- Que permita importar datos de bancos, tarjetas de crédito, brokers, etc.
- Que permita hablarle a la aplicacion con patrones preestablecidos y la aplicacion reconozca la voz y ejecute las ordenes dictadas. Por ejemplo "contraseña 12345 gasté 57 pesos con 40 centavos en una ensalada en chino top para almuerzo deshabilitar login" y (si la contraseña especificada es correcta) que deshabilite el login e ingrese una transaccion nueva con los datos: tipo: gasto, moneda: ARS, importe: 57.40, destinatario: chino top, categoria: almuerzo, descripcion: ensalada. Tambien podria ser por ejemplo "ayer le preste 14 pesos a NN para comprar una coca cola" o "NN me devolvio 14 pesos de lo que me debia".
- Que tenga un anazizador de webs tipo selenium para loguearse en páginas (de bancos, de inversiones, etc.) para actualizar los valores de las inversiones.

## Diseño

Todas las versiones se podrían desarrollar con kivy, que es multiplataforma, y de esa forma me evito que 

Para almacenamiento de datos se puede usar sqlite ya que es compatible tanto con python como con phonegap (usando Cordova-sqlite-storage), permite encriptar y no necesita la instalación de un motor de base de datos separado.
