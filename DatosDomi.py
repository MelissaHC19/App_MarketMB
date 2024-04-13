from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
import tkinter as tk
from DatosRT import DatosR
import Menu

class DatosD(DatosR):
    def __init__(self, ancho, alto):
        super().__init__(ancho, alto)

    def geT(self):
        nombre= self.nombre.get()
        docu= self.documento.get()
        tel= self.celular.get()
        ciudad= self.ciudad.get()
        direccion= self.direccion.get() 
        horasdispo= self.horasDisp.get()       
        if nombre == "" or docu == "" or tel == "" or ciudad == "" or direccion == "" or horasdispo == "":
            messagebox.showerror(message="Hay campos sin llenar",title="Fields Error")  
        else:
            messagebox.showinfo(message="Datos ingresados satisfactoriamente",title="Info")
            miArch= 'recolecta.txt'
            self.f= open(miArch,"a")
            self.f.write(f"{nombre}\n{ciudad}\n{docu}\n{tel}\n{horasdispo}\nDomicilio")
            self.ventana.destroy()
            self.f.close()
            mp= Menu.MenuP(900,600)
            mp.catalogo()        
    
    def DatosDm(self):
        self.ventana.geometry(str(self.ancho)+"x"+str(self.alto))
        self.ventana.config(bg=('#f5f5cb'))
        self.ventana.resizable(width=0,height=0)
        self.ventana.title("Registrar Datos Domicilio")
        self.ingresar= PhotoImage(file="imagenes/ingreseDatos.png")
        self.logo= tk.Label(image=self.MB, bd=0)
        self.logo.place(x=200,y=0)
        self.InDat= tk.Label(image=self.ingresar,bd=0)
        self.InDat.place(x=200,y=285)
        #Nombre
        self.labNom= Label(self.ventana,text="Ingrese su nombre completo: ", font=("Lucida Sans Unicode",13),background=('#f5f5cb')).place(x=100,y=350)
        self.nombre= ttk.Entry(self.ventana,width=25,font=("Tahoma"))
        self.nombre.place(x=370,y=350)
        #Documento
        self.labDoc= Label(self.ventana,text="Ingrese su documento: ", font=("Lucida Sans Unicode",13),background=('#f5f5cb')).place(x=100,y=390)
        self.documento= ttk.Entry(self.ventana,width=15,font=("Tahoma"))
        self.documento.place(x=370,y=390)
        #Celular
        self.labCel= Label(self.ventana,text="Ingrese su celular: ", font=("Lucida Sans Unicode",13),background=('#f5f5cb')).place(x=100,y=430)
        self.celular= ttk.Entry(self.ventana,width=15,font=("Tahoma"))
        self.celular.place(x=370,y=430)
        #Ciudad
        self.labCiu= Label(self.ventana,text="Seleccione su ciudad: ", font=("Lucida Sans Unicode",13),background=('#f5f5cb')).place(x=100,y=470)
        self.ciudad= Combobox(self.ventana,values=("Pereira","Dosquebradas","La Virginia"),font=("Tahoma"),state="readonly")
        self.ciudad.place(x=370,y=470)
        #Dirección
        self.labDir= Label(self.ventana,text="Ingrese su dirección: ", font=("Lucida Sans Unicode",13),background=('#f5f5cb')).place(x=100,y=510)
        self.direccion= ttk.Entry(self.ventana,width=25,font=("Tahoma"))
        self.direccion.place(x=370,y=510)
        #Hora
        self.labHoras= Label(self.ventana,text="Hora de entrega: ", font=("Lucida Sans Unicode",13),background=('#f5f5cb')).place(x=100,y=550)
        self.horasDisp= ttk.Combobox(self.ventana,values=("11:00 AM","12:00 M","1:00 PM","2:00 PM","3:00 PM","4:00 PM"),font=("Tahoma"),width=13,state="readonly")
        self.horasDisp.place(x=370,y=550)
        #Boton
        self.buton= tk.Button(self.ventana, text="Registrar y continuar", font=("Tahoma", 12),command=self.geT,relief="flat", overrelief="raised",bg=("#aad450"),borderwidth=3,cursor="hand2")
        self.buton.place(x=260,y=600)
        self.ventana.mainloop()
        return self.ventana
