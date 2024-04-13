from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import messagebox
import FrutasVerduras as Fv
import Comprobante as Fc
import Menu
import os

class lacteos(Fv.frutas):
    def __init__(self, ancho, alto):
        super().__init__(ancho, alto)
        self.pricesL= [12000,7000,13300,5200,11300,7500,7500,7200,3550]

    def retorno(self):
        if os.path.isfile("precios.txt"):
            if self.preciosl.closed == False:
                self.preciosl.close() 
            else:
                pass
        else:
            pass
        self.ventana.destroy()
        mp= Menu.MenuP(900,600)
        mp.catalogo()  
        
    def SaveDatos(self,index):
        self.preciosl= open("precios.txt","a")
        self.preciosl.write(f"{self.pricesL[index]}\n")
    
    def finish(self):
        if os.path.isfile("precios.txt"):
            if self.preciosl.closed == False:
                self.preciosl.close()
            else:
                pass
            self.ventana.destroy()
            v6= Fc.facturacion(900,700)
            v6.facturaCompleta()
        else:
            messagebox.showerror(title="Error Productos",message="No hay productos registrados, ingrese al menos uno")

    
    def menuL(self):
        self.cat2= PhotoImage(file="imagenes/catL.png")
        self.ventana.geometry(str(self.ancho)+"x"+str(self.alto)) 
        self.ventana.resizable(width=0,height=0)
        self.ventana.title("Lácteos")
        self.logo= tk.Label(image=self.cat2, bd=0)
        self.logo.place(x=0,y=0)
        self.b011= tk.Button(image=self.devolver,command= self.retorno,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b011.place(x=27,y=21)
        self.b02= tk.Button(image=self.finalizar,command= self.finish,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b02.place(x=550,y=21)
        #11
        self.b1= tk.Button(image=self.add,command=self.quesoPar,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b1.place(x=101,y=291)
        #12
        self.b2= tk.Button(image=self.add,command=self.quesoCamp,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b2.place(x=308,y=291)
        #13
        self.b3= tk.Button(image=self.add,command=self.yogurt,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b3.place(x=516,y=291)
        #21
        self.b4= tk.Button(image=self.add,command=self.cremaLeche,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b4.place(x=102,y=469)
        #22
        self.b5= tk.Button(image=self.add,command=self.quesoPera,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b5.place(x=307,y=469)
        #23
        self.b6= tk.Button(image=self.add,command=self.kumis,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b6.place(x=517,y=469)
        #31
        self.b7= tk.Button(image=self.add,command=self.mantequilla,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b7.place(x=102,y=646)
        #32
        self.b8= tk.Button(image=self.add,command=self.lecheDes,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b8.place(x=307,y=646)
        #33
        self.b7= tk.Button(image=self.add,command=self.lecheEnt,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b7.place(x=519,y=646)
        self.ventana.mainloop()
    
    def quesoPar(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.SaveDatos(0)
    def quesoCamp(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.SaveDatos(1)    
    def yogurt(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.SaveDatos(2)    
    def cremaLeche(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.SaveDatos(3)    
    def quesoPera(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.SaveDatos(4)    
    def kumis(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.SaveDatos(5)    
    def mantequilla(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.SaveDatos(6)
    def lecheDes(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.SaveDatos(7)
    def lecheEnt(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.SaveDatos(8)

#v4=lacteos(700,700)
#v4.menuL() 

