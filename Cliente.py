class Cliente:
    
    def __init__(self,id_cliente,nom_cliente,telefono):
        
        self.__id_cliente = id_cliente
        self.__nom_cliente = nom_cliente
        self.__telefono = telefono
        
    def obtener_id(self):
        
        return self.__id_cliente
    
    def obtener_nombre_cliente(self):
        
        return self.__nom_cliente
    
    def obtener_telefono_cliente(self):
        
        return self.__telefono
    
    def actualizar_telefono(self,nuevo_tel):
        
        if len(nuevo_tel) <= 10:
            self.__telefono = nuevo_tel
            return True
        else:
            return False
        
    def obtener_informacion(self):
        
        return (
            f"El ID del cliente es: {self.__id_cliente}\n"
            f"El nombre del cliente es: {self.__nom_cliente}\n"
            f"El telefono del usuario es: {self.__telefono}\n"
        )
        
        
        
    