# Economia Casera

Sistema que permita llevar la economía de la casa en forma fácil e intuitiva permitiendo que cada integrante del grupo familiar cargue las transacciones desde su celular sin necesidad de estar conectado y se pueda llevar una economía ordenada tanto de la casa como de los gastos personales de cada uno.

Tambien esta pensado para que la informacion que pueda ser accesible via web o mail se cargue en forma automatica evitandole al usuario el trabajo de cargarla (ahorrandole tiempo y esfuerzo al usuario) y evitando discrepancias x olvidarse de cargar algo.

## Características

### realizadas
Todavia no hay nada hecho que sea usable.

### sprint actual

#### Seguridad:
- Manejo básico de usuarios.

#### Usabilidad

- Que sea facil de usar para personas sin conocimientos de computación ni de economia.
- Que sea multi-plataforma (Linux, Windows, Android, etc.)
- Que permita sincronizar diferentes dispositivos y mantenga una base de datos en cada terminal.
- Que permita el uso sin estar conectado a internet y al obtener conexión permita sincronizar con las demás terminales.
- Que tenga sistema de plugins para agregar funcionalidades en forma fácil.

#### Economia

- Que permita ingresar operaciones básicas como gastos, ingresos simples o transferencias simples
- Que maneje múltiples monedas.

### Sprints futuros

#### Seguridad:
- Usuarios con contraseña estatica o dinamica (que la contraseña incluya calculos con variables como fecha y hora para que cambie cada 5 minutos por ejemplo).
- Que se puedan usar varios patrones de contraseña en forma secuencial o por horarios.
- Que haya un comando para deshabilitar el login hasta el proximo cambio de contraseña.

#### Usabilidad

- Que permita guardar y transmitir los datos en forma encriptada,
- Que cada transacción permita guardar uno o varios archivos de comprobante.
- Que permita importar y exportar datos en QIF y otros formatos de archivos contables.
- Que permita importar datos de bases de datos de otros progrmamas como "money Manager Ex" por ejemplo.
- Que tenga backward-compatibility permitiendo la sincronización entre distintas versiones.
- Que tenga un parser de mails para incorporar automaticamente transacciones que se informan por mail (pagos con débito automático, valorización de cartera, acreditación de dividendos, etc).
- Que permita hablarle a la aplicacion con patrones preestablecidos y la aplicacion reconozca la voz y ejecute las ordenes dictadas. Por ejemplo "contraseña 12345 gasté 57 pesos con 40 centavos en una ensalada en chino top para almuerzo deshabilitar login" y (si la contraseña especificada es correcta) que deshabilite el login e ingrese una transaccion nueva con los datos: tipo: gasto, moneda: ARS, importe: 57.40, destinatario: chino top, categoria: almuerzo, descripcion: ensalada. Tambien podria ser por ejemplo "ayer le preste 14 pesos a NN para comprar una coca cola" o "NN me devolvio 14 pesos de lo que me debia".
- Que tenga un anazizador de webs tipo selenium para loguearse en páginas (de bancos, de inversiones, etc.) para actualizar los valores de las inversiones.
- Que permita guardar backups en forma automatica.
- Que permita usar y guardar plantillas de operaciones.
- Que tenga reglas para definir x horario y monto la plantilla x defecto al iniciar una operacion.
- Que tenga multiples idiomas.
- Que sincronice con Google Calendar los eventos de inversiones (pago cupones y dividendos, finalizacion de inversiones, etc).

#### Economia

- Que maneje múltiples monedas y la conversión de las mismas (con o sin comisión).
- Que maneje gastos tanto recurrentes (impuestos x ejemplo) como no recurrentes.
- Que maneje ingresos incluyendo valores futuros (cheque diferido x ejemplo).
- Que maneje transacciones con comisiones fijas y/o variables.
- Que maneje inversiones (bonos, acciones, crowfunding, crowlending,  criptomonedas, metales, etc).
- Que maneje presupuesto de gastos.
- Que tenga un modo "avanzado" que permita calcular y registrar operaciones mas complejas (como swaption por ejemplo).
- Que calcule algunos impuestos como por ejemplo bienes personales, ingresos brutos, ganancias, etc.
- Que permita importar datos de bancos, tarjetas de crédito, brokers, etc.
- Que tenga cuentas compartidas (gastos de la casa  o supermercados por ejemplo).
- Que maneje prestamos a otras personas.
- Que tenga plugins de consejos financieros (por ejemplo te puede aconsejar cuando comprar o vender divisas o acciones usando estrategias como los promedios de ruedas moviles).

## Diseño y desarrollo

La aplicación se desarrollará en capas utilizando los métodos SCRUM y BDD utilizando el lenguaje Python. Se empaquetará con Kivy para que sea multiplataforma.

La aplicación tendrá distintas partes que interactuarán:
- **Core**: parte central que permitirá hacer los asientos, cálculos que se guarden, lógica de usuarios, manejo de plugins, etc.
- **Sync**: módulo de sincronización y api que permite que interactuar con otras instancias de Home_Economy o con programas externos.
- **GUI**: interfaz gráfica linda para interacuar con la aplicación.
- **Listener**: módulo para interactuar hablando con la aplicación.

### Core

El core se hará con clases de python puro, las cuales serán importadas por los demás módulos.
Para procesamiento de datos se usará pandas y numpy.
Para almacenamiento de datos se utilizará el ORM sqlAlchemy con una base de datos sqlite (tener en cuenta http://cheparev.com/kivy-sqlite/), ya que sqlite es muy liviana, permite encriptar y no necesita la instalación de un motor de base de datos separado. Si la aplicación crece en complejidad puede sustituirse la base de datos por una bd relacional más robusta (como postgresql) o incluso sustituir el diseño para utilizar una base de datos nosql o de grafos. Igualmente al tener una api de comunicación, el cambio sería transparente para los demás módulos.

### Sync

La parte de sync tendrá una api hecha con Tornado, la cual se utilizará tanto para la comunicación con otras instancias de la aplicación como con programas externos. También se prevee que en el futuro permita importar y exportar datos utilizando archivos compartidos por Dropbox, Google Drive, etc. Al sincronizar x http tendra opciones de ingresar ip, utilizar ultima ip conocida y/o buscar host en lan.

### GUI

La gui se desarrollará con kivy, que es multiplataforma, y de esa forma me evito tener 2 aplicaciones distintas (para moviles y para pc). Entre los widgets que se pretende utilizar se encuentran:
- Kivy Datagrid Plugin (https://github.com/namkazt/Kivy-Datagrid-plugin)
- Kivy Garden (https://github.com/kivy-garden)

### Listener

Este módulo utilizará reconocimiento de voz para entender lo que el usuario le dice y así operar con el sistema. Se utilizará para eso la librería CMUSphinx (https://cmusphinx.github.io/) para hacer el reconocmimiento y la librería SpeechRecognition (https://pypi.python.org/pypi/SpeechRecognition) como puente entre el programa y CMUSphinx.

### Plugins

Los plugins tendrán funcionalidades específicas como por ejemplo leer mails, manejar duplicados (por ejemplo si 2 plugins leen info de distintos medios y ponen una misma transacción 2 veces), etc.

### Testing
Se desarrollará tests unitarios en forma de historia y luego se verificará el accuracy y coverage de los tests para  que no quede nada en el tintero. Posiblemente se utilice KivyUnitTests (https://github.com/KeyWeeUsr/KivyUnitTest).