from laptop_business import LaptopBusiness
import tkinter as tk
from tkinter import ttk

from PIL import Image,ImageTk
import random
class AppBuisness:
    def __init__(self,root):
        self.root= root
        self.laptops=[]
        self.imagnes=["C:\\Users\\Usuario iTC\\Pictures\\Screenshots\\Modulo 6\\POO\\imgBuisness\\img1.png",
                      "C:\\Users\\Usuario iTC\\Pictures\\Screenshots\\Modulo 6\\POO\\imgBuisness\\img2.png",
                      "C:\\Users\\Usuario iTC\\Pictures\\Screenshots\\Modulo 6\\POO\\imgBuisness\\img3.png",
                      "C:\\Users\\Usuario iTC\\Pictures\\Screenshots\\Modulo 6\\POO\\imgBuisness\\img4.png",
                      "C:\\Users\\Usuario iTC\\Pictures\\Screenshots\\Modulo 6\\POO\\imgBuisness\\img5.png",
                      ]

        root.title("Ingresar datos")
        self.setup_ui();
        pass
    def setup_ui(self):
        ttk.Label(self.root,text="Marca").grid(row=0,column=0)
        self.marca=tk.StringVar()
        tk.Entry(self.root,textvariable=self.marca).grid(row=0,column=1) 

        ttk.Label(self.root,text="Procesador").grid(row=1,column=0)
        self.procesador=tk.StringVar()
        tk.Entry(self.root,textvariable=self.procesador).grid(row=1,column=1) 
       
        ttk.Label(self.root,text="Memoria").grid(row=2,column=0)
        self.memoria=tk.StringVar()
        tk.Entry(self.root,textvariable=self.memoria).grid(row=2,column=1) 


        ttk.Label(self.root,text="Almacenamiento").grid(row=3,column=0)
        self.almacenamiento=tk.StringVar()
        tk.Entry(self.root,textvariable=self.almacenamiento).grid(row=3,column=1) 

        ttk.Label(self.root,text="Duracion bateria").grid(row=4,column=0)
        self.duracion=tk.StringVar()
        tk.Entry(self.root,textvariable=self.duracion).grid(row=4,column=1) 

        ttk.Label(self.root,text="Precio").grid(row=5,column=0)
        self.precio=tk.StringVar()
        tk.Entry(self.root,textvariable=self.precio).grid(row=5,column=1) 

        ttk.Button(self.root,text="Agregar Laptop",command=self.agregar_laptop).grid(row=6,column=0)

        self.mostrar_laptops = tk.Text(self.root,height=10,width=50)
        self.mostrar_laptops.grid(row=7,column=0,columnspan=2)
  
        self.canva=tk.Canvas(self.root,width=200,height=200)
        self.canva.grid(row=1,column=3,rowspan=6)

    def agregar_laptop(self):
        nueva_laptop=LaptopBusiness(self.marca.get(),self.procesador.get(),self.memoria.get(),self.almacenamiento.get(),self.duracion.get(),self.precio.get())
        self.laptops.append(nueva_laptop)
        print(self.laptops[0])
        self.mostrar_laptops.insert(tk.END,f"{nueva_laptop}")
        self.mostrar_imagen_aleatorias()
       
    def mostrar_imagen_aleatorias(self):
        imagenPath=random.choice(self.imagnes)
        imagen=Image.open(imagenPath)
        imagen=imagen.resize((200,200),Image.Resampling.LANCZOS)
        photo=ImageTk.PhotoImage(imagen)
        self.canva.create_image(0,0,anchor=tk.NW,image=photo)

        self.canva.image=photo
        pass
root=tk.Tk()
app=AppBuisness(root)
root.mainloop()

