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


mi_auto = Auto("Toyota", "Corolla", 2020)
mi_auto.mostrar_informacion()
mi_auto.actualizar_kilometraje(15000)
mi_auto.realizar_viaje(5000)
mi_auto.estado_auto()
mi_auto.actualizar_kilometraje(12000) 
mi_auto.realizar_viaje(-100)  
mi_auto.estado_auto()