class Cita:
    
    def __init__(self,id_cita,mascota,servicio,fecha,franja,estado=True):
        
        self.__id_cita = id_cita
        self. __mascota = mascota
        self.__servicio = servicio
        self.__fecha = fecha
        self.__franja = franja
        self.__estado = estado
        
    def obtener_id(self):
        
        return self.__id_cita
    
    def obtener_mascota(self):
        
        return self.__mascota
    
    def obtener_servicio(self):
        
        return self.__servicio
    
    def obtener_fecha(self):
        
        return self.__fecha
    
    def obtener_franja(self):
        
        return self.__franja
    
    def obtener_estado(self):
        
        return self.__estado
    
    def esta_activa(self):
        
        if self.__estado == True:
            
            return True
        else:
            
            return False
        
    def cancelar(self):
        
        if self.__estado == True:
            
            self.__estado = False
            return True
        
        else:
            
            return False
        
    def informar_estado(self):
        
        if self.esta_activa () == True:
            return "Cita activa"
        else:
            return "Cita inactiva"

    def obtener_informacion(self):
        
        return(
            f"El ID de la cita es: {self.__id_cita}\n"
            f"La mascota es: {self.__mascota}\n"
            f"El servicio es: {self.__servicio}\n"
            f"La fecha de la cita es: {self.__fecha}\n"
            f"La franja horaria es: {self.__franja}\n"
            f"La cita tiene estado:{self.informar_estado()}\n"
        )
            