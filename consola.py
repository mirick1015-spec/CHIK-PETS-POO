from gestion import mostrar_mascotas,consultar_mascota_por_id,buscar_mascotas_de_cliente,consultar_citas_de_mascota,registrar_mascota,actualizar_datos_mascota,validar_se_puede_eliminar_mascota,ejecutar_eliminacion_mascota,consultar_servicio_por_id,actualizar_tarifa_por_servicio,mostrar_todas_las_citas,mostrar_citas_activas,consultar_citas_por_id,registrar_cita,validacion_cancelar_cita,ejecutar_cancelacion_cita,buscar_mascota_por_id,mostrar_clientes,consultar_cliente_por_id,buscar_mascotas_de_cliente,registrar_cliente,actualizar_telefono_cliente,validar_se_puede_eliminar_cliente,ejecutar_eliminacion_cliente,buscar_cliente_por_id

from validaciones_y_datos_iniciales import leer_id,leer_texto_no_vacio,seleccionar_especie,seleccionar_raza,leer_confirmacion,leer_numero_entero_positivo,seleccionar_fecha,seleccionar_franja,leer_entero_en_rango
from persistencia import cargar_datos, guardar_datos
import os









def _guardar_si_corresponde(guardar):
    if guardar is not None:
        guardar()

#Limpiar pantalla, muestra la información actual.
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

#======================GESTION CLIENTES====================

def imprimir_resultado(resultado):
    exito, contenido = resultado

    if isinstance(contenido, list):
        for informacion in contenido:
            print()
            print(informacion)
    else:
        print(contenido)


def consola_mostrar_clientes(clientes):
    resultado = mostrar_clientes(clientes)
    imprimir_resultado(resultado)


def consola_buscar_cliente(clientes):
    id_buscado = leer_id("Ingrese el ID del cliente: ")
    resultado = consultar_cliente_por_id(clientes, id_buscado)
    imprimir_resultado(resultado)


def consola_consultar_mascotas_cliente(clientes, mascotas):
    id_buscado = leer_id("Ingrese el ID del cliente: ")

    # Esta función ya esta en gestion.py y se reutiliza
    resultado = buscar_mascotas_de_cliente(mascotas, id_buscado, clientes)
    imprimir_resultado(resultado)


def consola_registrar_cliente(clientes):
    print("\n--- REGISTRAR CLIENTE ---")

    id_cliente = leer_id("Ingrese el ID del cliente: ")
    nom_cliente = input("Ingrese el nombre del cliente: ").strip()
    telefono = input("Ingrese el teléfono del cliente: ").strip()

    resultado = registrar_cliente(
        clientes,
        id_cliente,
        nom_cliente,
        telefono
    )

    imprimir_resultado(resultado)


def consola_actualizar_telefono_cliente(clientes):
    print("\n--- ACTUALIZAR TELÉFONO ---")

    id_buscado = leer_id("Ingrese el ID del cliente.")
    nuevo_tel = input("Ingrese el nuevo teléfono: ").strip()

    resultado = actualizar_telefono_cliente(
        clientes,
        id_buscado,
        nuevo_tel
    )

    imprimir_resultado(resultado)


def consola_eliminar_cliente(clientes, mascotas):
    print("\n--- ELIMINAR CLIENTE ---")

    id_buscado = leer_id("Ingrese el ID del cliente: ")

    se_puede_eliminar, mensaje = validar_se_puede_eliminar_cliente(
        clientes,
        id_buscado,
        mascotas
    )

    print(mensaje)

    if not se_puede_eliminar:
        return

    confirmacion = leer_confirmacion("¿Desea realizar la eliminación del cliente? s/n: ")
    if confirmacion :
        resultado = ejecutar_eliminacion_cliente(clientes, id_buscado)
        imprimir_resultado(resultado)
    else:
        print("La eliminación fue cancelada. No se realizó ningún cambio.")


#=====================GESTION MASCOTAS-CONSOLA=============

def consola_mostrar_mascotas(mascotas):
    
    bool,datos = mostrar_mascotas(mascotas)
    
    if bool == False:
        print(datos)
        return
    
    print("-------------INFORMACION MASCOTAS-------------")
    for dato in datos:
        print(dato)
        
def consola_buscar_mascota_por_id(mascotas):
    
    id_buscado = leer_id("Ingrese el ID de la mascota: ")
    bool,datos = consultar_mascota_por_id(mascotas,id_buscado)
    
    if bool == False:
        print(datos)
        return
    print("----------INFORMACIÓN DE LA MASCOTA----------")
    print(datos)
    
def consola_buscar_mascotas_por_cliente(mascotas,clientes):
    
    id_buscado = leer_id("Ingrese el ID del cliente: ")
    bool,datos = buscar_mascotas_de_cliente(mascotas,id_buscado,clientes)
    
    if bool == False:
        print(datos)
        return
    
    print("-------------INFORMACIÓN DE MASCOTA/S DEL CLIENTE---------")
    for dato in datos:
        print(dato)
    
def consola_consultar_citas_de_mascota(citas,mascotas):
    
    id_buscado = leer_id("Ingrese el ID de la mascota: ")
    bool,datos = consultar_citas_de_mascota(citas,mascotas,id_buscado)
    
    if bool == False:
        print(datos)
        return
    print("-------------------------CITAS DE LA MASCOTA------------------")
    for dato in datos:
        print(dato)

def consola_registrar_mascota(mascotas,clientes):
    
    id_dueño = leer_id("Ingrese el ID del dueño de la mascota: ")
    nombre = leer_texto_no_vacio("Ingrese el nombre de la Mascota: ")
    especie = seleccionar_especie()
    raza = seleccionar_raza(especie)
    
    bool,datos = registrar_mascota(mascotas,clientes,nombre,especie,raza,id_dueño)
    
    print(datos)

def consola_actualizar_datos_mascota(mascotas):
    
    id_buscado = leer_id("Ingrese el ID de la mascota: ")
    nueva_especie = seleccionar_especie()
    nueva_raza = seleccionar_raza(nueva_especie)
    
    bool,datos = actualizar_datos_mascota(mascotas,id_buscado,nueva_especie,nueva_raza)
    
    if bool == False:
        print(datos)
        return
    
    print(datos)
    mascota = buscar_mascota_por_id(mascotas,id_buscado)
    print(f"Información actualizada: {mascota.obtener_especie()} | {mascota.obtener_raza()}")
        
        
            
def consola_eliminar_mascota(mascotas,citas):
    
    id_buscado = leer_id("Ingrese el ID  de la mascota: ")
    bool,datos = validar_se_puede_eliminar_mascota(mascotas,id_buscado,citas)
    
    if bool == False:
        print(datos)
        return
    
    confirmacion = leer_confirmacion(f"¿Desea realizar la eliminacion de la mascota {id_buscado}? s/n: ")
    
    if confirmacion:
        bool,datos = ejecutar_eliminacion_mascota(mascotas,id_buscado)
        print(datos)
    else:
        print("No se realizo la eliminación de la mascota.")
    
#===================FUNCIONES GESTION DE SERVICIOS================

def consola_mostrar_servicios(servicios):
    if not servicios:
        print("No hay servicios predefinidos disponibles.")
        return

    print("ID      SERVICIO                                PRECIO (COP)")
    print("-" * 68)
    for servicio in servicios:
        precio = f"${servicio.obtener_tarifa():,}".replace(",", ".")
        minimo = f"${servicio.obtener_tarifa_min():,}".replace(",", ".")
        maximo = f"${servicio.obtener_tarifa_max():,}".replace(",", ".")
        print(
            f"{servicio.obtener_id():<7} "
            f"{servicio.obtener_nombre():<40} "
            f"{precio:>13} (rango: {minimo} - {maximo})"
        )
        
def consola_buscar_servicios_por_id(servicios):
    
    id_buscado = leer_id("Ingrese el ID del servicio: ")
    bool,datos = consultar_servicio_por_id(servicios,id_buscado)
    if bool == False:
        print(datos)
        return
    print("===========INFOMACIÓN SERVICIO======")
    print (datos)

def consola_modificar_servicio_por_id(servicios):
    
    print("-----------TARIFAS ACTUALES-----------")
    for servicio in servicios:
        print(
            f"{servicio.obtener_id()} | {servicio.obtener_nombre()} | "
            f"${servicio.obtener_tarifa():,} COP | "
            f"Rango permitido: ${servicio.obtener_tarifa_min():,} - "
            f"${servicio.obtener_tarifa_max():,} COP".replace(",", ".")
        )
    print("")
    print("----------------------------------------")
    id_buscado = leer_id("Ingrese el ID del servicio que desea actualizar: ")
    tarifa_nueva = leer_numero_entero_positivo("Ingrese una tarifa válida: ")
    bool,datos = actualizar_tarifa_por_servicio(servicios,tarifa_nueva,id_buscado)

    if bool == False:
        print(datos)
        return
    print(datos)
    print("")
    print("DATOS ACTUALIZADOS: ")
    bool,info_actualizada = consultar_servicio_por_id(servicios,id_buscado)
    print(info_actualizada)
    
#============ FUNCIONES GESTION CITAS - CONSOLA ==================
    
def consola_mostrar_todas_las_citas (citas):
    
    bool,datos = mostrar_todas_las_citas(citas)
    
    if bool == False:
        print(datos)
        return
    
    print("=========INFORMACIÓN CITAS==========")
    print("")
    for dato in datos:
        print(dato)
    
def consola_mostrar_citas_activas(citas):
    
    bool,datos = mostrar_citas_activas(citas)
    
    if bool == False:
        print(datos)
        return
    print("==========INFORMACIÓN CITAS ACTIVAS============")
    print("")
    for dato in datos:
        print(dato)
    
def consola_mostrar_cita_por_id(citas):
    
    id_buscado = leer_id("Ingrese el ID de la cita: ")
    bool,datos = consultar_citas_por_id(citas,id_buscado)
    
    if bool == False:
        print(datos)
        return
    
    print("===========INFORMACIÓN DE LA CITA===========")
    print("")
    print(datos)

def consola_registrar_cita (citas,mascotas,servicios):
    
    id_mascota = leer_id("Ingrese el ID de la mascota a la que desea realizar su cita: ")
    id_servicio = leer_id("Ingrese el ID del servicio: ")
    fecha = seleccionar_fecha()
    franja = seleccionar_franja()
    
    bool,datos = registrar_cita(citas,id_mascota,id_servicio,mascotas,servicios,fecha,franja)
    
    if bool == False:
        print(datos)
        return
    
    print(datos)
    
def consola_cancelar_cita(citas):
    
    id_buscado = leer_id("Ingrese el ID de la cita que desea cancelar: ")
    
    bool,datos = validacion_cancelar_cita(citas,id_buscado)
    
    if bool == False:
        print(datos)
        return
    
    confirmacion = leer_confirmacion(f"¿Desea realizar la cancelación de la cita con ID: {id_buscado}. s/n : ")
    
    if confirmacion:
        bool,datos = ejecutar_cancelacion_cita(citas,id_buscado)
        print(datos)
    else:
        print("No se realizo la cancelación de la cita.")
    
#================MENUS==================

#Menú mascotas
def menu_mascotas(mascotas,citas,clientes,guardar=None):
    
    limpiar_pantalla()
    while True:
        
        print("============MENÚ MASCOTAS==========")
        print("")
        print("""
            1. Mostrar todas las mascotas
            2. Buscar mascota por ID
            3. Buscar mascotas por cliente (dueño)
            4. Consultar las citas de una mascota
            5. Registrar Mascota
            6. Eliminar mascota
            7. Actualizar especie y raza. 
            0. Volver al menú principal""")
        print("")

        opcion = leer_entero_en_rango("Ingrese una opción: ",0,7)
        print("")
        
        if opcion == 1:
            consola_mostrar_mascotas(mascotas)
        elif opcion == 2:
            consola_buscar_mascota_por_id(mascotas)
        elif opcion == 3:
            consola_buscar_mascotas_por_cliente(mascotas,clientes)
        elif opcion == 4:
            consola_consultar_citas_de_mascota(citas,mascotas)
        elif opcion == 5:
            consola_registrar_mascota(mascotas,clientes)
            _guardar_si_corresponde(guardar)
        elif opcion == 6:
            consola_eliminar_mascota(mascotas,citas)
            _guardar_si_corresponde(guardar)
        elif opcion == 7:
            consola_actualizar_datos_mascota(mascotas)
            _guardar_si_corresponde(guardar)
        else:
            print("Saliendo del menú de mascotas...")
            limpiar_pantalla()
            break

        
#Menú servicios
def menu_servicios(servicios,guardar=None):
    limpiar_pantalla()
    while True:
        
        print("===========MENÚ SERVICIOS=======")
        print("")
        print("""
            1. Mostrar todos los servicios.
            2. Buscar servicios por ID.
            3. Actualizar tarifa.
            0. Volver al menú principal.""")
        print("")
        
        opcion = leer_entero_en_rango("Ingrese una opción: ",0,3)
        print("")
        if opcion == 1:
            consola_mostrar_servicios(servicios)
        elif opcion == 2:
            consola_buscar_servicios_por_id(servicios)
        elif opcion == 3:
            consola_modificar_servicio_por_id(servicios)
            _guardar_si_corresponde(guardar)
        else:
            print("Saliendo del menú de servicios...")
            limpiar_pantalla()
            break 
        
        
#Menú citas

def menu_citas(citas,servicios,mascotas,guardar=None):
    limpiar_pantalla()
    while True:
        
        print("===========MENÚ CITAS=======")
        print("")
        print("""
            1. Mostrar todos las citas.
            2. Mostrar citas activas.
            3. Buscar cita por ID.
            4. Consultar citas de una mascota.
            5. Registrar una cita.
            6. Cancelar una cita.
            0. Volver al menú principal.""")
        print("")
        opcion = leer_entero_en_rango("Ingrese una opción: ",0,6)
        print("")
        if opcion == 1:
            consola_mostrar_todas_las_citas(citas)
        elif opcion == 2:
            consola_mostrar_citas_activas(citas)
        elif opcion == 3:
            consola_mostrar_cita_por_id(citas)
        elif opcion == 4:
            consola_consultar_citas_de_mascota(citas,mascotas)
        elif opcion == 5:
            consola_registrar_cita(citas,mascotas,servicios)
            _guardar_si_corresponde(guardar)
        elif opcion == 6:
            consola_cancelar_cita(citas)
            _guardar_si_corresponde(guardar)
        else:
            print("Saliendo del menú de citas...")
            limpiar_pantalla()
            break
        
def menu_clientes(clientes, mascotas, guardar=None):
    while True:
        limpiar_pantalla()
        print("\n========== GESTIÓN DE CLIENTES ==========")
        print("1. Mostrar todos los clientes")
        print("2. Buscar cliente por ID")
        print("3. Consultar mascotas de un cliente")
        print("4. Registrar cliente")
        print("5. Actualizar teléfono de un cliente")
        print("6. Eliminar cliente")
        print("0. Volver al menú principal")

        opcion = leer_entero_en_rango("Seleccione una opción: ", 0, 6)

        if opcion == 1:
            consola_mostrar_clientes(clientes)
            input("\nPresione Enter para continuar...")

        elif opcion == 2:
            consola_buscar_cliente(clientes)
            input("\nPresione Enter para continuar...")

        elif opcion == 3:
            consola_consultar_mascotas_cliente(clientes, mascotas)
            input("\nPresione Enter para continuar...")

        elif opcion == 4:
            consola_registrar_cliente(clientes)
            _guardar_si_corresponde(guardar)
            input("\nPresione Enter para continuar...")

        elif opcion == 5:
            consola_actualizar_telefono_cliente(clientes)
            _guardar_si_corresponde(guardar)
            input("\nPresione Enter para continuar...")

        elif opcion == 6:
            consola_eliminar_cliente(clientes, mascotas)
            _guardar_si_corresponde(guardar)
            input("\nPresione Enter para continuar...")

        elif opcion == 0:
            print("Saliendo del sistema....")
            limpiar_pantalla()
            break
        
#DATOS INICIALES
#Menú principal
def main():
    
    try:
        clientes, mascotas, servicios, citas = cargar_datos()
    except (OSError, ValueError, KeyError) as error:
        print(f"No se pudo leer datos.json: {error}")
        return
    guardar_datos(clientes, mascotas, servicios, citas)

    def guardar_cambios():
        guardar_datos(clientes, mascotas, servicios, citas)

    limpiar_pantalla()
    while True:
        
        print(f"\n====================================")
        print(f"        CHIK & PETS      ")
        print(f"====================================")
        print(f"1. Gestion Cliente")
        print(f"2. Gestión de mascotas")
        print(f"3. Gestión de servicios")
        print(f"4. Gestión de citas")
        print(f"0. Salir")
        print("")
        opcion = leer_entero_en_rango("Ingrese una opción: ",0,4)
        print("")
        
        if opcion == 1:
            menu_clientes(clientes,mascotas,guardar_cambios)
        elif opcion == 2:
            menu_mascotas(mascotas,citas,clientes,guardar_cambios)
        elif opcion == 3:
            menu_servicios(servicios,guardar_cambios)
        elif opcion == 4:
            menu_citas(citas,servicios,mascotas,guardar_cambios)
        else:
            print(f"Gracias por utilizar el sistema de CHIK & PETS.")
            limpiar_pantalla()
            break
        
    
        
if __name__ == "__main__":
    main()

    

        
        
    



    
    

    
        
    
    
    
        


        