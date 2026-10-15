# Persistencia de Chik & Pets: guarda y recupera datos en JSON.
import json
from pathlib import Path

from Cliente import Cliente
from Mascota import Mascota
from Servicio import Servicio
from Cita import Cita

# Un solo archivo JSON para todo el proyecto.
ARCHIVO_DATOS = Path(__file__).resolve().with_name("datos.json")

SERVICIOS_PREDEFINIDOS = (
    ("S001", "Baño general y secado", 40000, 35000, 70000),
    ("S002", "Corte de pelo y estilo", 65000, 45000, 80000),
    ("S003", "Corte de uñas y limpieza de oídos", 20000, 15000, 35000),
    ("S004", "Masajes", 35000, 30000, 75000),
    ("S005", "Limpieza dental", 100000, 90000, 200000),
    ("S006", "Desparasitación", 25000, 20000, 90000),
    ("S007", "Vacunación", 50000, 40000, 110000),
)


def crear_servicios_predefinidos(tarifas_guardadas=None):
    tarifas_guardadas = tarifas_guardadas or {}
    return [
        Servicio(
            id_servicio,
            nombre,
            tarifas_guardadas.get(id_servicio, tarifa_inicial),
            tarifa_min,
            tarifa_max,
        )
        for id_servicio, nombre, tarifa_inicial, tarifa_min, tarifa_max
        in SERVICIOS_PREDEFINIDOS
    ]



def guardar_datos(clientes, mascotas, servicios, citas, archivo=ARCHIVO_DATOS):
    datos = {
        "clientes": [
            {
                "id": cliente.obtener_id(),
                "nombre": cliente.obtener_nombre_cliente(),
                "telefono": cliente.obtener_telefono_cliente(),
            }
            for cliente in clientes
        ],
        "mascotas": [
            {
                "id": mascota.obtener_id(),
                "nombre": mascota.obtener_nom_mascota(),
                "especie": mascota.obtener_especie(),
                "raza": mascota.obtener_raza(),
                "id_cliente": mascota.obtener_id_cliente(),
            }
            for mascota in mascotas
        ],
        "servicios": [
            {
                "id": servicio.obtener_id(),
                "nombre": servicio.obtener_nombre(),
                "tarifa": servicio.obtener_tarifa(),
                "tarifa_min": servicio.obtener_tarifa_min(),
                "tarifa_max": servicio.obtener_tarifa_max(),
            }
            for servicio in servicios
        ],
        "citas": [
            {
                "id": cita.obtener_id(),
                "id_mascota": cita.obtener_mascota().obtener_id(),
                "id_servicio": cita.obtener_servicio().obtener_id(),
                "fecha": cita.obtener_fecha(),
                "franja": cita.obtener_franja(),
                "estado": cita.obtener_estado(),
            }
            for cita in citas
        ],
    }
    archivo.write_text(
        json.dumps(datos, ensure_ascii=False, indent=4) + "\n",
        encoding="utf-8",
    )



def cargar_datos(archivo=ARCHIVO_DATOS):
    if not archivo.exists():
        return [], [], [], []

    with archivo.open(encoding="utf-8") as archivo_json:
        datos = json.load(archivo_json)

    if not isinstance(datos, dict):
        raise ValueError("El archivo de datos debe contener un objeto JSON.")

    categorias = ("clientes", "mascotas", "servicios", "citas")
    if any(not isinstance(datos.get(categoria), list) for categoria in categorias):
        raise ValueError(
            "El archivo de datos debe contener listas de clientes, mascotas, "
            "servicios y citas."
        )

    clientes = [
        Cliente(item["id"], item["nombre"], item["telefono"])
        for item in datos["clientes"]
    ]
    mascotas = [
        Mascota(
            item["id"],
            item["nombre"],
            item["especie"],
            item["raza"],
            item["id_cliente"],
        )
        for item in datos["mascotas"]
    ]
    rangos_predefinidos = {
        id_servicio: (tarifa_min, tarifa_max)
        for id_servicio, _, _, tarifa_min, tarifa_max in SERVICIOS_PREDEFINIDOS
    }
    tarifas_guardadas = {}
    for item in datos["servicios"]:
        id_servicio = item["id"]
        if id_servicio not in rangos_predefinidos:
            raise ValueError(
                f"El servicio {id_servicio} no pertenece al catálogo predefinido."
            )
        if id_servicio in tarifas_guardadas:
            raise ValueError(f"El servicio {id_servicio} está duplicado en el JSON.")
        tarifa = item["tarifa"]
        tarifa_min, tarifa_max = rangos_predefinidos[id_servicio]
        if (
            not isinstance(tarifa, int)
            or isinstance(tarifa, bool)
            or not tarifa_min <= tarifa <= tarifa_max
        ):
            raise ValueError(
                f"La tarifa guardada para el servicio {id_servicio} debe estar "
                f"entre {tarifa_min} y {tarifa_max} COP."
            )
        tarifas_guardadas[id_servicio] = tarifa
    servicios = crear_servicios_predefinidos(tarifas_guardadas)

    mascotas_por_id = {mascota.obtener_id(): mascota for mascota in mascotas}
    servicios_por_id = {servicio.obtener_id(): servicio for servicio in servicios}
    citas = []
    for item in datos["citas"]:
        try:
            mascota = mascotas_por_id[item["id_mascota"]]
            servicio = servicios_por_id[item["id_servicio"]]
        except KeyError as error:
            raise ValueError(
                f"La cita {item.get('id', '(sin ID)')} referencia una mascota "
                "o un servicio inexistente."
            ) from error
        citas.append(
            Cita(
                item["id"],
                mascota,
                servicio,
                item["fecha"],
                item["franja"],
                item["estado"],
            )
        )

    return clientes, mascotas, servicios, citas



def datos_iniciales():
    
    # 1. Crear clientes (al menos 5)
    clientes = [
        Cliente("C001", "Ana Gomez", "3162345678"),
        Cliente("C002", "Carlos Perez", "3178765432"),
        Cliente("C003", "Maria Lopez", "3181112233"),
        Cliente("C004", "Juan Torres", "3154445566"),
        Cliente("C005", "Lucia Diaz", "3197778899"),
    ]

    # 2. Crear mascotas relacionadas con esos clientes (al menos 5)
    mascotas = [
        Mascota("M001", "Firulais", "perro", "golden", "C001"),
        Mascota("M002", "Michi", "gato", "siamés", "C002"),
        Mascota("M003", "Lucas", "perro", "criollo", "C001"),
        Mascota("M004", "Copito", "conejo", "enano holandés", "C003"),
        Mascota("M005", "Max", "perro", "bulldog", "C004"),
    ]

    # 3. Servicios 
    servicios = crear_servicios_predefinidos()

    # 4. Citas de prueba asociadas a las mascotas y servicios
    citas = [
        Cita("C001", mascotas[0], servicios[0], "16/10/2026", "11:00-12:00", True),
        Cita("C002", mascotas[1], servicios[1], "13/10/2026", "8:00-9:00", True)
    ]

    return clientes, mascotas, servicios, citas        



