CHIK & PETS

Este proyecto es una aplicacion de agenda de servicios para mascotas que realizamos en Python

La idea del programa es ayudar a organizar la informacion de los clientes, sus mascotas, los servicios que ofrece el establecimiento y las citas que se van agendando

Para desarrollarlo utilizamos programacion orientada a objetos, creando diferentes clases y funciones que nos permiten manejar la informacion de una forma mas organizada

Que permite hacer el programa:

El programa tiene cuatro partes principales

Clientes: podemos registrar un cliente con su documento, nombre y telefono, consultar los clientes registrados, buscar uno por su identificacion, actualizar su telefono y eliminarlo siempre que no tenga mascotas asociadas

Mascotas: podemos registrar mascotas relacionandolas con un cliente que ya exista, consultar su informacion, buscar las mascotas de un cliente, actualizar su especie o raza y eliminarlas cuando no tengan citas registradas

Servicios: el programa tiene siete servicios que ya vienen definidos, como baño, corte de pelo, limpieza dental, vacunacion y otros, podemos consultar sus precios y cambiar las tarifas siempre que esten dentro de los valores permitidos

Citas: podemos registrar citas seleccionando una mascota, un servicio, una fecha y un horario disponible, tambien podemos consultar las citas, buscar una en especifico y cancelarla cuando sea necesario

Una de las reglas importantes es que no se pueden registrar dos citas activas para la misma fecha y el mismo horario

Cuando se cancela una cita esta no desaparece del programa, queda guardada como parte del historial y el horario vuelve a estar disponible

Como ejecutar el programa

Para utilizar el proyecto necesitamos tener Python instalado en el computador

Podemos abrir la carpeta del proyecto en Visual Studio Code o en otro programa que permita ejecutar archivos de Python

El proyecto tiene dos formas de utilizarse

Si queremos abrir la interfaz grafica ejecutamos el archivo "gui.py", ahi aparecen las ventanas y botones para manejar los clientes, mascotas, servicios y citas

Si queremos utilizar el programa desde la terminal ejecutamos "consola.py", esta version permite realizar las operaciones mediante menus y opciones numericas

Es importante tener todos los archivos del proyecto guardados en la misma carpeta porque unos necesitan importar funciones y clases de otros

Para la interfaz grafica utilizamos Tkinter, que normalmente viene incluido con Python, por eso no necesitamos instalar librerias adicionales

Como organizamos los archivos

"gui.py" contiene la interfaz grafica del programa, es decir las ventanas, botones y espacios donde ingresamos la informacion

"consola.py" contiene los menus que permiten utilizar el programa desde la terminal

"Cliente.py" contiene la clase Cliente, donde se manejan los datos de cada cliente

"Mascota.py" contiene la clase Mascota, donde se guarda la informacion de las mascotas y el cliente al que pertenecen

"Servicio.py" contiene la clase Servicio, donde estan los datos de los servicios y sus tarifas

"Cita.py" contiene la clase Cita, donde se maneja la informacion de cada cita y si esta activa o cancelada

"gestion.py" contiene las funciones que usamos para registrar, buscar, consultar, actualizar y eliminar informacion

"validaciones_y_datos_iniciales.py" contiene funciones de apoyo para validar datos y trabajar con las opciones del programa

"persistencia.py" contiene las funciones encargadas de guardar y cargar la informacion

"datos.json" es el archivo donde se almacenan los clientes, mascotas, servicios y citas

"README.md" es este archivo donde explicamos de manera general como funciona el proyecto

Como se guarda la informacion

Para que los datos no se pierdan cuando cerramos el programa utilizamos un archivo JSON

En nuestro caso usamos "datos.json", donde guardamos la informacion de los clientes, mascotas, servicios y citas en un mismo archivo

En "persistencia.py" tenemos dos funciones principales que son "guardar_datos()" y "cargar_datos()"

La primera permite guardar los cambios que hacemos en el programa y la segunda permite recuperar la informacion cuando volvemos a abrirlo

Por ejemplo si registramos un cliente o una mascota y cerramos el programa, al abrirlo nuevamente podemos encontrar esos datos porque quedaron guardados en el JSON

Tambien se guardan las citas canceladas para conservar el historial

Validaciones del programa

Durante el desarrollo agregamos algunas validaciones para evitar errores al registrar o modificar la informacion

Por ejemplo no se puede registrar un cliente con un documento que ya exista, el telefono debe tener diez numeros y no podemos registrar una mascota si el cliente al que pertenece no esta registrado

Tampoco podemos registrar una cita con una mascota o un servicio que no exista

Los horarios son opciones definidas por el programa y si ya existe una cita activa en una fecha y horario no se permite registrar otra en ese mismo espacio

Los servicios tienen tarifas minimas y maximas, por lo tanto si intentamos colocar un precio fuera del rango el programa no acepta el cambio

Tambien hay restricciones para eliminar registros, por ejemplo no podemos eliminar un cliente que tenga mascotas o una mascota que tenga citas asociadas

Estas validaciones ayudan a que la informacion se mantenga organizada y no se generen registros incorrectos

Pruebas que realizamos

Durante el desarrollo hicimos pruebas para comprobar que las funciones principales trabajaran correctamente

Probamos el registro de clientes y mascotas, las consultas, la actualizacion de telefonos y tarifas, el registro de citas y su cancelacion

Tambien probamos algunos casos incorrectos como registrar identificaciones repetidas, ingresar telefonos invalidos, intentar agendar dos citas en el mismo horario y eliminar registros que tienen informacion relacionada

Otra prueba importante fue guardar los datos en el JSON y volverlos a cargar para comprobar que la informacion no se perdiera

Sobre el proyecto

Trabajamos con clases, objetos, atributos privados, metodos, funciones, listas, validaciones, interfaz grafica y almacenamiento en archivos JSON

El programa esta pensado para manejar una agenda sencilla de servicios para mascotas, por eso no incluye pagos, historias clinicas ni manejo de varios profesionales

Con este proyecto buscamos aplicar los temas vistos en clase y desarrollar una aplicacion que permita realizar operaciones basicas de una manera organizada y facil de utilizar
