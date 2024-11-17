
from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from laptop_business import LaptopBusiness


laptop_pepito=Laptop("lenovo","17",32)
laptop_maria=Laptop("lenovo","17",32,600)


laptop_juanito=Laptop_Gaming("MSI","I7",4,"RTX 8GB")

laptop_jefazo=LaptopBusiness("Dell", "i7", 16, 200, 10)


print(laptop_jefazo.realizar_diagnostico_sistema())
