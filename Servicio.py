class Servicio:
    def __init__(self, id_servicio, nom_servicio, tarifa, tarifa_min, tarifa_max):
        
        self.__id_servicio = id_servicio
        self.__nom_servicio = nom_servicio
        self.__tarifa = tarifa
        self.__tarifa_min = tarifa_min
        self.__tarifa_max = tarifa_max
        
    def obtener_id (self):
        return self.__id_servicio
    
    def obtener_nombre(self):
        return self.__nom_servicio
    
    def obtener_tarifa(self):
        return self.__tarifa
    
    def obtener_tarifa_min(self):
        return self.__tarifa_min
    
    def obtener_tarifa_max(self):
        return self.__tarifa_max
    
    def actualizar_tarifa(self,nueva_tarifa):
        
        if (
            isinstance(nueva_tarifa, int)
            and not isinstance(nueva_tarifa, bool)
            and self.__tarifa_min <= nueva_tarifa <= self.__tarifa_max
        ):
            self.__tarifa = nueva_tarifa
            return True
        return False
    
    def __str__(self):
        
        return f"{self.__id_servicio} | {self.__nom_servicio} | {self.__tarifa} "
        
    def obtener_informacion(self):
        precio = f"${self.__tarifa:,}".replace(",", ".")
        minimo = f"${self.__tarifa_min:,}".replace(",", ".")
        maximo = f"${self.__tarifa_max:,}".replace(",", ".")
        return (
            f"ID: {self.__id_servicio}\n"
            f"Servicio: {self.__nom_servicio}\n"
            f"Precio: {precio} COP\n"
            f"Rango permitido: {minimo} - {maximo} COP\n"
        )