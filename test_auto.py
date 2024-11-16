from Auto import Auto
# Crear autos nuevos
auto1 = Auto.crear_auto_nuevo("Corolla")
auto2 = Auto.crear_auto_nuevo("Yaris")

# Mostramos la información  de los  autos nuevos
auto1.mostrar_informacion()
auto2.mostrar_informacion()


auto1.actualizar_kilometraje(5000)
auto2.actualizar_kilometraje(6000)

# Comparamos los  kilometrajes entre los autos
Auto.comparar_kilometraje(auto1, auto2)

# Cremaos un auto antiguo y validar su año
auto3 = Auto.crear_auto_antiguo("Mustang", 1965)
auto3.mostrar_informacion()
Auto.validar_anio_fabricacion(1965)

# validamos el auto con  un año inválido
Auto.validar_anio_fabricacion(1880)