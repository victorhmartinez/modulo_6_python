class Auto:
    def __init__(self,marca,modelo,anio,kilometraje=0):
       self.marca=marca
       self.modelo=modelo
       self.anio=anio
       self.kilometraje=kilometraje
       
    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}")

    def actualizar_kilometraje(self, kilometraje):
        if kilometraje >= self.kilometraje:
            self.kilometraje = kilometraje
        else:
            print("No se puede reducir el kilometraje.")

    def realizar_viaje(self, kilometros):
        if kilometros > 0:
            self.kilometraje += kilometros
            print(f"Kilometraje incrementado a {self.kilometraje} km tras recorrer {kilometros} km")
        else:
            print("La cantidad de kilómetros debe ser positiva.")

    def estado_auto(self):
        if self.kilometraje < 20000:
            print("Estoy como nuevo.")
        elif 20000 <= self.kilometraje <= 100000:
            print("Ya estoy usado.")
        else:
            print("¡Ya déjame descansar por favor!")


    @classmethod
    def crear_auto_nuevo(cls, modelo):
        marca= "Toyota"
        anio_actual =2024
        return cls(marca, modelo, anio_actual)
    @staticmethod
    def comparar_kilometraje(auto1, auto2):
        if auto1.kilometraje == auto2.kilometraje:
            print(f"Ambos autos tienen el mismo kilometraje: {auto1.kilometraje} km")
        else:
            print(f"Los autos tienen diferente kilometraje: {auto1.kilometraje} km y {auto2.kilometraje} km")

    
    @staticmethod
    def validar_anio_fabricacion(anio):
        anio_actual = 2024
        if 1886 <= anio <= anio_actual: 
            print(f"El año {anio} esta dentro de las fechas de creacion del primer auto.")
        else:
            print(f"El año {anio} no es válido para fechas de creacion del primer auto.")

    @classmethod
    def crear_auto_antiguo(cls, modelo, anio):
        marca="Convertible"
        return cls(marca, modelo, anio)


