from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
import tkinter as tk
import Lacteos 
import Comprobante as Fc
import Menu
import os

class Carnes(Lacteos.lacteos):
    def __init__(self, ancho, alto):
        super().__init__(ancho, alto)
        self.cat2= PhotoImage(file="imagenes/catC.png")
        self.pricesC= [6300,19700,12300,29400,46900,18800,20000,18700,5650]  

    def retorno(self):
        if os.path.isfile("precios.txt"):
            if self.preciosC.closed == False:
                self.preciosC.close() 
            else:
                pass
        else:
            pass
        self.ventana.destroy()
        mp= Menu.MenuP(900,600)
        mp.catalogo()
            
    def KeepDatos(self,index):
        self.preciosC= open("precios.txt","a")
        self.preciosC.write(f"{self.pricesC[index]}\n")

    def finisH(self):
        if os.path.isfile("precios.txt"):
            if self.preciosC.closed == False:
                self.preciosC.close()
            else:
                pass
            self.ventana.destroy()
            v6= Fc.facturacion(900,700)
            v6.facturaCompleta()
        else:
             messagebox.showerror(title="Error Productos",message="No hay productos registrados, ingrese al menos uno")

    def menuC(self):
        self.ventana.geometry(str(self.ancho)+"x"+str(self.alto)) 
        self.ventana.resizable(width=0,height=0)
        self.ventana.title("Pollo, carne y pescado")
        self.logo= tk.Label(image=self.cat2, bd=0)
        self.logo.place(x=0,y=0)
        self.b001= tk.Button(image=self.devolver,command=self.retorno,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b001.place(x=27,y=21)
        self.b02= tk.Button(image=self.finalizar,command=self.finisH,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b02.place(x=550,y=21)
        #11
        self.b1= tk.Button(image=self.add,command=self.tilapia,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b1.place(x=101,y=291)
        #12
        self.b2= tk.Button(image=self.add,command=self.tocino,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b2.place(x=308,y=291)
        #13
        self.b3= tk.Button(image=self.add,command=self.trucha,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b3.place(x=516,y=291)
        #21
        self.b4= tk.Button(image=self.add,command=self.pechuga,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b4.place(x=102,y=469)
        #22
        self.b5= tk.Button(image=self.add,command=self.camaron,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b5.place(x=307,y=469)
        #23
        self.b6= tk.Button(image=self.add,command=self.alitas,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b6.place(x=517,y=469)
        #31
        self.b7= tk.Button(image=self.add,command=self.burger,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b7.place(x=102,y=646)
        #32
        self.b8= tk.Button(image=self.add,command=self.chorizo,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b8.place(x=307,y=646)
        #33
        self.b7= tk.Button(image=self.add,command=self.higado,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b7.place(x=519,y=646)
        self.ventana.mainloop()
    
    def tilapia(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.KeepDatos(0)
    def tocino(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.KeepDatos(1)    
    def trucha(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.KeepDatos(2)    
    def pechuga(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.KeepDatos(3)    
    def camaron(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.KeepDatos(4)    
    def alitas(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.KeepDatos(5)    
    def burger(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.KeepDatos(6)
    def chorizo(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.KeepDatos(7)
    def higado(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.KeepDatos(8)

#v5=Carnes(700,700)
#v5.menuC() 

