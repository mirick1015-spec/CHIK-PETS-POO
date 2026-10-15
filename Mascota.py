class Mascota:
    
    def __init__(self,id_mascota,nom_mascota,especie,raza,id_cliente):
        
        self.__id_mascota = id_mascota 
        self.__nom_mascota = nom_mascota
        self.__especie = especie
        self.__raza = raza
        self.__id_cliente = id_cliente
        
    def obtener_id(self):
        
        return self.__id_mascota
    
    def obtener_nom_mascota(self,):
        
        return self.__nom_mascota
    
    def obtener_especie(self):
        
        return self.__especie
    
    def obtener_raza(self):
        
        return self.__raza
    
    def obtener_id_cliente(self):
        
        return self.__id_cliente
    
    def actualizar_datos(self,nueva_especie,nueva_raza):
        
        especies_y_razas = {
            "perro": ["criollo", "bulldog", "chihuahua", "pug", "golden", "pastor alemán", "french poodle"],
            "gato": ["criollo", "persa", "siamés", "maine coon", "ragdoll", "bengalí"],
            "conejo": ["enano holandés", "cabeza de león", "mini rex", "mini lop", "holland lop"]}
        
        if nueva_especie in especies_y_razas:
            
            for r in especies_y_razas[nueva_especie]:
                
                if r == nueva_raza:
                    
                    self.__especie = nueva_especie
                    self.__raza = nueva_raza
                    return True
        return False
    
    def __str__(self):
        
        return f"{self.__nom_mascota} | {self.__id_mascota} | {self.__especie} | {self.__raza}"
    
    def obtener_informacion(self):
        
        return(
            f"El ID de la mascota es: {self.__id_mascota}\n"
            f"El nombre de la mascota es: {self.__nom_mascota}\n"
            f"La especie de la mascota es: {self.__especie}\n"
            f"La raza de la mascota es: {self.__raza}\n"
            f"El ID del dueño de la mascota es: {self.__id_cliente}\n"
        )
    
                