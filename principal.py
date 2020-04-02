from tkinter import *
from tkinter import messagebox

window = Tk()
window.resizable(0,0)
window.title("Programación II - Sistema Stock - Super Rugby")
window.geometry('775x543')

#Funciones Cambiar

def cambiar1():
    cambio = Tk()
    cambio.resizable(0,0)
    cambio.title("Cambiar Informacion")
    cambio.geometry('282x242')

    def realizar():
        producro = producto_cambio.get()
        tipo = tipo_cambio.get()
        cantidad = cantidad_cambio.get()
        valor = valor_cambio.get()
        minim = minima_cambio.get()
        lapiz.configure(text=producro)
        valor_tipo.configure(text=tipo)
        valor_cantidad.configure(text=cantidad)
        valor_valor.configure(text=valor)
        valor_minima.configure(text=minim)
        valor_vendidas.configure(text="0")

        cambio.destroy()

    estetico = Canvas(cambio, width=275, height=180, borderwidth=2, bg='#EEEEEE', relief='raised').place(x=0, y=0)
    estetico1 = Canvas(cambio, width=275, height=50, borderwidth=2, bg='#EEEEEE', relief='raised').place(x=0, y=185)

    producto = Label(cambio, text="Producto:", font=("Arial", 11), borderwidth=2, width=13, relief="groove").place(x=10, y=10)
    producto_cambio = Entry(cambio, width=19)
    producto_cambio.place(x=150, y=13)
    tipo = Label(cambio, text="Tipo:", font=("Arial", 11), borderwidth=2, width=13, relief="groove").place(x=10, y=45)
    tipo_cambio = Entry(cambio, width=19)
    tipo_cambio.place(x=150, y=49)
    cantidad = Label(cambio, text="Cantidad Bodega:", font=("Arial", 11), borderwidth=2, width=13, relief="groove").place(x=10, y=80)
    cantidad_cambio = Entry(cambio, width=19)
    cantidad_cambio.place(x=150, y=83)
    valor = Label(cambio, text="Valor Unitario:", font=("Arial", 11), borderwidth=2, width=13, relief="groove").place(x=10, y=115)
    valor_cambio = Entry(cambio, width=19)
    valor_cambio.place(x=150, y=119)
    minima = Label(cambio, text="Cantidad Minima:", font=("Arial", 11), borderwidth=2, width=13, relief="groove").place(x=10, y=150)
    minima_cambio = Entry(cambio, width=19)
    minima_cambio.place(x=150, y=153)

    cambiar = Button(cambio, text="Modificar", font=("Arial", 10), width = 19, borderwidth=2, relief="raised", bg="#EEEEEE", cursor="hand2", command=realizar)
    cambiar.place(x=60, y=200)

    cambio.mainloop()

def cambiar2():
    cambio = Tk()
    cambio.resizable(0,0)
    cambio.title("Cambiar Informacion")
    cambio.geometry('282x242')

    def realizar():
        producro = producto_cambio.get()
        tipo = tipo_cambio.get()
        cantidad = cantidad_cambio.get()
        valor = valor_cambio.get()
        minim = minima_cambio.get()
        aspirina.configure(text=producro)
        valor_tipo1.configure(text=tipo)
        valor_cantidad1.configure(text=cantidad)
        valor_valor1.configure(text=valor)
        valor_minima1.configure(text=minim)
        valor_vendidas1.configure(text="0")

        cambio.destroy()

    estetico = Canvas(cambio, width=275, height=180, borderwidth=2, bg='#EEEEEE', relief='raised').place(x=0, y=0)
    estetico1 = Canvas(cambio, width=275, height=50, borderwidth=2, bg='#EEEEEE', relief='raised').place(x=0, y=185)

    producto = Label(cambio, text="Producto:", font=("Arial", 11), borderwidth=2, width=13, relief="groove").place(x=10, y=10)
    producto_cambio = Entry(cambio, width=19)
    producto_cambio.place(x=150, y=13)
    tipo = Label(cambio, text="Tipo:", font=("Arial", 11), borderwidth=2, width=13, relief="groove").place(x=10, y=45)
    tipo_cambio = Entry(cambio, width=19)
    tipo_cambio.place(x=150, y=49)
    cantidad = Label(cambio, text="Cantidad Bodega:", font=("Arial", 11), borderwidth=2, width=13, relief="groove").place(x=10, y=80)
    cantidad_cambio = Entry(cambio, width=19)
    cantidad_cambio.place(x=150, y=83)
    valor = Label(cambio, text="Valor Unitario:", font=("Arial", 11), borderwidth=2, width=13, relief="groove").place(x=10, y=115)
    valor_cambio = Entry(cambio, width=19)
    valor_cambio.place(x=150, y=119)
    minima = Label(cambio, text="Cantidad Minima:", font=("Arial", 11), borderwidth=2, width=13, relief="groove").place(x=10, y=150)
    minima_cambio = Entry(cambio, width=19)
    minima_cambio.place(x=150, y=153)

    cambiar = Button(cambio, text="Modificar", font=("Arial", 10), width = 19, borderwidth=2, relief="raised", bg="#EEEEEE", cursor="hand2", command=realizar)
    cambiar.place(x=60, y=200)

    cambio.mainloop()

def cambiar3():
    cambio = Tk()
    cambio.resizable(0,0)
    cambio.title("Cambiar Informacion")
    cambio.geometry('282x242')

    def realizar():
        producro = producto_cambio.get()
        tipo = tipo_cambio.get()
        cantidad = cantidad_cambio.get()
        valor = valor_cambio.get()
        minim = minima_cambio.get()
        borrador.configure(text=producro)
        valor_tipo2.configure(text=tipo)
        valor_cantidad2.configure(text=cantidad)
        valor_valor2.configure(text=valor)
        valor_minima2.configure(text=minim)
        valor_vendidas2.configure(text="0")

        cambio.destroy()

    estetico = Canvas(cambio, width=275, height=180, borderwidth=2, bg='#EEEEEE', relief='raised').place(x=0, y=0)
    estetico1 = Canvas(cambio, width=275, height=50, borderwidth=2, bg='#EEEEEE', relief='raised').place(x=0, y=185)

    producto = Label(cambio, text="Producto:", font=("Arial", 11), borderwidth=2, width=13, relief="groove").place(x=10, y=10)
    producto_cambio = Entry(cambio, width=19)
    producto_cambio.place(x=150, y=13)
    tipo = Label(cambio, text="Tipo:", font=("Arial", 11), borderwidth=2, width=13, relief="groove").place(x=10, y=45)
    tipo_cambio = Entry(cambio, width=19)
    tipo_cambio.place(x=150, y=49)
    cantidad = Label(cambio, text="Cantidad Bodega:", font=("Arial", 11), borderwidth=2, width=13, relief="groove").place(x=10, y=80)
    cantidad_cambio = Entry(cambio, width=19)
    cantidad_cambio.place(x=150, y=83)
    valor = Label(cambio, text="Valor Unitario:", font=("Arial", 11), borderwidth=2, width=13, relief="groove").place(x=10, y=115)
    valor_cambio = Entry(cambio, width=19)
    valor_cambio.place(x=150, y=119)
    minima = Label(cambio, text="Cantidad Minima:", font=("Arial", 11), borderwidth=2, width=13, relief="groove").place(x=10, y=150)
    minima_cambio = Entry(cambio, width=19)
    minima_cambio.place(x=150, y=153)

    cambiar = Button(cambio, text="Modificar", font=("Arial", 10), width = 19, borderwidth=2, relief="raised", bg="#EEEEEE", cursor="hand2", command=realizar)
    cambiar.place(x=60, y=200)

    cambio.mainloop()

def cambiar4():
    cambio = Tk()
    cambio.resizable(0,0)
    cambio.title("Cambiar Informacion")
    cambio.geometry('282x242')

    def realizar():
        producro = producto_cambio.get()
        tipo = tipo_cambio.get()
        cantidad = cantidad_cambio.get()
        valor = valor_cambio.get()
        minim = minima_cambio.get()
        pan.configure(text=producro)
        valor_tipo3.configure(text=tipo)
        valor_cantidad3.configure(text=cantidad)
        valor_valor3.configure(text=valor)
        valor_minima3.configure(text=minim)
        valor_vendidas3.configure(text="0")

        cambio.destroy()

    estetico = Canvas(cambio, width=275, height=180, borderwidth=2, bg='#EEEEEE', relief='raised').place(x=0, y=0)
    estetico1 = Canvas(cambio, width=275, height=50, borderwidth=2, bg='#EEEEEE', relief='raised').place(x=0, y=185)

    producto = Label(cambio, text="Producto:", font=("Arial", 11), borderwidth=2, width=13, relief="groove").place(x=10, y=10)
    producto_cambio = Entry(cambio, width=19)
    producto_cambio.place(x=150, y=13)
    tipo = Label(cambio, text="Tipo:", font=("Arial", 11), borderwidth=2, width=13, relief="groove").place(x=10, y=45)
    tipo_cambio = Entry(cambio, width=19)
    tipo_cambio.place(x=150, y=49)
    cantidad = Label(cambio, text="Cantidad Bodega:", font=("Arial", 11), borderwidth=2, width=13, relief="groove").place(x=10, y=80)
    cantidad_cambio = Entry(cambio, width=19)
    cantidad_cambio.place(x=150, y=83)
    valor = Label(cambio, text="Valor Unitario:", font=("Arial", 11), borderwidth=2, width=13, relief="groove").place(x=10, y=115)
    valor_cambio = Entry(cambio, width=19)
    valor_cambio.place(x=150, y=119)
    minima = Label(cambio, text="Cantidad Minima:", font=("Arial", 11), borderwidth=2, width=13, relief="groove").place(x=10, y=150)
    minima_cambio = Entry(cambio, width=19)
    minima_cambio.place(x=150, y=153)

    cambiar = Button(cambio, text="Modificar", font=("Arial", 10), width = 19, borderwidth=2, relief="raised", bg="#EEEEEE", cursor="hand2", command=realizar)
    cambiar.place(x=60, y=200)

    cambio.mainloop()

def venta():
    valor = int(valor_vendidas.cget("text"))
    cantidad = int(valor_cantidad.cget("text"))
    resta = str(cantidad-1)
    valor_total = str(valor+1)
    valor_vendidas.configure(text=valor_total)
    valor_cantidad.configure(text=resta)
    if resta<="0":
        valor_vendidas.configure(text=valor)
        valor_cantidad.configure(text="0")
        messagebox.showinfo(title="Alerta", message="No tiene stock del producto")


def venta1():
    valor = int(valor_vendidas1.cget("text"))
    cantidad = int(valor_cantidad1.cget("text"))
    resta = str(cantidad-1)
    valor_total = str(valor+1)
    valor_vendidas1.configure(text=valor_total)
    valor_cantidad1.configure(text=resta)
    if resta<="0":
        valor_vendidas1.configure(text=valor)
        valor_cantidad1.configure(text="0")
        messagebox.showinfo(title="Alerta", message="No tiene stock del producto")

def venta2():
    valor = int(valor_vendidas2.cget("text"))
    cantidad = int(valor_cantidad2.cget("text"))
    resta = str(cantidad-1)
    valor_total = str(valor+1)
    valor_vendidas2.configure(text=valor_total)
    valor_cantidad2.configure(text=resta)
    if resta<="0":
        valor_vendidas2.configure(text=valor)
        valor_cantidad2.configure(text="0")
        messagebox.showinfo(title="Alerta", message="No tiene stock del producto")

def venta3():
    valor = int(valor_vendidas3.cget("text"))
    cantidad = int(valor_cantidad3.cget("text"))
    resta = str(cantidad-1)
    valor_total = str(valor+1)
    valor_vendidas3.configure(text=valor_total)
    valor_cantidad3.configure(text=resta)
    if resta<="0":
        valor_vendidas3.configure(text=valor)
        valor_cantidad3.configure(text="0")
        messagebox.showinfo(title="Alerta", message="No tiene stock del producto")

def abastecer():
    valor = int(valor_cantidad.cget("text"))
    minima = int(valor_minima.cget("text"))
    suma = str(valor+minima)
    valor_cantidad.configure(text=suma)

def abastecer1():
    valor = int(valor_cantidad1.cget("text"))
    minima = int(valor_minima1.cget("text"))
    suma = str(valor+minima)
    valor_cantidad1.configure(text=suma)

def abastecer2():
    valor = int(valor_cantidad2.cget("text"))
    minima = int(valor_minima2.cget("text"))
    suma = str(valor+minima)
    valor_cantidad2.configure(text=suma)

def abastecer3():
    valor = int(valor_cantidad3.cget("text"))
    minima = int(valor_minima3.cget("text"))
    suma = str(valor+minima)
    valor_cantidad3.configure(text=suma)

def mas_vendido():
    valor1 = int(valor_vendidas.cget("text"))
    valor2 = int(valor_vendidas1.cget("text"))
    valor3 = int(valor_vendidas2.cget("text"))
    valor4 = int(valor_vendidas3.cget("text"))
    lapiz1 = str(lapiz.cget("text"))
    aspirina1 = str(aspirina.cget("text"))
    borrador1 = str(borrador.cget("text"))
    pan1 = str(pan.cget("text"))
    if valor1>valor2 and valor1>valor3 and valor1>valor4:
        messagebox.showinfo(title="Opcion", message="El producto mas vendido es: "+lapiz1)
    elif valor2>valor1 and valor2>valor3 and valor2>valor4:
        messagebox.showinfo(title="Opcion", message="El producto mas vendido es: "+aspirina1)
    elif valor3>valor1 and valor3>valor2 and valor3>valor4:
        messagebox.showinfo(title="Opcion", message="El producto mas vendido es: "+borrador1)
    else:
        messagebox.showinfo(title="Opcion", message="El producto mas vendido es: "+pan1)

def menos_vendido():
    valor1 = int(valor_vendidas.cget("text"))
    valor2 = int(valor_vendidas1.cget("text"))
    valor3 = int(valor_vendidas2.cget("text"))
    valor4 = int(valor_vendidas3.cget("text"))
    lapiz1 = str(lapiz.cget("text"))
    aspirina1 = str(aspirina.cget("text"))
    borrador1 = str(borrador.cget("text"))
    pan1 = str(pan.cget("text"))
    if valor1<valor2 and valor1<valor3 and valor1<valor4:
        messagebox.showinfo(title="Opcion", message="El producto menos vendido es: "+lapiz1)
    elif valor2<valor1 and valor2<valor3 and valor2<valor4:
        messagebox.showinfo(title="Opcion", message="El producto menos vendido es: "+aspirina1)
    elif valor3<valor1 and valor3<valor2 and valor3<valor4:
        messagebox.showinfo(title="Opcion", message="El producto menos vendido es: "+borrador1)
    else:
        messagebox.showinfo(title="Opcion", message="El producto menos vendido es: "+pan1)

def promedio():
    valor1 = float(valor_vendidas.cget("text"))
    valor2 = float(valor_vendidas1.cget("text"))
    valor3 = float(valor_vendidas2.cget("text"))
    valor4 = float(valor_vendidas3.cget("text"))
    precio1 = float(valor_valor.cget("text"))
    precio2 = float(valor_valor1.cget("text"))
    precio3 = float(valor_valor2.cget("text"))
    precio4 = float(valor_valor3.cget("text"))
    resultado1 = (precio1*valor1)
    resultado2 = (precio2*valor2)
    resultado3 = (precio3*valor3)
    resultado4 = (precio4*valor4)
    prom = ((resultado1+resultado2+resultado3+resultado4)/4)
    messagebox.showinfo(title="Promedio", message="El promedio es: "+str(prom))

def caja():
    valor1 = float(valor_vendidas.cget("text"))
    valor2 = float(valor_vendidas1.cget("text"))
    valor3 = float(valor_vendidas2.cget("text"))
    valor4 = float(valor_vendidas3.cget("text"))
    precio1 = float(valor_valor.cget("text"))
    precio2 = float(valor_valor1.cget("text"))
    precio3 = float(valor_valor2.cget("text"))
    precio4 = float(valor_valor3.cget("text"))
    resultado1 = (precio1*valor1)
    resultado2 = (precio2*valor2)
    resultado3 = (precio3*valor3)
    resultado4 = (precio4*valor4)
    prom = (resultado1+resultado2+resultado3+resultado4)
    messagebox.showinfo(title="Promedio", message="$"+str(prom))

#Cuadros Esteticos
cuadro_lapiz = Canvas(window, width=378, height=212, borderwidth=2, bg='#EEEEEE', relief='raised').place(x=0, y=10)
cuadro_aspirina = Canvas(window, width=378, height=212, borderwidth=2, bg='#EEEEEE', relief='raised').place(x=390, y=10)
cuadro_lapiz = Canvas(window, width=378, height=212, borderwidth=2, bg='#EEEEEE', relief='raised').place(x=0, y=240)
cuadro_pan = Canvas(window, width=378, height=212, borderwidth=2, bg='#EEEEEE', relief='raised').place(x=390, y=240)
cuadro_opciones = Canvas(window, width=768, height=65, borderwidth=2, bg='#EEEEEE', relief='raised').place(x=0, y=470)

#Productos
    #Lapiz
lapiz = Label(window, text="Lapiz", font="Arial")
lapiz.place(x=0, y=0)
tipo = Label(window, text="Tipo:", font=("Arial", 11))
tipo.place(x=90, y=25)
cantidad = Label(window, text="Cantidad Bodega:", font=("Arial", 11))
cantidad.place(x=90, y=55)
valor = Label(window, text="Valor Unitario:", font=("Arial", 11))
valor.place(x=90, y=85)
vendidas = Label(window, text="Cantidad Vendidas:", font=("Arial", 11))
vendidas.place(x=90, y=115)
minima = Label(window, text="Cantidad Minima:", font=("Arial", 11))
minima.place(x=90, y=145)
    #Aspirina
aspirina = Label(window, text="Aspirina", font="Arial")
aspirina.place(x=390, y=0)
tipo1 = Label(window, text="Tipo:", font=("Arial", 11))
tipo1.place(x=480, y=25)
cantidad1 = Label(window, text="Cantidad Bodega:", font=("Arial", 11))
cantidad1.place(x=480, y=55)
valor1 = Label(window, text="Valor Unitario:", font=("Arial", 11))
valor1.place(x=480, y=85)
vendidas1 = Label(window, text="Cantidad Vendidas:", font=("Arial", 11))
vendidas1.place(x=480, y=115)
minima1 = Label(window, text="Cantidad Minima:", font=("Arial", 11))
minima1.place(x=480, y=145)
    #Borrador
borrador = Label(window, text="Borrador", font="Arial")
borrador.place(x=0, y=230)
tipo2 = Label(window, text="Tipo:", font=("Arial", 11))
tipo2.place(x=90, y=255)
cantidad2 = Label(window, text="Cantidad Bodega:", font=("Arial", 11))
cantidad2.place(x=90, y=285)
valor2 = Label(window, text="Valor Unitario:", font=("Arial", 11))
valor2.place(x=90, y=315)
vendidas2 = Label(window, text="Cantidad Vendidas:", font=("Arial", 11))
vendidas2.place(x=90, y=345)
minima2 = Label(window, text="Cantidad Minima:", font=("Arial", 11))
minima2.place(x=90, y=375)
    #Pan
pan = Label(window, text="Pan", font="Arial")
pan.place(x=390, y=230)
tipo3 = Label(window, text="Tipo:", font=("Arial", 11))
tipo3.place(x=480, y=255)
cantidad3 = Label(window, text="Cantidad Bodega:", font=("Arial", 11))
cantidad3.place(x=480, y=285)
valor3 = Label(window, text="Valor Unitario:", font=("Arial", 11))
valor3.place(x=480, y=315)
vendidas3 = Label(window, text="Cantidad Vendidas:", font=("Arial", 11))
vendidas3.place(x=480, y=345)
minima3 = Label(window, text="Cantidad Minima:", font=("Arial", 11))
minima3.place(x=480, y=375)

#Productos Variables
    #Lapiz
valor_tipo = Label(window, text="Papeleria", font=("Arial", 11), borderwidth=2, width=14, relief="groove")
valor_tipo.place(x=230, y=25)
valor_cantidad = Label(window, text="18", font=("Arial", 11), borderwidth=2, width=14, relief="groove")
valor_cantidad.place(x=230, y=55)
valor_valor = Label(window, text="20.0", font=("Arial", 11), borderwidth=2, width=14, relief="groove")
valor_valor.place(x=230, y=85)
valor_vendidas = Label(window, text="0", font=("Arial", 11), borderwidth=2, width=14, relief="groove")
valor_vendidas.place(x=230, y=115)
valor_minima = Label(window, text="5", font=("Arial", 11), borderwidth=2, width=14, relief="groove")
valor_minima.place(x=230, y=145)
    #Aspirina
valor_tipo1 = Label(window, text="Drogueria", font=("Arial", 11), borderwidth=2, width=14, relief="groove")
valor_tipo1.place(x=620, y=25)
valor_cantidad1 = Label(window, text="25", font=("Arial", 11), borderwidth=2, width=14, relief="groove")
valor_cantidad1.place(x=620, y=55)
valor_valor1 = Label(window, text="50.0", font=("Arial", 11), borderwidth=2, width=14, relief="groove")
valor_valor1.place(x=620, y=85)
valor_vendidas1 = Label(window, text="0", font=("Arial", 11), borderwidth=2, width=14, relief="groove")
valor_vendidas1.place(x=620, y=115)
valor_minima1 = Label(window, text="8", font=("Arial", 11), borderwidth=2, width=14, relief="groove")
valor_minima1.place(x=620, y=145)
    #Borrador
valor_tipo2 = Label(window, text="Papeleria", font=("Arial", 11), borderwidth=2, width=14, relief="groove")
valor_tipo2.place(x=230, y=255)
valor_cantidad2 = Label(window, text="30", font=("Arial", 11), borderwidth=2, width=14, relief="groove")
valor_cantidad2.place(x=230, y=285)
valor_valor2 = Label(window, text="10.0", font=("Arial", 11), borderwidth=2, width=14, relief="groove")
valor_valor2.place(x=230, y=315)
valor_vendidas2 = Label(window, text="0", font=("Arial", 11), borderwidth=2, width=14, relief="groove")
valor_vendidas2.place(x=230, y=345)
valor_minima2 = Label(window, text="10", font=("Arial", 11), borderwidth=2, width=14, relief="groove")
valor_minima2.place(x=230, y=375)
    #Pan
valor_tipo3 = Label(window, text="Supermercado", font=("Arial", 11), borderwidth=2, width=14, relief="groove")
valor_tipo3.place(x=620, y=255)
valor_cantidad3 = Label(window, text="15", font=("Arial", 11), borderwidth=2, width=14, relief="groove")
valor_cantidad3.place(x=620, y=285)
valor_valor3 = Label(window, text="45.0", font=("Arial", 11), borderwidth=2, width=14, relief="groove")
valor_valor3.place(x=620, y=315)
valor_vendidas3 = Label(window, text="0", font=("Arial", 11), borderwidth=2, width=14, relief="groove")
valor_vendidas3.place(x=620, y=345)
valor_minima3 = Label(window, text="20", font=("Arial", 11), borderwidth=2, width=14, relief="groove")
valor_minima3.place(x=620, y=375)

#Botones
    #Lapiz
abastecer = Button(window, text="Abastecer", font=("Arial", 10), width = 13, borderwidth=2, relief="raised", bg="#EEEEEE", cursor="hand2", command=abastecer)
abastecer.place(x=10, y=190)
vender = Button(window, text="Vender", font=("Arial", 10), width = 13, borderwidth=2, relief="raised", bg="#EEEEEE", cursor="hand2", command=venta)
vender.place(x=135, y=190)
cambiar = Button(window, text="Cambiar", font=("Arial", 10), width = 13, borderwidth=2, relief="raised", bg="#EEEEEE", cursor="hand2", command=cambiar1)
cambiar.place(x=260, y=190)
    #Aspirina
abastecer1 = Button(window, text="Abastecer", font=("Arial", 10), width = 13, borderwidth=2, relief="raised", bg="#EEEEEE", cursor="hand2", command=abastecer1)
abastecer1.place(x=400, y=190)
vender1 = Button(window, text="Vender", font=("Arial", 10), width = 13, borderwidth=2, relief="raised", bg="#EEEEEE", cursor="hand2", command=venta1)
vender1.place(x=525, y=190)
cambiar1 = Button(window, text="Cambiar", font=("Arial", 10), width = 13, borderwidth=2, relief="raised", bg="#EEEEEE", cursor="hand2", command=cambiar2)
cambiar1.place(x=650, y=190)
    #Borrador
abastecer2 = Button(window, text="Abastecer", font=("Arial", 10), width = 13, borderwidth=2, relief="raised", bg="#EEEEEE", cursor="hand2", command=abastecer2)
abastecer2.place(x=10, y=420)
vender2 = Button(window, text="Vender", font=("Arial", 10), width = 13, borderwidth=2, relief="raised", bg="#EEEEEE", cursor="hand2", command=venta2)
vender2.place(x=135, y=420)
cambiar2 = Button(window, text="Cambiar", font=("Arial", 10), width = 13, borderwidth=2, relief="raised", bg="#EEEEEE", cursor="hand2", command=cambiar3)
cambiar2.place(x=260, y=420)
    #Pan
abastecer3 = Button(window, text="Abastecer", font=("Arial", 10), width = 13, borderwidth=2, relief="raised", bg="#EEEEEE", cursor="hand2", command=abastecer3)
abastecer3.place(x=400, y=420)
vender3 = Button(window, text="Vender", font=("Arial", 10), width = 13, borderwidth=2, relief="raised", bg="#EEEEEE", cursor="hand2", command=venta3)
vender3.place(x=525, y=420)
cambiar3 = Button(window, text="Cambiar", font=("Arial", 10), width = 13, borderwidth=2, relief="raised", bg="#EEEEEE", cursor="hand2", command=cambiar4)
cambiar3.place(x=650, y=420)

#Opciones
opciones = Label(window, text="Opciones", font="Arial").place(x=0, y=460)
mas_vendido = Button(window, text="Producto Mas Vendido", font=("Arial", 10), width = 19, borderwidth=2, relief="raised", bg="#EEEEEE", cursor="hand2", command=mas_vendido)
mas_vendido.place(x=50, y=490)
menos_vendido = Button(window, text="Producto Menos Vendido", font=("Arial", 10), width = 19, borderwidth=2, relief="raised", bg="#EEEEEE", cursor="hand2", command=menos_vendido)
menos_vendido.place(x=220, y=490)
ventas = Button(window, text="Promedio Ventas", font=("Arial", 10), width = 19, borderwidth=2, relief="raised", bg="#EEEEEE", cursor="hand2", command=promedio)
ventas.place(x=390, y=490)
caja = Button(window, text="Dinero En Caja", font=("Arial", 10), width = 19, borderwidth=2, relief="raised", bg="#EEEEEE", cursor="hand2", command=caja)
caja.place(x=560, y=490)

window.mainloop()
