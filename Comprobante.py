from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from datetime import datetime
import random
from RandList import lista

class facturacion:
    def __init__(self, ancho, alto):
        self.ventana= Tk()
        self.ancho= ancho
        self.alto= alto
        self.fondoC= PhotoImage(file="imagenes/Comprobante.png")

    def contar(self):
        self.Registros= open("precios.txt","r")
        cantidad= self.Registros.readlines()
        Ncantidad= len(cantidad)
        return Ncantidad
    
    def SubTotal(self):
        subtotal=0
        leer= open("precios.txt","r")
        longitud= leer.readlines()
        for i in longitud:
            subtotal+=int(i)
        return subtotal

    def facturaCompleta(self):
        self.Registros= open("recolecta.txt","r")
        counter= 0
        for i in self.Registros:
            if counter == 0:
                nombre= i
                counter+=1
            elif counter == 1:
                ciudad= i
                counter+=1
            elif counter == 2:
                documento= i
                counter+=1
            elif counter == 3:
                telefono= i
                counter+=1
            elif counter == 4:
                hora= i
                counter+=1
            elif counter == 5:
                mood= i
        self.ventana.geometry(str(self.ancho)+"x"+str(self.alto))
        self.ventana.resizable(width=0,height=0)
        self.ventana.config(bg="black")
        self.ventana.title("Comprobante de pago")
        self.backfondo= tk.Label(image=self.fondoC).place(x=0,y=0)
        self.fecha= datetime.today().strftime(('%Y-%m-%d %H:%M'))
        self.rand= random.choice(lista)
        self.labFec= tk.Label(text=self.fecha,font=("Lucida Sans Unicode",14),bg=('#f5f5cb'),bd=0).place(x=156,y=207)
        self.ordentx= tk.Label(text=self.rand,font=("Lucida Sans Unicode",14),bg=('#f5f5cb'),bd=0).place(x=180,y=178)        
        self.nombre= tk.Label(text=nombre,font=("Lucida Sans Unicode",14),bg=('#f5f5cb'),bd=0).place(x=185,y=282)   
        self.docu= tk.Label(text=documento,font=("Lucida Sans Unicode",14),bg=('#f5f5cb'),bd=0,anchor="s").place(x=230,y=343)
        self.tel= tk.Label(text=telefono,font=("Lucida Sans Unicode",14),bg=('#f5f5cb'),bd=0,anchor="s").place(x=342,y=400)
        self.city= tk.Label(text=ciudad,font=("Lucida Sans Unicode",14),bg=('#d4e18b'),bd=0,anchor="s").place(x=171,y=455)
        self.modalidad= tk.Label(text=mood,font=("Lucida Sans Unicode",14),bg=('#d6e290'),bd=0,anchor="s").place(x=649,y=177) 
        self.hora= tk.Label(text=hora,font=("Lucida Sans Unicode",14),bg=('#d6e290'),bd=0,anchor="s").place(x=713,y=210)    
        self.total= self.contar()
        self.products= tk.Label(text=self.total,font=("Lucida Sans Unicode",14),bg=('#f5f5cb'),bd=0).place(x=360,y=570)
        if mood == "Domicilio":
            precioDomi=10000
        else:
            precioDomi=0

        self.precioDomi= tk.Label(text=precioDomi,font=("Lucida Sans Unicode",14),bg=('#f5f5cb'),bd=0,anchor="s").place(x=700,y=542)
        self.subtotalp=self.SubTotal()
        self.pagar= tk.Label(text=self.subtotalp,font=("Lucida Sans Unicode",14),bg=('#f5f5cb'),bd=0,anchor="s").place(x=700,y=515)
        totalFactura= self.subtotalp+precioDomi
        self.finallabel= tk.Label(text=totalFactura,font=("Lucida Sans Unicode",14),bg=('#d6e290'),bd=0,anchor="s").place(x=700,y=570)   
        self.ventana.mainloop()

#v6= facturacion(900,700)
#v6.facturaCompleta()