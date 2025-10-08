README.md debe incluir:
markdown
# [Convertidor de Monedas] - Integración Backend
## Integrantes:
- Izquierdo Quintana Miguel Angel
- Raymundo Rafael, Mirko Josué
- Serrano Pure, Victor Manuel
- Sosa Porras, Jhoan 

## Nueva Funcionalidad:
Se ha integrado un backend usando **Flask** que permite manejar datos de usuarios y preferencias de monedas en la aplicación. Esto significa que ahora los usuarios pueden crear un perfil, guardar su moneda preferida, actualizar sus datos, consultar información y eliminar su perfil directamente desde la aplicación. La integración backend permite que la app sea más interactiva y dinámica, ofreciendo persistencia de datos y comunicación con el servidor de manera confiable y segura.

## Cómo instalar aplicativo:
-Primero, se debe presionar el botón "Windows" en el teclado, al momento de abrirse usted escribe lo siguiente "cmd" y presiona la tecla "ENTER". Eso le abrirá el CMD que le permitirá instalar el FLask.

-Segundo, con el CMD abierto, escribir dentro de este los siguientes comandos sin las comillas dobles : "py -m ensurepip --default-pip", seguido de la tecla ENTER, igualmente el segundo comando "py -m pip install flask" seguido de ENTER, y el ultimo comando "py -m pip install flask-cors", todo esto le permitirá ...(continua comentando tu).

-Tercero, ingresar al siguiente enlace que te dirigira al repositorio donde se encuentran los archivos necesarios para poner la Aplicación del Conversor y el Servidor de este a ejecutarse, sin comillas dobles "https://github.com/Javi1008/ConversordeMonedas_G03". Una vez dentro del repositorio en GITHUB visualizaremos todos los archivos que componen la app, 
posteriormente ubicamos en la parte superior derecha un botón (verde) con el enunciado "<> Code", le damos clik y este mostrara algunas opciones a descargar, presionamos el apartado que dice "DOWLOAD ZIP", esto descargara una carpeta con el nombre "ConversordeMonedas_G03-main.zip" que se guarda en el EXPLORADOR DE ARCHIVOS de la PC.

-Cuarto, presionamos nuevamente la tecla WINDOWS ubicada en el teclado al lado de la tecla "ALT" y escribimos "EXPLORADOR DE ARCHIVOS" seguido de la tecla "ENTER", una vez dentro ubicamos la opción "DESCARGAS" para lograr encontrar nuestra carpeta que descargamos anteriormente, seguido ponemos el cursor del mouse sobre la carpeta recién descargada y le damos "clik derecho", esto abrira una lista de opciones donde ubicaremos la opcion "EXTRAER TODO", hacemos clik a esta opcion y luego se mostrara una interfaz donde solo presionaremos el boton que dice "EXTRAER", una vez se termine de extraer, se mostrara una interfaz con la carpeta ya no zipeada, cerramos esa ventana nueva que se abrio.

-QUINTO, nos dirigimos al "DISCO LOCAL C", que se muestra en el EXPLORADOR DE ARCHIVOS como: "(Windows(C:))". Una vez dentro tenemos que dar clik derecho en un zona que no tenga ningun tipo de archivo ni carpeta, esto mostrara una lista de opciones, ubicamos la opcion "NUEVO", seguido de "CARPETA", esto permitira crear una carpeta a la que colocaremos de nombre "CONVERSOR". Volvemos a la opcion "DESCARGAS" del "EXPLORADOR DE ARCHIVOS" donde extrajimos nuestra carpeta zipeada. DATO:(para saber que la carpeta esta comprimida o no, ubicamos el cursor sobre la carpeta que tiene el nombre "ConversordeMonedas_G03-main" y damos clik derecho, se abrira una lista de opciones donde ubicaremos la opcion "PROPIEDADES", ingresamos en esa opcion y visualizaremos una interfaz donde buscaremos el apartado donde dice "TIPO" y alli se menciona que extensión tiene la carpeta, siendo zip la carpeta que no se encuentra extraída). Ubicamos el cursor encima de la carpeta que ya no se encuentra comprimida, le hacemos un clik y seguido presionamos las teclas ("CNTRL" + "C") esto permitirá copiar la carpeta. Luego nos dirigmos otra vez al apartado de (Windows(C:)) donde pegaremos nuestra carpeta dentro de la carpeta anteriormente creada llamada "CONVERSOR" usando la combinación de teclas ("CNTRL" + "V") seguido damos doble clik sobre nuestra carpeta recién pegada, seguido de otro doble click en la carpeta que se muestra dentro, una vez haciendo esto se podrán visualizar todos los archivos descargados directamente del GITHUB. 

## Cómo ejecutar:
-PRIMERO, continuando con los pasos anteriores, para poder ejecutar la aplicación junto con el servidor tenemos que tener descargado el "SOFTWARE VISUAL STUDIO CODE" (OJO SOLO SI NO TIENES EL SOFTWARE INSTALADO) el cual descargaremos desde el siguiente enlace "https://code.visualstudio.com/download" seguido le damos al botón de Windows dependiendo si se posee WINDOWS o MAC descargar, de tener ya descargado el software ignoramos este punto. Con el software instalado primero le damos click a la tecla "WINDOWS" y escribimos "VISUAL STUDIO" seguido presionamos "ENTER", esto abrirá el SOFTWARE VISUAL STUDIO CODE.

-SEGUNDO, una vez dentro de el software abirmos nuevamente el "EXPLORADOR DE ARCHIVOS" e ingresamos en la carpeta que creamos llamada "CONVERSOR", seguido damos doble clik en la carpeta que se encuentra dentro de esta llamada "ConversordeMonedas_G03-main" esto mostrara otra carpeta llamada de la misma manera, esta carpeta la arrastramos hasta la interface del Visual Studio, no sin antes minimizar un poco el "EXPLORADOR DE ARCHIVOS", una vez hecho este paso aceptamos el mensaje que nos muestra el Visual Studio pulsando el botón azul "YES, I TRUST THE AUTHORS".

-TERCERO, esto subirá de manera automática nuestra carpeta dentro del SOFTWARE podremos visualizar todos los componentes de la APP (app.js/db.json/index.html/server.py/style.css), seguido ubicamos el cursor del mouse encima del que dice "SERVER.PY" y le damos un clik, esto abrirá el código que compone nuestro servidor.
  1. Backend: `cd backend && python app.py`
-CUARTO, una vez abierto nuestro "SERVER.PY" para poner a andar nuestro servidor le damos a la tecla "F5" en el teclado, esto nos mostrara opciones en la parte superior de la ventana del VISUAL STUDIO, seguido de ello le damos a la opción que dice "PYTHON DEBUGGER", asi también seguido le damos a la opción que dice "PYTHON FILE debug the currently active Python file" de manera que si todo esta correcto se inicializara el servidor. En la parte inferior del Visual Studio visualizaremos un mensaje que dice "Servidor Flask ejecutándose correctamente...".

-QUINTO, una vez inicializada el servidor, abrimos el CMD usando la tecla "WINDOWS" donde escribiremos "CMD" que nos abrirá una ventana de comandos donde podremos escribir los comandos para consultar con nuestro servidor. Pero no sin antes verificar cual es nuestra dirección ip escribiendo el comando "ipconfig" en el cmd sin las comillas dobles. Nos mostrara una serie de mensajes donde nos ubicaremos al final y ubicamos el mensaje que dice "Dirección IPv4" y recordamos/guardamos el IP que aparece.

-SEXTO, para poder ingresar las consultas a nuestro servidor le mostrare una serie de comandos que sirven para poder interactuar con este:
  1. Para empezar si queremos "añadir nuevos usuarios" al servidor usamos el comando copiando tal y como se muestra, completando el apartado con la IP guardada anteriormente, y cambiando las diferentes opciones que se muestran como el nombre, correo y prefCurrency que pueden ser (PEN/USD/EUR) : curl -X POST http://(colocar el IP de su compu sin espacios):5000/users -H "Content-Type: application/json" -d "{\"name\":\"Usuario1\",\"email\":\"ejemplo@gmail.com\",\"prefCurrency\":\"PEN\"}"
  2. Asi también podemos "Mostrar todos los usuarios ya creados" usando el comando de la misma manera usando el IP guardado: curl -X GET http://(colocar el IP de su compu sin espacios):5000/users
  3. De la misma manera podemos "Mostrar un usuario por su ID", una vez visualizamos el usuario que queremos mostrar solo copiamos el ID que este posee y lo implementamos el este código, asi mismo no olvidarse de colocar su IP: curl -X GET http://(coloquen su ip de su compu sin espacios):5000/users/(id del usuario sin espacios)
  4.Para poder "Actualizar un usuario" realizamos lo siguiente editando los campos que se requieren actualizar, todo sin olvidarse el IP de la PC que guardamos anteriormente y colocando el ID del usuario a actualizar, con el siguiente comando: curl -X PUT http://(coloquen su ip de su compu sin espacios):5000/users/(id del usuario sin espacios) -H "Content-Type: application/json" -d "{\"name\":\"Carlos P. Actualizado\",\"email\":\"carlos_new@gmail.com\",\"prefCurrency\":\"EUR\"}"
  5. Para terminar podemos "Eliminar un usuario", lo realizmos con el ID del usuario que queremos eliminar y usamos el comando: curl -X DELETE http://(coloquen su ip de su compu sin espacios):5000/users/(id del usuario sin espacios)
     
2. Frontend: Abrir `frontend/index.html` en navegador
   Para poder abrir el fronted de la App dirijase al Visual Studio y deberemos darle un clik al apartado que dice INDEX.HTML seguido de la tecla F5, solo si el servidor esta siendo ejecutado desde el CMD ya que de no hacerlo los datos que estan ya en nuestro servidor de Pyton no cargaran en la App directamente. Con el servidor funcionando desde el CMD inicializamos nuestra APP en el navegador ubicando en la parte de arriba del Visual Studio el apartado que dice "WEB APP CHROME" le damos un clik, y la app se cargara automaticamente desde el navegador.
   
3. Usar la nueva opción de "Perfil" en la app
   Dentro de la app, encontrará una nueva sección llamada Perfil. Aquí podrá crear un usuario, guardar sus datos (nombre, correo y moneda preferida), actualizar su información o consultar los perfiles existentes.
   
## Lista de Endpoints implementados:
Método	Endpoint	Descripción
POST	 /perfil	  Guardar los datos de un usuario nuevo
GET	   /perfil	  Obtener todos los datos guardados de los usuarios

## Describir estructura de carpetas
ConversordeMonedas_G03-main/
│
├── backend/
│   ├── app.py          # Código del servidor Flask
│   └── db.json         # Base de datos simulada en JSON
│
├── frontend/
│   ├── index.html      # Interfaz principal del conversor
│   ├── style.css       # Estilos de la aplicación
│   └── app.js          # Lógica del frontend
└──README.md      # Este documento
