SOFTWARE DE INVENTARIO.

Que contiene?:

1. Pantalla de login

el campo de usuario/correo/celular sirve para loguiarse con cualquiera de los 2
campo contraseña
y autenticador con aplicacion de 2FA.



2. "Menu" componente que habilita opciones segun la pantalla
---------------------------------
|en la "pantalla Principal":	|
---------------------------------
Panel de control
|	(Se divide en 2)
|-Configuración del sistema
|-Configuración Cliente
|-Refrescar
|-Cerrar sesión
|
|-----------------------------------------
|En la "Pantalla Equipo" el menu mostrara |
|-----------------------------------------
|Icono "Ir a pantalla principal"
|icono "+" mas para agregar equipo al inventario
|icono "atras" volver pantalla anterior
|
|----------------------------------------
|En la "pantalla equipo" estará oculto	|
|----------------------------------------



*Para esta parte ayúdame a completar los filtros y opciones que debería de ir según el modal o formulario:*

#####3.Al darle clic en "Panel de control" y luego "Configuración del sistema"#####
Pantalla "Configuración del sistema"

Es una pantalla con estilo galería que contiene unos iconos y sus respectiva etiquetas
Sección configuración Empresa y usuario del sistema
Icono - "Mis Empresas"
Icono - "Mis Sedes"
Icono - "Mis Usuarios"
Icono - "Area"
Icono - "Cargos"

Sección configuración de (GEMINI Dame una idea basado en lo que hay)
Icono - "Estado equipo"
Icono - "Tipo Equipo"
Icono - "Fabricantes"
Icono - "Procesadores"
Icono - "RAM"
Icono - "Almacenamiento"
Icono - "Puertos"
Icono - "Sistema Operativo"
Icono - "Ofimáticas"
Icono - "Antivirus"
Icono - "Aplicaciones"

Sección auditoria:
Esta sección es para crear los iconos con sus respetivas etiquetas que hagan falta para llamar cada log, ya que el sistema no permite eliminar pero si permite, crear, activar/desactivar, editar y esta acciones deben quedar registradas en sus respectivos logs, con nombre del usuario que realizo el cambio, fecha, hora,minuto, que tipo de cambio realizo, el antes y el después

Al darle clic a un icono abrirá su respectivo modal:

##Al dar clic en "Mis Empresas"

Es una galería de cards que muestran:
Campo de texto global que filtra por nit, nombre, filtro de activos/inactivos, botón mas para crear
Cada card muestra una previa:
Razón social (Nombre del cliente)
NIT

Si le doy clic a la card se abre la información donde podre modificar la información

"Formulario Empresa" para crear o editar:
CAMPOS:
NIT
RAZON SOCIAL
DIRECCION
DEPARTAMENTO (combox selet, tabla BD con los departamentos de comlombia)
CIUDAD (combobox selet, tabla con las ciudades de colombia, se filtra de acurdo con el departament, Ejemplo: Departamento valle, Ciudad: Santiago de cali, Jamundí, Palmira, otros)



##Al dar clic en "Mis Sedes"
misma lógica de mis empresas, pero, con sus respectivos filtros

"Formulario Mis Sedes" para crear o editar:
Campos:
NOMBRE SEDE
DIRECCION
DEPARTAMENTO (combox selet, tabla BD con los departamentos de comlombia)
CIUDAD (combobox selet, tabla con las ciudades de colombia, se filtra de acurdo con el departament, Ejemplo: Departamento valle, Ciudad: Santiago de cali, Jamundí, Palmira, otros)
TELEFONO DE LA SEDE

##Al dar clic en "Mis Usuarios":
misma lógica de mis empresas, pero, con sus respectivos filtros
"Formulario Mis Usuarios" para crear o editar:
Nombre
Apellido
SEDE
AREA
CARGO
CORREO
CONTACTO

##Al dar clic en "Areas"
En este caso de areas es solo una lista con su respectivo filtro de búsqueda, filtro inactivo/activo
Al darle clic al la linea de cada área me permite desactivar/activar
no se editan

##Al dar clic en "Cargos"
En este caso de cargos es solo una lista con su respectivo filtro de búsqueda, filtro inactivo/activo
Al darle clic al la linea de cada cargo me permite desactivar/activar
No se editan


##Al dar clic en "Estado equipo"
En este caso de los estado de los equipos es solo una lista con su respectivo filtro de búsqueda, filtro inactivo/activo
Al darle clic al la linea de cada estado me permite desactivar/activar.


##Al dar clic en "Tipo Equipo"
Cumple la misma lógica que "Estado equipo"

##Al dar clic en "Fabricantes"
Cumple la misma lógica que "Estado equipo"

##Al dar clic en "Procesadores"
con sus respectivos filtros, permite desactivar/activar, no permite editar
"Formulario Procesadores" para crear/editar
Marca Procesador
Tipo Procesador
Generación Procesador
Una marca puede tener diferentes tipos. diferentes tipos tienen diferentes generaciones, ejemplo: Intel - core i5 - G13 (Marca - Tipo - Generación)

##Al dar clic en "RAM"
con sus respectivos filtros, permite desactivar/activar, no permite editar
"Formulario RAM" para crear/editar
Tipo RAM
Capacidad RAM
Un tipo de RAM puede tener diferentes capacidades (la capacidad no depende de tipo ni bus) y diferentes buses de datos.ejemplo: DDR4 - 8GB- 3200 (Tipo - capacidad - bus de datos)

##Al dar clic en "Almacenamiento"
con sus respectivos filtros, permite desactivar/activar, no permite editar
"Formulario Almacenamiento" para crear/editar
Tipo Almacenamiento
Capacidad Almacenamiento
hay difrentes tipos de almacenamiento, MECANICO, SSD, M.2
Hay diferente protocolos según el tipo de almacenamiento
Mecanico - SATA
SSD - SATA
M.2 - SATA
M.2 - PCIe
Hay diferentes tamaños/dimensiones
Mecanico - 3.5
Mecanico - 2.5
SSD - solo 2.5
M.2 - 2280
M.2 - 2242
M.2 - 2230
M.2 - 22110
Las capacidades pueden aplicar a cualquiera, no hay necesidad de asignación directa, se crea una tabla con todas las capacidades

##Al dar clic en "Puertos"
Cumple la misma lógica que "Estado equipo"


##Al dar clic en "Sistema Operativo"
Cumple la misma lógica que "Estado equipo"

##Al dar clic en "Ofimáticas"
Cumple la misma lógica que "Estado equipo"

##Al dar clic en "Antivirus"
Cumple la misma lógica que "Estado equipo"

##Al dar clic en "Aplicaciones"
Cumple la misma lógica que "Estado equipo"



#####4.Al darle clic en "Panel de control" y luego "Configuración Cliente"#####
Pantalla "Clientes"
Es una pantalla con estilo galería que contiene unos iconos y sus respectiva etiquetas

Icono - "Clientes"
Icono - "Sede clientes" sedes de los clientes
Icono - "Contacto" son los usuarios de los clientes


Al darle clic a un icono me llevara a su respectiva pantalla o modal:

##Al dar clic en "Clientes"

Es una galería de cards que muestran:
Campo de texto global que filtra por nit, nombre, filtro de activos/inactivos, botón mas para crear
Cada card muestra una previa:
Razón social (Nombre del cliente)
NIT

Si le doy clic a la card se abre la información donde podre modificar la información

Formulario "Clientes":
CAMPOS:
NIT
RAZON SOCIAL
DIRECCION
DEPARTAMENTO (combox selet, tabla BD con los departamentos de comlombia)
CIUDAD (combobox selet, tabla con las ciudades de colombia, se filtra de acurdo con el departament, Ejemplo: Departamento valle, Ciudad: Santiago de cali, Jamundí, Palmira, otros)


##Al dar clic en "Sede Clientes"
Misma

CAMPOS:
NIT
RAZON SOCIAL
DIRECCION
DEPARTAMENTO (combox selet, tabla BD con los departamentos de comlombia)
CIUDAD (combobox selet, tabla con las ciudades de colombia, se filtra de acurdo con el departament, Ejemplo: Departamento valle, Ciudad: Santiago de cali, Jamundí, Palmira, otros)


##Al dar clic en "Contactos"
Misma lógica de "Clientes", pero con sus respectivos filtros

"Formulario Contactos":
Campos:
Nombre (Texto)
Apellido (Texto)
SEDE (Combobox selet, "sede cliente")
AREA (Texto)
CARGO (Texto)
CORREO (Texto validado)
Celular (quemar 57)


5. "Pantalla Principal"
Esta pantalla es una galeria de cards que tiene todos muestra todas la empresas de todos mis clientes, tambien muestra mis empresas. Desde aqui al darle clic a la tarjeta del cliente me redirige hacia la pantalla de Inventario
Esta pantalla contiene un filtro campo de texto global que sirve para filtrar, por: NIT, Razon social, numero de codigo del equipo, nombre del equipo (numero o nombre del equipo lo que hara es mostrar la empresa, se utiliza por filtrado rapido)
La vista previa de cada Card es: Razon Social y nit.
cuando se le da clic a una card, esta me llevara a la "Pantalla Inventario"

6."Pantalla Inventario"
La "Pantalla inventario" muestra la lista de todos los equipo de la empresa seleccionada en "Pantalla Pricipal"
Filtro: Campo de texto para busqueda global por Codigo Equipo, Nombre equipo, numero de serial, Nombre del usuario del equipo, palabra o frase que pueda estar en el historial del equipo, por licencia, (gemini crea mas ideas para este filtro global).

Esta pantalla es una galeria, muestra todas las card, cada card muestra previamente
Codigo equipo
Nombre del equipo
Nombre de la usuaria
Al darle clic a la card me redirigira a la "Pantalla Equipo" en modo solo vista

7. La "pantalla equipo"
Cuando se abre la pantalla sera modo vista, tendra un icono de "Lapiz" para cambiarlo a modo "editable"
Tendra una barra de navegacion con iconos que abren cada ventana:
icono - "Usuario Equipo"
icono - "Equipo"
icono - "Hardware"
icono - "Software"
icono - "Aplicativos"
icono - "Adjuntos"
icono - "Historial"
Todo este conjunto de elementos componen la ficha tecnica y/o Hoja del de vida del equipo

***Al dar clic en "Usuario Equipo"
Me muestra los siguientes campos:

Codigo de equipo (Campo de texto, codigo unico ABC-123, este se escanea con un lector de barras y QR)
Usuario (Campo de texto)
Cargo (Campo de texto)
Area (Campo de texto)
Correo (Campo de texto)
Teléfono (Quemar 57, numero celular eje: 57 310 5555656 o 57 601 592 2721)
Sede (comobobox selet, para filtrar y seleccionar la sede)
Ciudad de la sede (no editable, ya que muestra automaticamente la ciudad de la sede)

***Al dar clic en "Equipo"
CAMPOS:
Estado equipo (combobox selet, filtrar y seleccionar)
Propio (campo selet solo tiene 2 opciones Si/No) si no es propio (No), muestra los campos "Proveedor Alquiler" y "Codigo Alquiler"
Proveedor alquiler (Texto)
Código alquiler (texto)
Tipo Equipo (combobox selet, filtrar y seleccionar)
Fabricantes (combobox selet, filtrar y seleccionar. Si selecciona clon, no solicitara Serial, ni foto serial)
Serial (Campo de texto) al frente de este campo ira una camarita/clip para adjuntar foto del seria (OJO: Si en fabricante se selecciona Clon, entonces, oculta este campo y no solicita la foto)
Modelo (Campo de texto)

***Al dar clic en "Hardware"
**Procesador:
Marca (Combobox selet, filtra y selecciona)
Tipo (Combobox selet, se filtra según la marca seleccionada, y permite filtrar y seleccionar)
Generación (Combobox selet, se filtra según la marca seleccionada, y permite filtrar y seleccionar)

**RAM: (Un equipo puede terner varios eslots de ram)
Tipo (Combobox selet, filtra y selecciona)
Capacidad (Combobox selet, permite filtrar y seleccionar)
Bus de datos (Combobox selet, se filtra según el tipo seleccionado, y permite filtrar y seleccionar)

**Almacenamiento: (Cada equipo puede tener varios slots de almacenamiento)
Tipo (Combobox selet, filtra y selecciona)
Capacidad (Combobox selet, permite filtrar y seleccionar)
Protocolo (Combobox selet, se filtra según el tipo seleccionado, y permite filtrar y seleccionar)
Tamaño/Dimencion (Combobox selet, se filtra según el tipo seleccionado, y permite filtrar y seleccionar)

**Puertos Equipo (Desplegable, filtra y permite seleccionar varias opciones.)

**Monitor:
Serial (campo de texto "Digite el serial o código de alquiler")
Puertos monitor (Desplegable, filtra y permite seleccionar varias opciones. (se pueden seleccionar los mismo que para "Puertos Equipo"))

***Al dar clic en "Software"
Campos:
**Equipo pertenece: (Selet simple Grupo de trabajo / Dominio)
**Nombre Equipo (texto)
**Mantenimiento preventivo (Con un botón "Aplicar". tomara la fecha y hora y la mostrara en un campo de texto no editable. al dar clic en guardar se ira al historial fecha, hora, Nombre del tecnico, cambio "Mantenimiento Preventivo", si **cancela lo cambios no hara nada, no se gurda el hitorial ni nada)
**Sistema operativo (combobox selet, filtrar y seleccionar el sistema)
**Licensia SO (texto)
**Ofimatica (combobox selet, filtrar y seleccionar el sistema) Si selecciona Libre habilitara el campo "Nombre ofimatica" y se ocultara el campo "Licencia Ofimatica".
**Nombre Ofimatica (Texto)
**Licencia Ofimatica (Texto)
**Antivirus (combobox selet, filtrar y seleccionar el sistema)

***Al dar clic en "Aplicativos"
Filtro de texto global, par buscar en la galeria. boton agregar campo para buscar y seleccionar, a medida que selecciono se van a gregando en la parte inferior, en la galeria, tiene boton para vista (Galeria/Listado), boton para crear aplicativos (Formulario Aplicaciones)
Es una pantalla galeria, muestra card. muestra el nombre de aplicativos

***Al dar clic en "Adjuntos"
Boton para añadir archivos o hacer fotos
Vista de galeria, muestra imagenes, archivos word, excel, txt, PDF
Muestra todos los adjuntos

***Al dar clic en "Historial"
Pantalla se visibiliza en forma de card en listado
orden mas reciente primero (Arriba)
Este contiene todos los cambios que se realizaron automaticamente pero tambien tendra un boton para agregar un comentario u observaciones
Cambios que se toman automaticamente:
Ejemplo card:
-----------------------------------------------------------------------------------------
|25/Nov/2025 03:04.12 (hh:mm.ss)				Realizo: Julio Garcia	|
|											|
|Cambio realizado: Se cambio de usuario							|
|Antes: Usuario "ana maria" "Compras"							|
|Despues: "Sandra Garces" "Despachos"							|
-----------------------------------------------------------------------------------------
"Usuario Equipo"
Porcada campo, Cambio realizado de "Campo"
Ejemplo
Cambio realizado de "Usuario"

Asi con todos los campos que corresponde con "Usuario Equipo"
Se aplicaran las misma logica con las demas pantallas o modales y sus campos correspondientes
"Equipo"
"Hardware"
"Software"
"Aplicativos"
"Adjuntos"
El primer comentario (card) que tendra el hortorial sera
la informacion de la creacion del equipo
es decir el equipo no existe, lo creo y adiciono los campos, le doy guardar
el primero comentario seria la fecha y hora y quien creo el equipo

Valida, verifica que no tuve en cuenta, completa la logica, respetando lo que yo quiero hacer, pero las mejoras siempre seran recibidas.
Ten presente validacion de los campos
que se trabajara con complementos reutilizables cuando se pueda

🎨 Colores SIICSA
Blanco (fondo)
#223551 — Azul corporativo
#00A08F — Verde corporativo
#616367 — Gris corporativo