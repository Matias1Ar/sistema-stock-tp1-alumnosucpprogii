from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import abm

window=Tk()
window.title('Tienda')
window.geometry('900x600')
window.resizable(0,0)

#Registro de ventas
listaVentas = list()

abm.restablecerValoresVendidos() # para que cada vez que inicie el programa las cantidades vendidas vuelvan a 0

def confirmarCambios(listaRes,producto):
    def modificarProducto():
        try:
            nombre = et_nombre.get()
            tipo = cb_tipo.current()
            cantidadB = int(et_cantidadB.get())
            valorU = float(et_valorU.get())
            cantidadM = int(et_cantidadM.get())
            abm.cambiarProducto(producto["nombre"],nombre,tipo,cantidadB,valorU,cantidadM)
            cargarProductos(listaRes,producto,sinImagen)
        except:
            messagebox.showinfo("mensaje","No se pudo modificar el producto, verifique los campos.")
        window2.destroy()
    window2=Tk()
    window2.title('Cambiar Producto')
    Label(window2, text="Nombre del nuevo producto:", font=("Arial black", 9)).grid(row=0,column=0)
    Label(window2, text="Tipo:", font=("Arial black", 9)).grid(row=1,column=0)
    Label(window2, text="Cantidad bodega:", font=("Arial black", 9)).grid(row=2,column=0)
    Label(window2, text="Valor unitario:", font=("Arial black", 9)).grid(row=3,column=0)
    Label(window2, text="Cantidad minima:", font=("Arial black", 9)).grid(row=4,column=0)
    et_nombre = Entry(window2)
    et_nombre.grid(row=0,column=1)
    cb_tipo = ttk.Combobox(window2,width="17")
    cb_tipo['values'] = ("Papeleria","Supermercado","Drogueria")
    cb_tipo.set("Papeleria")
    cb_tipo.grid(row=1,column=1)
    et_cantidadB = Entry(window2)
    et_cantidadB.grid(row=2,column=1)
    et_valorU = Entry(window2)
    et_valorU.grid(row=3,column=1)
    et_cantidadM = Entry(window2)
    et_cantidadM.grid(row=4,column=1)
    bt = Button(window2,text="Confirmar",command=modificarProducto,width="17")
    bt.grid(row=5,column=1)
    window2.resizable(0,0)
    window2.mainloop()

def abastecerProductos(listaRes,producto,imagen):
    def aceptar():
        try:
            cant = int(et_cant.get())
            abm.comprarProducto(producto["nombre"],cant)
            cargarProductos(listaRes,producto,imagen)
            messagebox.showinfo("Mensaje","Se agrego "+str(cant)+" productos.")
        except:
            messagebox.showinfo("Mensaje","La cantidad en bodega debe ser menor o igual que la cantidad minima.")
        window2.destroy()
    window2=Tk()
    window2.title('Abastecer Producto')
    Label(window2, text="Cantidad de productos a abastecer:", font=("Arial black", 9)).grid(row=0,column=0)
    et_cant = Entry(window2)
    et_cant.grid(row=0,column=1)
    Button(window2,text="ACEPTAR",width="17",command=aceptar).grid(row=1,column=1)
    window2.resizable(0,0)
    window2.mainloop()

def venderProducto(listaRes,producto,imagen):
    def aceptar():
        try:
            cant = int(et_cant.get())
            abm.venderProducto(producto["nombre"],cant)
            cargarProductos(listaRes,producto,imagen)
            listaVentas.append(abm.precioFinal(producto,cant))
            messagebox.showinfo("Mensaje","Se vendio con exito "+str(cant)+" productos.")
            # print(listaVentas) ACTIVARLO SI QUIERE VER, COMO SE VAN AGREGANDO LAS VENTAS
        except:
            messagebox.showinfo("Mensaje","No se pudo realizar la venta solicitada.")
        window2.destroy()
    window2=Tk()
    window2.title('Vender Producto')
    Label(window2, text="Cantidad de productos a vender:", font=("Arial black", 9)).grid(row=0,column=0)
    et_cant = Entry(window2)
    et_cant.grid(row=0,column=1)
    Button(window2,text="ACEPTAR",width="17",command=aceptar).grid(row=1,column=1)
    window2.resizable(0,0)
    window2.mainloop()

def botonAbastecer():
    abastecerProductos(listaResultados,producto1,imagen)
def botonAbastecer2():
    abastecerProductos(listaResultados2,producto2,imagen2)
def botonAbastecer3():
    abastecerProductos(listaResultados3,producto3,imagen3)
def botonAbastecer4():
    abastecerProductos(listaResultados4,producto4,imagen4)

def botonVender():
    venderProducto(listaResultados,producto1,imagen)
def botonVender2():
    venderProducto(listaResultados2,producto2,imagen2)
def botonVender3():
    venderProducto(listaResultados3,producto3,imagen3)
def botonVender4():
    venderProducto(listaResultados4,producto4,imagen4)

def botonCambiar():
    confirmarCambios(listaResultados,producto1)
def botonCambiar2():
    confirmarCambios(listaResultados2,producto2)
def botonCambiar3():
    confirmarCambios(listaResultados3,producto3)
def botonCambiar4():
    confirmarCambios(listaResultados4,producto4)

def cargarProductos(listaResultados,producto,imagen):
    tipo=""
    if producto["tipo"] == 0:
        tipo="Papeleria"
    elif producto["tipo"] == 1:
        tipo="Supermercado"
    elif producto["tipo"] == 2:
        tipo="Drogueria"
    listaResultados[0].config(image=imagen)
    listaResultados[1].config(text=producto["nombre"])
    listaResultados[2].config(text=tipo)
    listaResultados[3].config(text=producto["cantidad_bodega"])
    listaResultados[4].config(text=producto["valor_unitario"])
    listaResultados[5].config(text=producto["cantidad_vendida"])
    listaResultados[6].config(text=producto["cantidad_minima"])

def crearBotones(frame):
    listaBotones = list()
    bt_abatecer = Button(frame,width="18",height="2",text="Abastecer")
    bt_abatecer.place(x=5,y=195)
    bt_vender = Button(frame,width="18",height="2",text="Vender")
    bt_vender.place(x=150,y=195)
    bt_cambiar = Button(frame,width="18",height="2",text="Cambiar")
    bt_cambiar.place(x=295,y=195)
    listaBotones.append(bt_abatecer)
    listaBotones.append(bt_vender)
    listaBotones.append(bt_cambiar)
    return listaBotones

def crearLabels(frame):
    listaLabels = list()
    y=40
    Label(frame, text="Tipo:", font=("Arial black", 9)).place(x=165,y=40)
    Label(frame, text="Cantidad bodega:", font=("Arial black", 9)).place(x=165,y=70)
    Label(frame, text="Valor unitario:", font=("Arial black", 9)).place(x=165,y=100)
    Label(frame, text="Cantidad vendidas:", font=("Arial black", 9)).place(x=165,y=130)
    Label(frame, text="Cantidad minima:", font=("Arial black", 9)).place(x=165,y=160)
    for i in range(5):
        if i==0:
            lbl_img = Label(frame)
            lbl_img.place(x=10,y=30)
            listaLabels.append(lbl_img)
            lbl_titulo = Label(frame, text="", font=("Arial black", 10))
            lbl_titulo.place(x=0,y=0)
            listaLabels.append(lbl_titulo)
        lbl = Label(frame, text="", font=("Arial", 9))
        lbl.place(x=340,y=y)
        listaLabels.append(lbl)
        y += 30
    return listaLabels

def dineroCaja():
    caja= 0.0
    for una_venta in listaVentas:
        caja += una_venta
    caja = float(caja) #Para disminuir decimales
    messagebox.showinfo("CAJA","Dinero actual en caja: "+str(caja))

def productoMasVendido():
    producto = abm.productoMasVendido()
    messagebox.showinfo("Mensaje","Producto mas vendido: "+str(producto))

def productoMenosVendido():
    producto = abm.productoMenosVendido()
    messagebox.showinfo("Mensaje","Producto menos vendido: "+str(producto))

def promedioVentas():
    try:
        caja=0.0
        for una_venta in listaVentas:
            caja += una_venta
        totalVendidas = abm.totalVendidos()
        prom = caja/totalVendidas
        prom = float(prom)
        messagebox.showinfo("Mensaje","Promedio de ventas: "+str(prom))
    except:
        messagebox.showinfo("Mensaje","Todavia no es posible sacar el promedio")

#Imagenes de productos
sinImagen = PhotoImage(file="imagenes/blanco.gif")
imagen = PhotoImage(file="imagenes/lapiz.gif")
imagen2 = PhotoImage(file="imagenes/aspirina.gif")
imagen3 = PhotoImage(file="imagenes/borrador.gif")
imagen4 = PhotoImage(file="imagenes/pan.gif")

#Frame producto1
frame1 = Frame(window,width="450", height="250",relief="groove",bd=5)
frame1.grid(row=0,column=0)

listaResultados = crearLabels(frame1)

#CargarProductos1
producto1 = abm.listaProductos[0]
cargarProductos(listaResultados,producto1,imagen)

#Botones 1
listaBotones = crearBotones(frame1)
listaBotones[0].config(command=botonAbastecer)
listaBotones[1].config(command=botonVender)
listaBotones[2].config(command=botonCambiar)

#------------------------------------------------------------------------

#Frame producto2
frame2 = Frame(window,width="450", height="250",relief="groove",bd=5)
frame2.grid(row=0,column=1)

listaResultados2 = crearLabels(frame2)


#CargarProductos2
producto2 = abm.listaProductos[1]
cargarProductos(listaResultados2,producto2,imagen2)

#Botones 2
listaBotones2 = crearBotones(frame2)
listaBotones2[0].config(command=botonAbastecer2)
listaBotones2[1].config(command=botonVender2)
listaBotones2[2].config(command=botonCambiar2)

#------------------------------------------------------------------------

#Frame producto3
frame3 = Frame(window,width="450", height="250",relief="groove",bd=5)
frame3.grid(row=1,column=0)

listaResultados3 = crearLabels(frame3)


#CargarProductos3
producto3 = abm.listaProductos[2]
cargarProductos(listaResultados3,producto3,imagen3)

#Botones 2
listaBotones3 = crearBotones(frame3)
listaBotones3[0].config(command=botonAbastecer3)
listaBotones3[1].config(command=botonVender3)
listaBotones3[2].config(command=botonCambiar3)

#------------------------------------------------------------------------

#Frame producto4
frame4 = Frame(window,width="450", height="250",relief="groove",bd=5)
frame4.grid(row=1,column=1)

listaResultados4 = crearLabels(frame4)

#CargarProductos4
producto4 = abm.listaProductos[3]
cargarProductos(listaResultados4,producto4,imagen4)

#Botones 2
listaBotones4 = crearBotones(frame4)
listaBotones4[0].config(command=botonAbastecer4)
listaBotones4[1].config(command=botonVender4)
listaBotones4[2].config(command=botonCambiar4)

#------------------------------------------------------------------------

#Frame Opciones
frame5 = Frame(window,width="900", height="125",relief="groove",bd=5)
frame5.place(x=0,y=500)

#Opciones
Label(frame5, text="Opciones", font=("Arial black", 10)).place(x=0,y=0)
Button(frame5,width="35",height="1",text="Producto mas vendido",command=productoMasVendido).place(x=2,y=25)
Button(frame5,width="35",height="1",text="Dinero en caja",command=dineroCaja).place(x=2,y=55)
Button(frame5,width="35",height="1",text="Producto menos vendido",command=productoMenosVendido).place(x=280,y=25)
Button(frame5,width="35",height="1",text="Promedio de ventas",command=promedioVentas).place(x=280,y=55)




window.mainloop()
