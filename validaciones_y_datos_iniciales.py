import unicodedata


def normalizar_texto(valor):
    """Normaliza texto para comparar sin importar mayúsculas, tildes o espacios extras."""
    if valor is None:
        return ""
    texto = unicodedata.normalize("NFKD", str(valor))
    texto = "".join(caracter for caracter in texto if not unicodedata.combining(caracter))
    return texto.strip().lower()


def leer_entrada(mensaje):
    try:
        return input(mensaje)
    except EOFError:
        print("\nNo se recibió entrada del usuario. Saliendo del programa...")
        raise SystemExit(0)


def leer_texto_no_vacio(mensaje):
    while True:
        valor = leer_entrada(mensaje)
        if valor.strip() != "":
            return valor.strip()
        print("El valor ingresado está vacío. Intente de nuevo.")


def leer_numero_entero_positivo(mensaje):
    while True:
        try:
            numero = int(leer_entrada(mensaje))
            if numero > 0:
                return numero
            print("Ingrese un número entero mayor a 0.")
        except ValueError:
            print("Ingrese un valor válido.")


def leer_id(mensaje):
    """
    Solicita un identificador no vacío.
    Retorna el identificador en mayúsculas.
    """
    while True:
        valor = leer_entrada(f"{mensaje}").strip().upper()
        if valor != "":
            return valor
        print("El identificador no puede estar vacío.")


def leer_confirmacion(mensaje):
    while True:
        confirmacion = leer_entrada(mensaje).strip().lower()
        if confirmacion == "s":
            return True
        if confirmacion == "n":
            return False
        print("Ingrese s/n, no se acepta otro valor. Intente de nuevo.")


def leer_telefono_valido():
    while True:
        telefono = leer_entrada("Ingrese un teléfono válido: ").strip()
        if telefono.isdigit() and 1 <= len(telefono) <= 10:
            return telefono
        print("Ingrese un teléfono con valores numéricos y máximo 10 dígitos.")


def leer_entero_en_rango(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(leer_entrada(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print("Error: Ingrese un valor dentro del rango.")
        except ValueError:
            print("Error: Ingrese un número entero dentro del rango.")


def seleccionar_especie():
    print("======ESPECIES======")
    print("")
    print("""
        1. Perro
        2. Gato
        3. Conejo""")

    opcion = leer_entero_en_rango("Ingrese una especie: ", 1, 3)

    if opcion == 1:
        return "perro"
    if opcion == 2:
        return "gato"
    if opcion == 3:
        return "conejo"
    return None


def seleccionar_raza(especie):
    especie = normalizar_texto(especie)

    if especie == "perro":
        print("=======RAZAS========")
        print("")
        print("""
            1. Criollo
            2. Bulldog
            3. Chihuahua
            4. Pug
            5. Golden
            6. Pastor Alemán
            7. French Poodle
        """)
        opcion_raza = leer_entero_en_rango("Ingrese una raza: ", 1, 7)
        if opcion_raza == 1:
            return "criollo"
        if opcion_raza == 2:
            return "bulldog"
        if opcion_raza == 3:
            return "chihuahua"
        if opcion_raza == 4:
            return "pug"
        if opcion_raza == 5:
            return "golden"
        if opcion_raza == 6:
            return "pastor aleman"
        if opcion_raza == 7:
            return "french poodle"

    elif especie == "gato":
        print("=======RAZAS========")
        print("")
        print("""
            1. Criollo
            2. Persa
            3. Siamés
            4. Maine Coon
            5. Ragdoll
            6. Bengalí
        """)
        opcion_raza = leer_entero_en_rango("Ingrese una raza: ", 1, 6)
        if opcion_raza == 1:
            return "criollo"
        if opcion_raza == 2:
            return "persa"
        if opcion_raza == 3:
            return "siames"
        if opcion_raza == 4:
            return "maine coon"
        if opcion_raza == 5:
            return "ragdoll"
        if opcion_raza == 6:
            return "bengali"

    else:
        print("=======RAZAS========")
        print("")
        print("""
            1. Enano Holandés
            2. Cabeza de León
            3. Mini Rex
            4. Mini Lop
            5. Holland Lop
        """)
        opcion_raza = leer_entero_en_rango("Ingrese una raza: ", 1, 5)
        if opcion_raza == 1:
            return "enano holandes"
        if opcion_raza == 2:
            return "cabeza de leon"
        if opcion_raza == 3:
            return "mini rex"
        if opcion_raza == 4:
            return "mini lop"
        if opcion_raza == 5:
            return "holland lop"

    return None


def seleccionar_franja():
    print("=======FRANJAS HORARIAS========")
    print("")
    print("""
        1. 8:00-9:00
        2. 9:00-10:00
        3. 10:00-11:00
        4. 11:00-12:00
        5. 14:00-15:00
        6. 15:00-16:00
        7. 16:00-17:00
    """)
    opcion = leer_entero_en_rango("Ingrese la opción de la franja horaria que desea: ", 1, 7)

    if opcion == 1:
        return "8:00-9:00"
    if opcion == 2:
        return "9:00-10:00"
    if opcion == 3:
        return "10:00-11:00"
    if opcion == 4:
        return "11:00-12:00"
    if opcion == 5:
        return "14:00-15:00"
    if opcion == 6:
        return "15:00-16:00"
    return "16:00-17:00"


def seleccionar_fecha():
    print("=========FECHAS===========")
    print("")
    print("""
        1. 12/10/2026
        2. 13/10/2026
        3. 14/10/2026
        4. 15/10/2026
        5. 16/10/2026
        6. 17/10/2026
        7. 18/10/2026
    """)

    opcion = leer_entero_en_rango("Ingrese la opción de una fecha horaria que desea: ", 1, 7)

    if opcion == 1:
        return "12/10/2026"
    if opcion == 2:
        return "13/10/2026"
    if opcion == 3:
        return "14/10/2026"
    if opcion == 4:
        return "15/10/2026"
    if opcion == 5:
        return "16/10/2026"
    if opcion == 6:
        return "17/10/2026"
    return "18/10/2026"


def combinacion_valida(especie, raza):
    """
    Retorna True si la especie existe y la raza pertenece a esa especie.
    """
    especie = normalizar_texto(especie)
    raza = normalizar_texto(raza)

    RAZAS_POR_ESPECIE = {
        "perro": ["criollo", "bulldog", "chihuahua", "pug", "golden", "pastor aleman", "french poodle"],
        "gato": ["criollo", "persa", "siames", "maine coon", "ragdoll", "bengali"],
        "conejo": ["enano holandes", "cabeza de leon", "mini rex", "mini lop", "holland lop"],
    }

    return especie in RAZAS_POR_ESPECIE and raza in RAZAS_POR_ESPECIE[especie]

