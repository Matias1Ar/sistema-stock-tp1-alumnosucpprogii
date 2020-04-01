from tkinter import Tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

listaTipo=("Papeleria","Supermercado","Drogueria")

#IVA
papel=16/100
super=4/100
drog=12/100

#variables Izquierda Superior
tipo1=listaTipo[0]
cantBod1=18
cantMin1=5
precio1=10
cantVen1=0
venta1=0

#variables Derecha Superior
tipo2=listaTipo[2]
cantBod2=7
cantMin2=8
precio2=50
cantVen2=0
venta2=0

#variables Izquierda Inferior
tipo3=listaTipo[0]
cantBod3=9
cantMin3=10
precio3=5
cantVen3=0
venta3=0

#variables Derecha Inferior
tipo4=listaTipo[1]
cantBod4=19
cantMin4=20
precio4=15
cantVen4=0
venta4=0

#ventana
ventana=Tk()
ventana.title("Trabajo Practico")
ventana.geometry("800x620")

#canvas titulo
tit=Canvas(ventana,width=794,height=70, borderwidth=2,relief="raised")
tit.create_rectangle(0,0,900,900)
tit.place(x=0,y=0)

#canvas e imagen izquiera superior
izqSup=Canvas(ventana,width=395,height=230, borderwidth=2,relief="raised")
izqSup.create_rectangle(0,0,900,900)
izqSup.place(x=0,y=75)

imageEx1=PhotoImage(file="001-pencil.png")
Label(ventana,image=imageEx1).place(x=40,y=140)

#canvas e imagen derecha superior
derSup=Canvas(ventana,width=394,height=230, borderwidth=2,relief="raised")
derSup.create_rectangle(0,0,900,900)
derSup.place(x=400,y=75)

imageEx2=PhotoImage(file="002-meds.png")
Label(ventana,image=imageEx2).place(x=440,y=140)

#canvas e imagen izquiera inferior
izqInf=Canvas(ventana,width=395,height=230, borderwidth=2,relief="raised")
izqInf.create_rectangle(0,0,900,900)
izqInf.place(x=0,y=310)

imageEx3=PhotoImage(file="003-eraser.png")
Label(ventana,image=imageEx3).place(x=40,y=380)

#canvas e imagen derecha inferior
derInf=Canvas(ventana,width=394,height=230, borderwidth=2,relief="raised")
derInf.create_rectangle(0,0,900,900)
derInf.place(x=400,y=310)

imageEx4=PhotoImage(file="004-flat-bread.png")
Label(ventana,image=imageEx4).place(x=440,y=380)

#canvas botones inferiores
botInf=Canvas(ventana,width=794,height=70, borderwidth=2,relief="raised")
botInf.create_rectangle(0,0,900,900)
botInf.place(x=0,y=545)

#titulo
titulo=Label(ventana, text="Tienda", font=("Times New Roman",36,"bold"),fg="black")
titulo.place(x=320,y=3)

#funcion abastecer Izquierda Superior
def abastecerIzqSup():
    global cantBod1
    global cantMin1
    def guardar():
        global cantBod1
        cantBod1+=int(cantCambTxt.get())
        resul2IzqSup.configure(text=cantBod1)
        messagebox.showinfo(title="Advertencia",message=("Se ha Guardado Correctamente"))
    if cantBod1>cantMin1:
        messagebox.showinfo(title="Advertencia",message=("La cantidad en la bodega todavia no es menor a la minima"))
    else:
        ventanaAbastecer=Tk()
        ventanaAbastecer.title("Abastecer")
        ventanaAbastecer.geometry("400x90")
        
        cantCamb=Label(ventanaAbastecer, text="Cantidad para Abastecer:", font=("Arial",12), fg="black")
        cantCamb.place(x=0,y=10)
        cantCambTxt=Entry(ventanaAbastecer,width=21)
        cantCambTxt.place(x=200,y=11)
        botonCantCamb=Button(ventanaAbastecer,text="Cambiar", font=("Times New Roman",12),width=13,height=1, command=guardar)
        botonCantCamb.place(x=0,y=40)
        
        ventanaAbastecer.mainloop()

#funcion abastecer Derecha Superior
def abastecerDerSup():
    global cantBod2
    global cantMin2
    def guardar():
        global cantBod2
        cantBod2+=int(cantCambTxt.get())
        resul2DerSup.configure(text=cantBod2)
        messagebox.showinfo(title="Advertencia",message=("Se ha Guardado Correctamente"))
    if cantBod2>cantMin2:
        messagebox.showinfo(title="Advertencia",message=("La cantidad en la bodega todavia no es menor a la minima"))
    else:
        ventanaAbastecer=Tk()
        ventanaAbastecer.title("Abastecer")
        ventanaAbastecer.geometry("400x90")
        
        cantCamb=Label(ventanaAbastecer, text="Cantidad para Abastecer:", font=("Arial",12), fg="black")
        cantCamb.place(x=0,y=10)
        cantCambTxt=Entry(ventanaAbastecer,width=21)
        cantCambTxt.place(x=200,y=11)
        botonCantCamb=Button(ventanaAbastecer,text="Cambiar", font=("Times New Roman",12),width=13,height=1, command=guardar)
        botonCantCamb.place(x=0,y=40)
        
        ventanaAbastecer.mainloop()
    
#funcion abastecer Izquierda Inferior
def abastecerIzqInf():
    global cantBod3
    global cantMin3
    def guardar():
        global cantBod3
        cantBod3+=int(cantCambTxt.get())
        resul2IzqInf.configure(text=cantBod3)
        messagebox.showinfo(title="Advertencia",message=("Se ha Guardado Correctamente"))
    if cantBod3>cantMin3:
        messagebox.showinfo(title="Advertencia",message=("La cantidad en la bodega todavia no es menor a la minima"))
    else:
        ventanaAbastecer=Tk()
        ventanaAbastecer.title("Abastecer")
        ventanaAbastecer.geometry("400x90")
        
        cantCamb=Label(ventanaAbastecer, text="Cantidad para Abastecer:", font=("Arial",12), fg="black")
        cantCamb.place(x=0,y=10)
        cantCambTxt=Entry(ventanaAbastecer,width=21)
        cantCambTxt.place(x=200,y=11)
        botonCantCamb=Button(ventanaAbastecer,text="Cambiar", font=("Times New Roman",12),width=13,height=1, command=guardar)
        botonCantCamb.place(x=0,y=40)
        
        ventanaAbastecer.mainloop()
    
#funcion abastecer Derecha Inferior
def abastecerDerInf():
    global cantBod4
    global cantMin4
    def guardar():
        global cantBod4
        cantBod4+=int(cantCambTxt.get())
        resul2DerInf.configure(text=cantBod4)
        messagebox.showinfo(title="Advertencia",message=("Se ha Guardado Correctamente"))
    if cantBod4>cantMin4:
        messagebox.showinfo(title="Advertencia",message=("La cantidad en la bodega todavia no es menor a la minima"))
    else:
        ventanaAbastecer=Tk()
        ventanaAbastecer.title("Abastecer")
        ventanaAbastecer.geometry("400x90")
        
        cantCamb=Label(ventanaAbastecer, text="Cantidad para Abastecer:", font=("Arial",12), fg="black")
        cantCamb.place(x=0,y=10)
        cantCambTxt=Entry(ventanaAbastecer,width=21)
        cantCambTxt.place(x=200,y=11)
        botonCantCamb=Button(ventanaAbastecer,text="Cambiar", font=("Times New Roman",12),width=13,height=1, command=guardar)
        botonCantCamb.place(x=0,y=40)
        
        ventanaAbastecer.mainloop()

#funcion vender Izquierda Superior
def venderIzqSup():
    global cantBod1
    global cantMin1
    global cantVen1
    cantVentaUni=0
    def guardar():
        global cantVen1
        global cantBod1
        cantVen1+=float(cantVentaTxt.get())
        if tipo1==listaTipo[0]:
            venta1=float(cantVen1*(precio1+papel))
        elif tipo1==listaTipo[1]:
            venta1=float(cantVen1*(precio1+super))
        else:
            venta1=float(cantVen1*(precio1+drog))
        if cantBod1>cantVen1:
            cantBod1=int(cantBod1-cantVen1)
        else:
            cantBod1=int(cantVen1-cantBod1)
        resul2IzqSup.configure(text=cantBod1)
        resul3IzqSup.configure(text=(f"$ {venta1}"))
        resul4IzqSup.configure(text=cantVen1)
        messagebox.showinfo(title="Advertencia",message=("Se ha Guardado Correctamente"))
    if cantBod1<cantMin1:
        messagebox.showinfo(title="Advertencia",message=("La cantidad en la bodega es menor a la minima, no se puede realizar la venta"))
    else:
        ventanaVender=Tk()
        ventanaVender.title("Vender")
        ventanaVender.geometry("400x90")
        
        cantVenta=Label(ventanaVender, text="Cantidad para Vender:", font=("Arial",12), fg="black")
        cantVenta.place(x=0,y=10)
        cantVentaTxt=Entry(ventanaVender,width=21)
        cantVentaTxt.place(x=200,y=11)
        botonCantVenta=Button(ventanaVender,text="Vender", font=("Times New Roman",12),width=13,height=1, command=guardar)
        botonCantVenta.place(x=0,y=40)
        
        ventanaVender.mainloop()

#funcion vender Derecha Superior
def venderDerSup():
    global cantBod2
    global cantMin2
    global cantVen2
    cantVentaUni=0
    def guardar():
        global cantVen2
        global cantBod2
        cantVen2+=float(cantVentaTxt.get())
        if tipo2==listaTipo[0]:
            venta2=float(cantVen2*(precio2+papel))
        elif tipo2==listaTipo[1]:
            venta2=float(cantVen2*(precio2+super))
        else:
            venta2=float(cantVen2*(precio2+drog))
        if cantBod2>cantVen2:
            cantBod2=int(cantBod2-cantVen2)
        else:
            cantBod2=int(cantVen2-cantBod2)
        resul2DerSup.configure(text=cantBod2)
        resul3DerSup.configure(text=(f"$ {venta2}"))
        resul4DerSup.configure(text=cantVen2)
        messagebox.showinfo(title="Advertencia",message=("Se ha Guardado Correctamente"))
    if cantBod2<cantMin2:
        messagebox.showinfo(title="Advertencia",message=("La cantidad en la bodega es menor a la minima, no se puede realizar la venta"))
    else:
        ventanaVender=Tk()
        ventanaVender.title("Vender")
        ventanaVender.geometry("400x90")
        
        cantVenta=Label(ventanaVender, text="Cantidad para Vender:", font=("Arial",12), fg="black")
        cantVenta.place(x=0,y=10)
        cantVentaTxt=Entry(ventanaVender,width=21)
        cantVentaTxt.place(x=200,y=11)
        botonCantVenta=Button(ventanaVender,text="Vender", font=("Times New Roman",12),width=13,height=1, command=guardar)
        botonCantVenta.place(x=0,y=40)
        
        ventanaVender.mainloop()
    
#funcion vender Izquierda Inferior
def venderIzqInf():
    global cantBod3
    global cantMin3
    global cantVen3
    cantVentaUni=0
    def guardar():
        global cantVen3
        global cantBod3
        cantVen3+=float(cantVentaTxt.get())
        if tipo3==listaTipo[0]:
            venta3=float(cantVen3*(precio3+papel))
        elif tipo3==listaTipo[1]:
            venta3=float(cantVen3*(precio3+super))
        else:
            venta3=float(cantVen3*(precio3+drog))
        if cantBod3>cantVen3:
            cantBod3=int(cantBod3-cantVen3)
        else:
            cantBod3=int(cantVen3-cantBod3)
        resul2IzqInf.configure(text=cantBod3)
        resul3IzqInf.configure(text=(f"$ {venta3}"))
        resul4IzqInf.configure(text=cantVen3)
        messagebox.showinfo(title="Advertencia",message=("Se ha Guardado Correctamente"))
    if cantBod3<cantMin3:
        messagebox.showinfo(title="Advertencia",message=("La cantidad en la bodega es menor a la minima, no se puede realizar la venta"))
    else:
        ventanaVender=Tk()
        ventanaVender.title("Vender")
        ventanaVender.geometry("400x90")
        
        cantVenta=Label(ventanaVender, text="Cantidad para Vender:", font=("Arial",12), fg="black")
        cantVenta.place(x=0,y=10)
        cantVentaTxt=Entry(ventanaVender,width=21)
        cantVentaTxt.place(x=200,y=11)
        botonCantVenta=Button(ventanaVender,text="Vender", font=("Times New Roman",12),width=13,height=1, command=guardar)
        botonCantVenta.place(x=0,y=40)
        
        ventanaVender.mainloop()

#funcion vender Derecha Inferior
def venderDerInf():
    global cantBod4
    global cantMin4
    global cantVen4
    cantVentaUni=0
    def guardar():
        global cantVen4
        global cantBod4
        cantVen4+=float(cantVentaTxt.get())
        if tipo4==listaTipo[0]:
            venta4=float(cantVen4*(precio4+papel))
        elif tipo4==listaTipo[1]:
            venta4=float(cantVen4*(precio4+super))
        else:
            venta4=float(cantVen4*(precio4+drog))
        if cantBod4>cantVen4:
            cantBod4=int(cantBod4-cantVen4)
        else:
            cantBod4=int(cantVen4-cantBod4)
        resul2IzqSup.configure(text=cantBod4)
        resul3IzqSup.configure(text=(f"$ {venta4}"))
        resul4IzqSup.configure(text=cantVen4)
        messagebox.showinfo(title="Advertencia",message=("Se ha Guardado Correctamente"))
    if cantBod4<cantMin4:
        messagebox.showinfo(title="Advertencia",message=("La cantidad en la bodega es menor a la minima, no se puede realizar la venta"))
    else:
        ventanaVender=Tk()
        ventanaVender.title("Vender")
        ventanaVender.geometry("400x90")
        
        cantVenta=Label(ventanaVender, text="Cantidad para Vender:", font=("Arial",12), fg="black")
        cantVenta.place(x=0,y=10)
        cantVentaTxt=Entry(ventanaVender,width=21)
        cantVentaTxt.place(x=200,y=11)
        botonCantVenta=Button(ventanaVender,text="Vender", font=("Times New Roman",12),width=13,height=1, command=guardar)
        botonCantVenta.place(x=0,y=40)
        
        ventanaVender.mainloop()

def cambiarIzqSup():
    print("hola")

def cambiarDerSup():
    print("hola")

def cambiarIzqInf():
    print("hola")

def cambiarDerInf():
    print("hola")

def productoMasVendido():
    if venta1>venta2 and venta1>venta3 and venta1>venta4:
        messagebox.showinfo(title="Producto Mas Vendido",message=(f"El Producto mas vendido es el {venta1}"))
    elif venta2>venta1 and venta2>venta3 and venta2>venta4:
        messagebox.showinfo(title="Producto Mas Vendido",message=(f"El Producto mas vendido es el {venta2}"))
    elif venta3>venta1 and venta3>venta2 and venta3>venta4:
        messagebox.showinfo(title="Producto Mas Vendido",message=(f"El Producto mas vendido es el {venta3}"))
    else:
        messagebox.showinfo(title="Producto Mas Vendido",message=(f"El Producto mas vendido es el {venta4}"))
    
def productoMenosVendido():
    if venta1<venta2 and venta1<venta3 and venta1<venta4:
        messagebox.showinfo(title="Producto menos Vendido",message=(f"El Producto menos vendido es el {venta1}"))
    elif venta2<venta1 and venta2<venta3 and venta2<venta4:
        messagebox.showinfo(title="Producto menos Vendido",message=(f"El Producto menos vendido es el {venta2}"))
    elif venta3<venta1 and venta3<venta2 and venta3<venta4:
        messagebox.showinfo(title="Producto menos Vendido",message=(f"El Producto menos vendido es el {venta3}"))
    else:
        messagebox.showinfo(title="Producto menos Vendido",message=(f"El Producto menos vendido es el {venta4}"))
    
def promedioVentas():
    ventaProm=int((venta1+venta2+venta3+venta4)/4)
    messagebox.showinfo(title="Promedio de Ventas",message=(f"El promedio de ventas es {ventaProm}"))
    
def dineroEnCaja():
    ventaDinero=int(venta1+venta2+venta3+venta4)
    messagebox.showinfo(title="Dinero Total",message=(f"El dinero total es {ventaDinero}"))

#Informacion Izquierda Superior
tituloProductoIzqSup=Label(ventana, text="Lapiz", font=("Times New Roman",12,"bold"),fg="black")
tituloProductoIzqSup.place(x=10,y=75)

tipo1IzqSup=Label(ventana, text="Tipo:", font=("Arial",12), fg="black")
tipo1IzqSup.place(x=120,y=80)
resul1IzqSup=Label(ventana, text=tipo1, font=("Arial",12), fg="black")
resul1IzqSup.place(x=260,y=80)

tipo2IzqSup=Label(ventana, text="Cantidad Bodega:", font=("Arial",12), fg="black")
tipo2IzqSup.place(x=120,y=120)
resul2IzqSup=Label(ventana, text=cantBod1, font=("Arial",12), fg="black")
resul2IzqSup.place(x=260,y=120)

tipo3IzqSup=Label(ventana, text="Valor Unitario:", font=("Arial",12), fg="black")
tipo3IzqSup.place(x=120,y=160)
resul3IzqSup=Label(ventana, text=(f"$ {venta1}"), font=("Arial",12), fg="black")
resul3IzqSup.place(x=260,y=160)

tipo4IzqSup=Label(ventana, text="Cantidad Vendida:", font=("Arial",12), fg="black")
tipo4IzqSup.place(x=120,y=200)
resul4IzqSup=Label(ventana, text=cantVen1, font=("Arial",12), fg="black")
resul4IzqSup.place(x=260,y=200)

tipo5IzqSup=Label(ventana, text="Cantidad Minima:", font=("Arial",12), fg="black")
tipo5IzqSup.place(x=120,y=240)
resul5IzqSup=Label(ventana, text=cantMin1, font=("Arial",12), fg="black")
resul5IzqSup.place(x=260,y=240)

botonAbastecer=Button(ventana,text="Abastecer", font=("Times New Roman",12),width=13,height=1, command=abastecerIzqSup)
botonAbastecer.place(x=5,y=270)

botonVender=Button(ventana,text="Vender", font=("Times New Roman",12),width=13,height=1, command=venderIzqSup)
botonVender.place(x=135,y=270)

botonCambiar=Button(ventana,text="Cambiar", font=("Times New Roman",12),width=13,height=1, command=cambiarIzqSup)
botonCambiar.place(x=265,y=270)

#Informacion Derecha Superior
tituloProductoDerSup=Label(ventana, text="Aspirina", font=("Times New Roman",12,"bold"),fg="black")
tituloProductoDerSup.place(x=410,y=75)

tipo1DerSup=Label(ventana, text="Tipo:", font=("Arial",12), fg="black")
tipo1DerSup.place(x=510,y=80)
resul1DerSup=Label(ventana, text=tipo2, font=("Arial",12), fg="black")
resul1DerSup.place(x=650,y=80)

tipo2DerSup=Label(ventana, text="Cantidad Bodega:", font=("Arial",12), fg="black")
tipo2DerSup.place(x=510,y=120)
resul2DerSup=Label(ventana, text=cantBod2, font=("Arial",12), fg="black")
resul2DerSup.place(x=650,y=120)

tipo3DerSup=Label(ventana, text="Valor Unitario:", font=("Arial",12), fg="black")
tipo3DerSup.place(x=510,y=160)
resul3DerSup=Label(ventana, text=(f"$ {venta2}"), font=("Arial",12), fg="black")
resul3DerSup.place(x=650,y=160)

tipo4DerSup=Label(ventana, text="Cantidad Vendida:", font=("Arial",12), fg="black")
tipo4DerSup.place(x=510,y=200)
resul4DerSup=Label(ventana, text=cantVen2, font=("Arial",12), fg="black")
resul4DerSup.place(x=650,y=200)

tipo5DerSup=Label(ventana, text="Cantidad Minima:", font=("Arial",12), fg="black")
tipo5DerSup.place(x=510,y=240)
resul5DerSup=Label(ventana, text=cantMin2, font=("Arial",12), fg="black")
resul5DerSup.place(x=650,y=240)

botonAbastecer=Button(ventana,text="Abastecer", font=("Times New Roman",12),width=13,height=1, command=abastecerDerSup)
botonAbastecer.place(x=405,y=270)

botonVender=Button(ventana,text="Vender", font=("Times New Roman",12),width=13,height=1, command=venderDerSup)
botonVender.place(x=535,y=270)

botonCambiar=Button(ventana,text="Cambiar", font=("Times New Roman",12),width=13,height=1, command=cambiarDerSup)
botonCambiar.place(x=665,y=270)

#Informacion Izquierda Inferior
tituloProductoIzqInf=Label(ventana, text="Borrador", font=("Times New Roman",12,"bold"),fg="black")
tituloProductoIzqInf.place(x=10,y=310)

tipo1IzqInf=Label(ventana, text="Tipo:", font=("Arial",12), fg="black")
tipo1IzqInf.place(x=120,y=320)
resul1IzqInf=Label(ventana, text=tipo3, font=("Arial",12), fg="black")
resul1IzqInf.place(x=260,y=320)

tipo2IzqInf=Label(ventana, text="Cantidad Bodega:", font=("Arial",12), fg="black")
tipo2IzqInf.place(x=120,y=360)
resul2IzqInf=Label(ventana, text=cantBod3, font=("Arial",12), fg="black")
resul2IzqInf.place(x=260,y=360)

tipo3IzqInf=Label(ventana, text="Valor Unitario:", font=("Arial",12), fg="black")
tipo3IzqInf.place(x=120,y=400)
resul3IzqInf=Label(ventana, text=venta3, font=("Arial",12), fg="black")
resul3IzqInf.place(x=260,y=400)

tipo4IzqInf=Label(ventana, text="Cantidad Vendida:", font=("Arial",12), fg="black")
tipo4IzqInf.place(x=120,y=440)
resul4IzqInf=Label(ventana, text=cantVen3, font=("Arial",12), fg="black")
resul4IzqInf.place(x=260,y=440)

tipo5IzqInf=Label(ventana, text="Cantidad Minima:", font=("Arial",12), fg="black")
tipo5IzqInf.place(x=120,y=480)
resul5IzqInf=Label(ventana, text=cantMin3, font=("Arial",12), fg="black")
resul5IzqInf.place(x=260,y=480)

botonAbastecer=Button(ventana,text="Abastecer", font=("Times New Roman",12),width=13,height=1, command=abastecerIzqInf)
botonAbastecer.place(x=5,y=504)

botonVender=Button(ventana,text="Vender", font=("Times New Roman",12),width=13,height=1, command=venderIzqInf)
botonVender.place(x=135,y=504)

botonCambiar=Button(ventana,text="Cambiar", font=("Times New Roman",12),width=13,height=1, command=cambiarIzqInf)
botonCambiar.place(x=265,y=504)

#Informacion Derecha Inferior
tituloProductoDerSup=Label(ventana, text="Pan", font=("Times New Roman",12,"bold"),fg="black")
tituloProductoDerSup.place(x=410,y=310)

tipo1DerInf=Label(ventana, text="Tipo:", font=("Arial",12), fg="black")
tipo1DerInf.place(x=510,y=320)
resul1DerInf=Label(ventana, text=tipo4, font=("Arial",12), fg="black")
resul1DerInf.place(x=650,y=320)

tipo2DerInf=Label(ventana, text="Cantidad Bodega:", font=("Arial",12), fg="black")
tipo2DerInf.place(x=510,y=360)
resul2DerInf=Label(ventana, text=cantBod4, font=("Arial",12), fg="black")
resul2DerInf.place(x=650,y=360)

tipo3DerInf=Label(ventana, text="Valor Unitario:", font=("Arial",12), fg="black")
tipo3DerInf.place(x=510,y=400)
resul3DerInf=Label(ventana, text=venta4, font=("Arial",12), fg="black")
resul3DerInf.place(x=650,y=400)

tipo4DerInf=Label(ventana, text="Cantidad Vendida:", font=("Arial",12), fg="black")
tipo4DerInf.place(x=510,y=440)
resul4DerInf=Label(ventana, text=cantVen4, font=("Arial",12), fg="black")
resul4DerInf.place(x=650,y=440)

tipo5DerInf=Label(ventana, text="Cantidad Minima:", font=("Arial",12), fg="black")
tipo5DerInf.place(x=510,y=480)
resul5DerInf=Label(ventana, text=cantMin4, font=("Arial",12), fg="black")
resul5DerInf.place(x=650,y=480)

botonAbastecer=Button(ventana,text="Abastecer", font=("Times New Roman",12),width=13,height=1, command=abastecerDerInf)
botonAbastecer.place(x=405,y=504)

botonVender=Button(ventana,text="Vender", font=("Times New Roman",12),width=13,height=1, command=venderDerInf)
botonVender.place(x=535,y=504)

botonCambiar=Button(ventana,text="Cambiar", font=("Times New Roman",12),width=13,height=1, command=cambiarDerInf)
botonCambiar.place(x=665,y=504)

#Botones Inferiores
botonMasVendido=Button(ventana,text="Producto mas vendido", font=("Times New Roman",12),width=28,height=1, command=productoMasVendido)
botonMasVendido.place(x=5,y=554)

botonMenosVendido=Button(ventana,text="Producto Menos Vendido", font=("Times New Roman",12),width=28,height=1, command=productoMenosVendido)
botonMenosVendido.place(x=269,y=554)

botonPromedio=Button(ventana,text="Promedio Ventas", font=("Times New Roman",12),width=28,height=1, command=promedioVentas)
botonPromedio.place(x=533,y=554)

botonDineroEnCaja=Button(ventana,text="Dinero en Caja", font=("Times New Roman",12),width=28,height=1, command=dineroEnCaja)
botonDineroEnCaja.place(x=269,y=588)

opcionesEdad=ttk.Combobox(ventana)

ventana.mainloop()
