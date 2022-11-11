# Ejemplo middleware Neuraan
En este tutorial verás como configurar un middleware para acceder a los servicios de Neuraan

## Roadmap
1. Configura tu proyecto
2. Crea tu bot
3. Configura tu base de conocimientos
4. Configura tu RAN Machine
5. Inicializa tu API

## Configuración del proyecto
Para poder configurar el proyecto, necesitarás una cuenta de Neuraan. Si no cuentas con una, crea una [aquí](https://panel.neuraan.com/es/user/signup). Una vez creada tu cuenta y confirmada tu dirección de email (si tienes duda sobre como crear tu cuenta, puedes ver los pasos [aquí](https://docs.neuraan.com/guide/01-creacion-de-la-cuenta.html)), realiza los siguientes pasos:

### Crea el proyecto
En ésta sección se describen los pasos para crear el proyecto con el cual trabajaremos. Si quieres ver a detalle los pasos puedes consutarlos [aquí](https://docs.neuraan.com/guide/02-creacion-del-proyecto.html)
1. Inicia sesión [aquí](https://panel.neuraan.com/es/session/signin)
2. Da click en el botón crear proyecto
3. Proporciona un nombre para el proyecto
4. Marca la casilla habilitar disponibilidad del proyecto
5. Da click en guardar.

### Agrega los servicios
En está sección se agregarán dos servicios: Detección de entidades nombradas especiales y Creador de asistentes virtuales. Si quieres saber más sobre los diferentes servicios ofrecidos por la API, puedes consultar maś información [aquí](https://docs.neuraan.com/services/). Si quieres ver una guía detallada de la [configuración](https://docs.neuraan.com/guide/04-configuracion-de-los-servicios.html) e [invocación](https://docs.neuraan.com/guide/05-invocacion-de-los-servicios.html) de los servicios en los enlaces proporcionados.

1. Da click en el proyecto que acabas de crear
2. Da click en el botón agregar servicio
3. Selecciona el servicio ``Detección de entidades nombradas especiales``
4. Proporciona un nombre para el servicio (por ejemplo: Custom NER)
5. Define un límite de consultas a 100

Verás que el servicio ha sido agregado al proyecto. Este servicio te permitirá consultar las entidades nombradas especiales. A continuación vamos a configurar el servicio de asistentes virtuales.

6. Da click en el botón de agregat servicio
7. Selecciona el servicio ``Creador de asistentes virtuales``
8. Selecciona un nombre para el servicio (por ejemplo: Bot de prueba)
9. Define el límite de consultas a 100

## Crea tu bot
En está sección se mostrarán los pasos para crear un bot.
1. Da click en el ícono del bot en el servicio de creador de asistentes virtuales.
2. Define un nombre para el bot (por ejemplo: Bot tutorial)

## Configura tu base de conocimientos
Las bases de conocimientos proporcionan los ejemplos de intents y entities necesarios para detectar tópicos en tus aplicaciones. Existen 2 tipos de bases de conocimientos, la de servicios y la de bot. Cada una de ellas tiene la misma estructura. Puedes ver más acerca de la configuración de la base de conocimientos [aquí](https://docs.neuraan.com/guide/03-configuracion-de-la-base-de-conocimientos.html)

Para este ejemplo usaremos una base de conocimientos que tiene información de códigos postales y negocios para realizar la configuración.
Configura la base de conocimientos de los servicios:

1. Da click en servicios 
2. Da click en NLU
3. Copia el contenido de knowledge_base.json en el editor 
4. Da click en guardar

Ahora configuraremos la misma base de conocimientos en el asistente virtual:

1. Da click en servicios
2. Da click en el ícono del bot en el servicio de creador de asistentes virtuales
3. Da click en NLU
4. Copia el contenido de knowledge_base.json en el editor
5. Da click en guardar

## Configura tu RAN machine
Este proceso se realiza desde el aisstenete virtual, si no lo encuentras da click en servicios y posteriormente en el ícono del bot en el servicio de creador de asistentes virtuales.

1. Da click en RAN
2. Copia el contenido de ran_machine.json en el editor
3. Da click en guardar

## Inicializa tu API
Para inicializar el API usaremos ngrok y para generar una url pública al puerto 5000 de nuestra API es necesario proporcionar la key de la API de servicios.

1. Abre el archivo middleware > api.py
2. Reemplaza el valor de la variable ``API_KEY`` por el valor obtenido en el servicio de Custom NER y guarda el archivo. **Nota:** Si no encuentras el api-key, navega a servicios, da click en el ícono que muestra el snippet de código (</>) y ubica la cabecera ``Àuthorization`` el valor posterior a ``Bearer`` es tu api key.
3. Inicializa tu API ejecutando el comando: ``python app.py`` desde la carpeta middleware
4. Inicializa Ngrok ejecutando el comando ``ngrok http 5000``
5. Prueba la API, accede desde el navegador a la dirección de ngrok y añade la ruta ``/hello``. **Nota:** Deberías ver Hello, World!! en tu nevegador
6. Actualiza el endpoint de la API en la Ran machine, usando el editor busca las ocurrencias de la dirección https://3755-2806-10b7-3-9a3d-8dda-9404-6978-7a36.ngrok.io y cámbialas por la url asignada por ngrok.
7. Da click en el botón guardar

## Prueba la app
En el asistente da click al botón probar y usa el siguiente flujo:

User: Hola
Bot: ¿Qué negocio deseas consultar?
User: Un gimnasio
Bot: Detecté que quieres consultar NEGOCIO_GIMNASIO, ¿Cuál es el código postal que quieres consultar?
User: el de Monterrey Centro
Bot: En el código postal 64000 hay 68 NEGOCIO_GIMNASIO


## ¿Qué sigue?
Adapta la RAN machine a tus necesidades, así como la base de conocimientos. Pueedes usar está estructura para generar flujos conversacionales complejos que te permitan extraer información a medida que platicas con tus usuarios.

Happy Coding!!