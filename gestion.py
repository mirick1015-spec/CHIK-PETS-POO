from Mascota import Mascota
from Cita import Cita
from Cliente import Cliente
from validaciones_y_datos_iniciales import combinacion_valida
#===============FUNCIONES DE BUSQUEDA Y FILTRO==================

#=======BUSQUEDAS POR ID=========
#Retornar el objeto o None

def buscar_cliente_por_id(clientes,id_buscado):
    
    for cliente in clientes:
        
        if cliente.obtener_id() == id_buscado:
            
            return cliente
        
    return None

def buscar_mascota_por_id(mascotas,id_buscado):
    
    for mascota in mascotas:
        
        if mascota.obtener_id() == id_buscado:
            
            return mascota
    return None

def buscar_servicio_por_id(id_buscado,servicios):
    
    for servicio in servicios:
        
        if servicio.obtener_id() == id_buscado:
            
            return servicio
    return None

def buscar_cita_por_id(citas,id_buscado):
    
    for cita in citas:
        
        if cita.obtener_id() == id_buscado:
            return cita
    return None

#============FILTROS (RETORNAN UNA LISTA, QUE PUEDE ESTAR VACÍA)

#Retornar una lista con las mascotas de un dueño.
def filtrar_mascotas_por_cliente(id_buscado,mascotas):
    
    mascotas_cliente = []
    
    for mascota in mascotas:
        
        if mascota.obtener_id_cliente() == id_buscado:
            
            mascotas_cliente.append(mascota)
    return mascotas_cliente

#Retorna todas las citas que estan activas.
def filtrar_citas_activas(citas):
    
    citas_activas =[]
    for cita in citas:
        
        if cita.esta_activa()==True:
            
            citas_activas.append(cita)
    return citas_activas

#Retorna todas las citas canceladas o activas de la mascota
def filtrar_cita_por_mascota(citas,id_buscado):
    citas_mascota = [] 
    
    for cita in citas:
        
        mascota = cita.obtener_mascota()
        
        if mascota.obtener_id() == id_buscado:
            
            citas_mascota.append(cita)
            
    return citas_mascota

#==============COMPROBACIONES (RETORNAN TRUE O FALSE) ===============

def cliente_tiene_mascota(mascotas,id_buscado):
    
    for mascota in mascotas:
        if mascota.obtener_id_cliente() == id_buscado:
            
            return True
    return False 

#Servira para bloquear la eliminación de una mascota.
def mascotas_tiene_citas(id_buscado,citas):
    
    for cita in citas:
        
        mascota = cita.obtener_mascota()
        if mascota.obtener_id() == id_buscado:
            
            return True
    return False 

#Comprueba que en la fecha y franja ingresadas no haya una cita en ese mismo horario.
def existe_cita_activa_en_franja(citas,fecha,franja):
    
    citas_activas = filtrar_citas_activas(citas)
    
    for cita in citas_activas:
        
        if (cita.obtener_franja() == franja and cita.obtener_fecha()== fecha) :
            
            return True 
    return False

#==========GENERACIÓN DE IDs ===========
def generar_id(elementos,prefijo):
    
    mayor = 0
        
    for elemento in elementos:
            
        numero = int(elemento.obtener_id()[len(prefijo):])
        if numero > mayor:
            mayor = numero
    return f"{prefijo}{mayor + 1:03d}"

#==================FUNCIONES DE GESTION DE MASCOTAS=====================
#Nota: Bool y mensaje nos permiten reutilizar estas funciones de gestion tanto para la consola como para la interfaz gráfica.

def mostrar_mascotas(mascotas):
    
    informacion_mascotas = []
    if len(mascotas) == 0:
        
        return False,"No hay mascotas registradas."
        
    for mascota in mascotas:
        
        informacion_mascotas.append(mascota.obtener_informacion())
        
    return True,informacion_mascotas

def consultar_mascota_por_id(mascotas,id_buscado):
    
    mascota = buscar_mascota_por_id(mascotas,id_buscado)
    
    if mascota is None:
        return False,"No existe una mascota con el ID ingresado"
    else:
        return True,mascota.obtener_informacion()

    
def buscar_mascotas_de_cliente(mascotas,id_buscado,clientes):
    
    if (buscar_cliente_por_id(clientes,id_buscado)) is None:
        
        return False, "El cliente no existe"
    
    informacion_mascotas = [] 
    
    mascotas = filtrar_mascotas_por_cliente(id_buscado,mascotas)
    
    if len(mascotas) == 0:
        
        return False,"El cliente ingresado no tiene registrado mascotas."
    
    else:
        
        for mascota in mascotas:
            informacion_mascotas.append(mascota.obtener_informacion())
        return True, informacion_mascotas

        
def consultar_citas_de_mascota(citas,mascotas,id_buscado):
    
    if (buscar_mascota_por_id(mascotas,id_buscado)) is None:
        
        return False, "La mascota no existe. No se puede continuar con el proceso"
        
    informacion_citas = []
    citas_mascota = filtrar_cita_por_mascota(citas,id_buscado)
    
    if len(citas_mascota) == 0:
        
        return False,"La mascota no tiene citas registradas"
    for cita in citas_mascota:
        informacion_citas.append(cita.obtener_informacion())
    return True, informacion_citas


def registrar_mascota(mascotas,clientes,nombre,especie,raza,id_dueño):
    
    if nombre.strip() == "":
        return False,"El nombre de la mascota no puede estar vacío."
    
    if not combinacion_valida(especie,raza):
        return False,"La especie y la raza no son una combinación válida."
    
    if (buscar_cliente_por_id(clientes,id_dueño)) is None:
        return False, "El cliente ingresado no existe...No se puede realizar el registro."
    
    id_mascota = generar_id(mascotas,"M")
    nom_mascota = nombre
    id_cliente = id_dueño
    nueva_mascota = Mascota(id_mascota,nom_mascota,especie,raza,id_cliente)
    
    mascotas.append(nueva_mascota)
    return True, f"Mascota registrada correctamente con el ID {id_mascota}"

    
def actualizar_datos_mascota(mascotas,id_buscado,nueva_especie,nueva_raza):
    mascota = buscar_mascota_por_id(mascotas,id_buscado) 
    if mascota is None:
        return False, "No existe la mascota ingresada."
    if mascota.actualizar_datos(nueva_especie,nueva_raza):
        return True, "Se actualizaron los datos correctamente"
    else:
        return False, "No se logro realizar la actualización."

#PARA LA ELIMINACIÓN DE MASCOTAS SE DIVIDIRA EN DOS FUNCIONES PARA QUE PUEDA SER REUTILIZADA EN EL TKINTER Y EN LA CONSOLA, Y QUE CUMPLA CON ELIMINARSE SOLO SI EL USUARIO LO DESEA.

#VALIDA QUE CUMPLA CON TODOS LOS REQUERIMIENTOS PARA REALIZAR DICHA OPERACIÓN

def validar_se_puede_eliminar_mascota(mascotas,id_buscado,citas):
    
    mascota = buscar_mascota_por_id(mascotas,id_buscado)
    
    if mascota is None:
        return False,"La mascota buscada no existe."
    
    mascota_cita = mascotas_tiene_citas(id_buscado,citas)
    
    if mascota_cita:
        return False, "La mascota tiene citas registradas. No se puede realizar su eliminación."
    
    return True, "La mascota cumple con los requisitos para ser eliminada."

def ejecutar_eliminacion_mascota(mascotas,id_buscado):
    
    mascota = buscar_mascota_por_id(mascotas,id_buscado)
    mascotas.remove(mascota)
    return True, "Mascota eliminada exitosamente."

#===============FUNCIONES DE GESTION DE SERVICIOS=====================

def mostrar_todos_los_servicios(servicios):
    
    informacion_servicios = []
    if len(servicios) == 0:
        return False,"No hay servcios registrados"
        
    for servicio in servicios:
        informacion_servicios.append(servicio.obtener_informacion())
        
    return True,informacion_servicios

def consultar_servicio_por_id(servicios,id_buscado):
    
    servicio = buscar_servicio_por_id(id_buscado,servicios)
    if servicio is None:
        return False,"El servicio con ese ID no existe."
    
    return True,servicio.obtener_informacion()

def actualizar_tarifa_por_servicio(servicios,tarifa_nueva,id_buscado):
    
    servicio = buscar_servicio_por_id(id_buscado,servicios)
    if servicio is None:
        return False,"El servicio ingresado no existe. No se puede realizar su actualización de tarifa."
    
    servico_valido = servicio.actualizar_tarifa(tarifa_nueva)
    
    if servico_valido:
        return True, "Se hizo la actualización correctamente."
    return False, (
        "La tarifa debe estar entre "
        f"${servicio.obtener_tarifa_min():,} y "
        f"${servicio.obtener_tarifa_max():,} COP.".replace(",", ".")
    )

#=======================FUNCIONES DE GESTION DE CITAS======================

def mostrar_todas_las_citas(citas):
    
    if len(citas) == 0:
        
        return False, "No hay citas registradas de momento."
    
    informacion_citas = []
    
    for cita in citas:
        
        informacion_citas.append(cita.obtener_informacion())
    return True,informacion_citas

def mostrar_citas_activas(citas):
    
    citas_activas = filtrar_citas_activas(citas)
    
    if len(citas_activas) == 0:
        return False,"No hay citas activas de momento."
    informacion_citas_activas = []
    
    for cita in citas_activas:
        
        informacion_citas_activas.append(cita.obtener_informacion())
        
    return True,informacion_citas_activas

def consultar_citas_por_id(citas,id_buscado):
    
    cita = buscar_cita_por_id(citas,id_buscado)
    if cita is None:
        return False,"La cita ingresada no existe."
    return True,cita.obtener_informacion()

def registrar_cita(citas,id_mascota,id_servicio,mascotas,servicios,fecha,franja):
    
    mascota = buscar_mascota_por_id(mascotas,id_mascota)
    
    if mascota is None:
        return False,"La mascota ingresada no existe. No se puede realizar el registro."
    
    servicio = buscar_servicio_por_id(id_servicio,servicios)
    
    if servicio is None:
        return False,"El servicio no existe. No se puede realizar el registro."
    
    cita_activa = existe_cita_activa_en_franja(citas,fecha,franja)
    
    if cita_activa:
        return False,"No se puede realizar el registro de cita. Ya hay una cita activa en esa fecha y franja horaria."
    
    id_cita = generar_id(citas,"C")
    
    cita_nueva = Cita(id_cita,mascota,servicio,fecha,franja,True)
    
    citas.append(cita_nueva)
    return True,f"Se registro correctamente la cita con ID: {id_cita}."

#PARA QUE EN LA OPERACION CANCELAR CITA PUEDA SER REUTILIZADA POR LA CONSOLA Y LA GUI, SE HARA EN DOS FUNCIONES, PARA QUE SE PUEDA REALIZAR EL MENSAJE DE CONFIRMACION ANTES DE DE CANCELARLA.

def validacion_cancelar_cita(citas,id_buscado):
    
    cita = buscar_cita_por_id(citas,id_buscado)
    if cita is None:
        return False, "La cita ingresada no existe. No se puede realizar la cancelación."
    if cita.esta_activa():
        return True,"La cita esta activa, se puede realizar su cancelación"
    return False,"La cita ya estaba cancelada."

def ejecutar_cancelacion_cita(citas,id_buscado):
    
    cita = buscar_cita_por_id(citas,id_buscado)
    cita.cancelar()
    return True,"Se cancelo la cita correctamente."
    
# ================== FUNCIONES DE GESTION DE CLIENTES ==================

def mostrar_clientes(clientes):
    
    informacion_clientes = []

    if len(clientes) == 0:
        return False, "No hay clientes registrados."

    for cliente in clientes:
        informacion_clientes.append(cliente.obtener_informacion())

    return True, informacion_clientes


def consultar_cliente_por_id(clientes, id_buscado):
    
    cliente = buscar_cliente_por_id(clientes, id_buscado)

    if cliente is None:
        return False, "No existe un cliente con el ID ingresado."

    return True, cliente.obtener_informacion()


def registrar_cliente(clientes, id_cliente, nom_cliente, telefono):
    id_cliente = id_cliente.strip()
    nom_cliente = nom_cliente.strip()
    telefono = telefono.strip()

    if id_cliente == "":
        return False, "El ID del cliente no puede estar vacío."

    if buscar_cliente_por_id(clientes, id_cliente) is not None:
        return False, "Ya existe un cliente con el ID ingresado."

    if nom_cliente == "":
        return False, "El nombre del cliente no puede estar vacío."

    if not telefono.isdigit() or len(telefono) != 10:
        return False, "El teléfono debe contener exactamente 10 dígitos numéricos."

    nuevo_cliente = Cliente(id_cliente, nom_cliente, telefono)
    clientes.append(nuevo_cliente)

    return True, "Cliente registrado correctamente."


def actualizar_telefono_cliente(clientes, id_buscado, nuevo_tel):
    cliente = buscar_cliente_por_id(clientes, id_buscado)

    if cliente is None:
        return False, "No existe un cliente con el ID ingresado."

    nuevo_tel = nuevo_tel.strip()

    if not nuevo_tel.isdigit() or len(nuevo_tel) != 10:
        return False, "El teléfono debe contener exactamente 10 dígitos numéricos."

    if cliente.actualizar_telefono(nuevo_tel):
        return True, "El teléfono del cliente se actualizó correctamente."

    return False, "No se logró actualizar el teléfono."


# La eliminación se divide en dos funciones igual que en mascotas y citas
# Eso permite validar primero y pedir confirmación desde l consola o Tkinter 

def validar_se_puede_eliminar_cliente(clientes, id_buscado, mascotas):
    cliente = buscar_cliente_por_id(clientes, id_buscado)

    if cliente is None:
        return False, "El cliente ingresado no existe."

    if cliente_tiene_mascota(mascotas, id_buscado):
        return False, "El cliente tiene mascotas registradas. No se puede eliminar."

    return True, "El cliente cumple con los requisitos para ser eliminado."


def ejecutar_eliminacion_cliente(clientes, id_buscado):
    cliente = buscar_cliente_por_id(clientes, id_buscado)

    if cliente is None:
        return False, "El cliente ingresado no existe."

    clientes.remove(cliente)
    return True, "Cliente eliminado correctamente."
    
        
    

    
    
        
            
            
