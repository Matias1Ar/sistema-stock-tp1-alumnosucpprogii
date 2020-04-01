from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

window = Tk()
window.wm_title("Programacion II - Lic. en Sistemas")
window.config(background = "#EEEEEE")
window.geometry("850x450+10+20")
window.resizable(0,0)
style = ttk.Style()
style.configure('TButton', foreground='Black', borderwidth=110,relief='groove', padding=10)

########FUNCIONES 1 RECUADRO##############
def registrar():
    entradaTipo.configure(state=DISABLED)
    entradaStock.configure(state=DISABLED)
    entradaValorUnitario.configure(state=DISABLED)
    entradaCantidadVendida.configure(state=DISABLED)
    entradaCantidadMinima.configure(state=DISABLED)

def venderProducto():
    entradaStock.configure(state=NORMAL)
    entradaCantidadVendida.configure(state=NORMAL)
    stock=int(entradaStock.get())
    nvoStock=stock-1
    entradaStock.delete(0,END)
    entradaStock.insert(0,nvoStock)
    cantVendida=int(entradaCantidadVendida.get())
    nvaCantVendida=cantVendida+1
    entradaCantidadVendida.delete(0,END)
    entradaCantidadVendida.insert(0,nvaCantVendida)
    entradaStock.configure(state=DISABLED)
    entradaCantidadVendida.configure(state=DISABLED)

def abastecer():
    entradaStock.configure(state=NORMAL)
    stock=int(entradaStock.get())
    nvoStock=stock+1
    entradaStock.delete(0,END)
    entradaStock.insert(0,nvoStock)
    entradaStock.configure(state=DISABLED)

def cambiar():
    entradaTipo.configure(state=NORMAL)
    entradaStock.configure(state=NORMAL)
    entradaValorUnitario.configure(state=NORMAL)
    entradaCantidadVendida.configure(state=NORMAL)
    entradaCantidadMinima.configure(state=NORMAL)
    entradaTipo.delete(0,END)
    entradaStock.delete(0,END)
    entradaValorUnitario.delete(0,END)
    entradaCantidadVendida.delete(0,END)
    entradaCantidadMinima.delete(0,END)

#######FUNCIONES 2 RECUADRO####################
def registrar2():
    entradaTipo2.configure(state=DISABLED)
    entradaStock2.configure(state=DISABLED)
    entradaValorUnitario2.configure(state=DISABLED)
    entradaCantidadVendida2.configure(state=DISABLED)
    entradaCantidadMinima2.configure(state=DISABLED)

def venderProducto2():
    entradaStock2.configure(state=NORMAL)
    entradaCantidadVendida2.configure(state=NORMAL)
    stock=int(entradaStock2.get())
    nvoStock=stock-1
    entradaStock2.delete(0,END)
    entradaStock2.insert(0,nvoStock)
    cantVendida=int(entradaCantidadVendida2.get())
    nvaCantVendida=cantVendida+1
    entradaCantidadVendida2.delete(0,END)
    entradaCantidadVendida2.insert(0,nvaCantVendida)
    entradaStock2.configure(state=DISABLED)
    entradaCantidadVendida2.configure(state=DISABLED)

def abastecer2():
    entradaStock2.configure(state=NORMAL)
    stock=int(entradaStock2.get())
    nvoStock=stock+1
    entradaStock2.delete(0,END)
    entradaStock2.insert(0,nvoStock)
    entradaStock2.configure(state=DISABLED)

def cambiar2():
    entradaTipo2.configure(state=NORMAL)
    entradaStock2.configure(state=NORMAL)
    entradaValorUnitario2.configure(state=NORMAL)
    entradaCantidadVendida2.configure(state=NORMAL)
    entradaCantidadMinima2.configure(state=NORMAL)
    entradaTipo2.delete(0,END)
    entradaStock2.delete(0,END)
    entradaValorUnitario2.delete(0,END)
    entradaCantidadVendida2.delete(0,END)
    entradaCantidadMinima2.delete(0,END)
#######################FUNCIONES 3 RECUADRO###################
def registrar3():
    entradaTipo3.configure(state=DISABLED)
    entradaStock3.configure(state=DISABLED)
    entradaValorUnitario3.configure(state=DISABLED)
    entradaCantidadVendida3.configure(state=DISABLED)
    entradaCantidadMinima3.configure(state=DISABLED)

def venderProducto3():
    entradaStock3.configure(state=NORMAL)
    entradaCantidadVendida3.configure(state=NORMAL)
    stock=int(entradaStock3.get())
    nvoStock=stock-1
    entradaStock3.delete(0,END)
    entradaStock3.insert(0,nvoStock)
    cantVendida=int(entradaCantidadVendida3.get())
    nvaCantVendida=cantVendida+1
    entradaCantidadVendida3.delete(0,END)
    entradaCantidadVendida3.insert(0,nvaCantVendida)
    entradaStock3.configure(state=DISABLED)
    entradaCantidadVendida3.configure(state=DISABLED)

def abastecer3():
    entradaStock3.configure(state=NORMAL)
    stock=int(entradaStock3.get())
    nvoStock=stock+1
    entradaStock3.delete(0,END)
    entradaStock3.insert(0,nvoStock)
    entradaStock3.configure(state=DISABLED)

def cambiar3():
    entradaTipo3.configure(state=NORMAL)
    entradaStock3.configure(state=NORMAL)
    entradaValorUnitario3.configure(state=NORMAL)
    entradaCantidadVendida3.configure(state=NORMAL)
    entradaCantidadMinima3.configure(state=NORMAL)
    entradaTipo3.delete(0,END)
    entradaStock3.delete(0,END)
    entradaValorUnitario3.delete(0,END)
    entradaCantidadVendida3.delete(0,END)
    entradaCantidadMinima3.delete(0,END)

##############FUNCIONES 4 RECUADRO##################
def registrar4():
    entradaTipo4.configure(state=DISABLED)
    entradaStock4.configure(state=DISABLED)
    entradaValorUnitario4.configure(state=DISABLED)
    entradaCantidadVendida4.configure(state=DISABLED)
    entradaCantidadMinima4.configure(state=DISABLED)

def venderProducto4():
    entradaStock4.configure(state=NORMAL)
    entradaCantidadVendida4.configure(state=NORMAL)
    stock=int(entradaStock4.get())
    nvoStock=stock-1
    entradaStock4.delete(0,END)
    entradaStock4.insert(0,nvoStock)
    cantVendida=int(entradaCantidadVendida4.get())
    nvaCantVendida=cantVendida+1
    entradaCantidadVendida4.delete(0,END)
    entradaCantidadVendida4.insert(0,nvaCantVendida)
    entradaStock4.configure(state=DISABLED)
    entradaCantidadVendida4.configure(state=DISABLED)

def abastecer4():
    entradaStock4.configure(state=NORMAL)
    stock=int(entradaStock4.get())
    nvoStock=stock+1
    entradaStock4.delete(0,END)
    entradaStock4.insert(0,nvoStock)
    entradaStock4.configure(state=DISABLED)

def cambiar4():
    entradaTipo4.configure(state=NORMAL)
    entradaStock4.configure(state=NORMAL)
    entradaValorUnitario4.configure(state=NORMAL)
    entradaCantidadVendida4.configure(state=NORMAL)
    entradaCantidadMinima4.configure(state=NORMAL)
    entradaTipo4.delete(0,END)
    entradaStock4.delete(0,END)
    entradaValorUnitario4.delete(0,END)
    entradaCantidadVendida4.delete(0,END)
    entradaCantidadMinima4.delete(0,END)

##############FUNCIONES 5 RECUADRO##################################
def productoMasVendido():
    productos=dict()
    productos["Lapiz"]=entradaCantidadVendida.get()
    productos["Aspirina"]=entradaCantidadVendida2.get()
    productos["Borrador"]=entradaCantidadVendida3.get()
    productos["Pan"]=entradaCantidadVendida4.get()

    pmv.configure(state=NORMAL)
    masVendido=max(zip(productos.values(),productos.keys()))
    pmv.delete(0,END)
    pmv.insert(0,masVendido)
    pmv.configure(state=DISABLED)
    productos.clear()

def productoMenosVendido():
    productos=dict()
    productos["Lapiz"]=entradaCantidadVendida.get()
    productos["Aspirina"]=entradaCantidadVendida2.get()
    productos["Borrador"]=entradaCantidadVendida3.get()
    productos["Pan"]=entradaCantidadVendida4.get()

    pmenosv.configure(state=NORMAL)
    menosVendido=min(zip(productos.values(),productos.keys()))
    pmenosv.delete(0,END)
    pmenosv.insert(0,menosVendido)
    pmenosv.configure(state=DISABLED)
    productos.clear()

def dineroCaja():
    precio1=float(float(entradaValorUnitario.get())*1.16)
    precio2=float(float(entradaValorUnitario2.get())*1.12)
    precio3=float(float(entradaValorUnitario3.get())*1.16)
    precio4=float(float(entradaValorUnitario4.get())*1.04)

    ventas1=float(precio1*float(entradaCantidadVendida.get()))
    ventas2=float(precio2*float(entradaCantidadVendida2.get()))
    ventas3=float(precio3*float(entradaCantidadVendida3.get()))
    ventas4=float(precio4*float(entradaCantidadVendida4.get()))

    totalVentas=float(ventas1+ventas2+ventas3+ventas4)
    caja.configure(state=NORMAL)
    caja.delete(0,END)
    caja.insert(0,totalVentas)
    caja.configure(state=DISABLED)

def promedioVentas():
    precio1=float(float(entradaValorUnitario.get())*1.16)
    precio2=float(float(entradaValorUnitario2.get())*1.12)
    precio3=float(float(entradaValorUnitario3.get())*1.16)
    precio4=float(float(entradaValorUnitario4.get())*1.04)

    ventas1=float(precio1*float(entradaCantidadVendida.get()))
    ventas2=float(precio2*float(entradaCantidadVendida2.get()))
    ventas3=float(precio3*float(entradaCantidadVendida3.get()))
    ventas4=float(precio4*float(entradaCantidadVendida4.get()))

    totalVentas=float(ventas1+ventas2+ventas3+ventas4)
    cantidadesVendidasTotal=float(float(entradaCantidadVendida.get())+float(entradaCantidadVendida2.get())
                                  +float(entradaCantidadVendida3.get())+float(entradaCantidadVendida4.get()))
    prom=float(totalVentas/cantidadesVendidasTotal)

    promVentas.configure(state=NORMAL)
    promVentas.delete(0,END)
    promVentas.insert(0,prom)
    promVentas.configure(state=DISABLED)
    #totalventas/cantvendidas sumatoria por precio



#############################################################3333
def start():
    titulo=Label(window,width=30, text="Informacion de Productos", font=("helvetica",14))
    titulo.place(x=0,y=8)

    recuadro01 = Canvas(window, width=420,
                height=180,
                borderwidth=2,
                background='#EEEEEE',
                relief='groove')
    recuadro01.place(x=0, y=40)

    lbl01 = Label(window,width=10, text="Lapiz", font=("Helvetica",12)) #Nombre Producto
    lbl01.place(x=4, y=44)
    #Labels del producto
    lblTipo = Label(window,width=10, text="Tipo:", font=("Helvetica",11))
    lblTipo.place(x=12, y=70)
    lblStock = Label(window, width=20, text="Cantidad Bodega:", font=("Helvetica",11))
    lblStock.place(x=12,y=90)
    lblValorUnitario = Label(window, width=20, text="Valor Unitario:", font=("Helvetica",11))
    lblValorUnitario.place(x=12,y=110)
    lblCantidadVendida = Label(window, width=20, text="Cantidad Vendida:", font=("Helvetica",11))
    lblCantidadVendida.place(x=12,y=130)
    lblCantidadMinima = Label(window, width=20, text="Cantidad Minima:", font=("Helvetica",11))
    lblCantidadMinima.place(x=12,y=150)
    #Entry productos
    global entradaTipo
    entradaTipo = Entry(window, width=20)
    entradaTipo.place(x=200, y=70)
    global entradaStock
    entradaStock = Entry(window, width=20)
    entradaStock.place(x=200, y=90)
    global entradaValorUnitario
    entradaValorUnitario = Entry(window, width=20)
    entradaValorUnitario.place(x=200, y=110)
    global entradaCantidadVendida
    entradaCantidadVendida = Entry(window, width=20)
    entradaCantidadVendida.place(x=200, y=130)
    global entradaCantidadMinima
    entradaCantidadMinima = Entry(window, width=20)
    entradaCantidadMinima.place(x=200, y=150)
    #Botones recuadro01
    buttonAbastecer = Button(window,width=20, text="Abastecer",command=abastecer)
    buttonAbastecer.place(x=4, y=172,height=29)

    buttonVender = Button(window, text="Vender",width=20, command=venderProducto)
    buttonVender.place(x=140, y=172,height=29)

    buttonCambiar = Button(window, text="Cambiar",width=20, command=cambiar)
    buttonCambiar.place(x=280, y=172,height=29)

    buttonRegistrar= Button(window, text="Registrar", width=8, command=registrar)
    buttonRegistrar.place(x=340,y=110, height=29)



#######################################################
    recuadro02 = Canvas(window, width=420,
                height=180,
                borderwidth=2,
                background='#EEEEEE',
                relief='groove')
    recuadro02.place(x=420, y=40)

    lbl02 = Label(window,width=10, text="Aspirina", font=("Helvetica",12)) #Nombre Producto
    lbl02.place(x=424, y=44)

    #Labels del producto
    lblTipo2 = Label(window,width=10, text="Tipo:", font=("Helvetica",11))
    lblTipo2.place(x=432, y=70)
    lblStock2 = Label(window, width=20, text="Cantidad Bodega:", font=("Helvetica",11))
    lblStock2.place(x=432,y=90)
    lblValorUnitario2 = Label(window, width=20, text="Valor Unitario:", font=("Helvetica",11))
    lblValorUnitario2.place(x=432,y=110)
    lblCantidadVendida2 = Label(window, width=20, text="Cantidad Vendida:", font=("Helvetica",11))
    lblCantidadVendida2.place(x=432,y=130)
    lblCantidadMinima2 = Label(window, width=20, text="Cantidad Minima:", font=("Helvetica",11))
    lblCantidadMinima2.place(x=432,y=150)
    #Entry productos
    global entradaTipo2
    entradaTipo2 = Entry(window, width=20)
    entradaTipo2.place(x=620, y=70)
    global entradaStock2
    entradaStock2 = Entry(window, width=20)
    entradaStock2.place(x=620, y=90)
    global entradaValorUnitario2
    entradaValorUnitario2 = Entry(window, width=20)
    entradaValorUnitario2.place(x=620, y=110)
    global entradaCantidadVendida2
    entradaCantidadVendida2 = Entry(window, width=20)
    entradaCantidadVendida2.place(x=620, y=130)
    global entradaCantidadMinima2
    entradaCantidadMinima2 = Entry(window, width=20)
    entradaCantidadMinima2.place(x=620, y=150)
    #Botones recuadro02
    buttonAbastecer2 = Button(window,width=20, text="Abastecer", command=abastecer2)
    buttonAbastecer2.place(x=424, y=172,height=29)

    buttonVender2 = Button(window, text="Vender",width=20,command=venderProducto2)
    buttonVender2.place(x=564, y=172,height=29)

    buttonCambiar2 = Button(window, text="Cambiar",width=20,command=cambiar2)
    buttonCambiar2.place(x=695, y=172,height=29)

    buttonRegistrar2= Button(window, text="Registrar", width=8, command=registrar2)
    buttonRegistrar2.place(x=760,y=110, height=29)

##########################################################
    recuadro03= Canvas(window, width=420,
                height=158,
                borderwidth=2,
                background='#EEEEEE',
                relief='groove')
    recuadro03.place(x=0, y=200)


    lbl03 = Label(window,width=10, text="Borrador", font=("Helvetica",12)) #Nombre del producto
    lbl03.place(x=4, y=204)

    #Labels del producto
    lblTipo3 = Label(window,width=10, text="Tipo:", font=("Helvetica",11))
    lblTipo3.place(x=12, y=230)
    lblStock3 = Label(window, width=20, text="Cantidad Bodega:", font=("Helvetica",11))
    lblStock3.place(x=12,y=250)
    lblValorUnitario3 = Label(window, width=20, text="Valor Unitario:", font=("Helvetica",11))
    lblValorUnitario3.place(x=12,y=270)
    lblCantidadVendida3 = Label(window, width=20, text="Cantidad Vendida:", font=("Helvetica",11))
    lblCantidadVendida3.place(x=12,y=290)
    lblCantidadMinima3 = Label(window, width=20, text="Cantidad Minima:", font=("Helvetica",11))
    lblCantidadMinima3.place(x=12,y=310)
    #Entry productos
    global entradaTipo3
    entradaTipo3 = Entry(window, width=20)
    entradaTipo3.place(x=200, y=230)
    global entradaStock3
    entradaStock3 = Entry(window, width=20)
    entradaStock3.place(x=200, y=250)
    global entradaValorUnitario3
    entradaValorUnitario3 = Entry(window, width=20)
    entradaValorUnitario3.place(x=200, y=270)
    global entradaCantidadVendida3
    entradaCantidadVendida3 = Entry(window, width=20)
    entradaCantidadVendida3.place(x=200, y=290)
    global entradaCantidadMinima3
    entradaCantidadMinima3 = Entry(window, width=20)
    entradaCantidadMinima3.place(x=200, y=310)
    #Botones recuadro03
    buttonAbastecer3 = Button(window,width=20, text="Abastecer",command=abastecer3)
    buttonAbastecer3.place(x=4, y=332,height=29)

    buttonVender3 = Button(window, text="Vender",width=20,command=venderProducto3)
    buttonVender3.place(x=140, y=332,height=29)

    buttonCambiar3 = Button(window, text="Cambiar",width=20,command=cambiar3)
    buttonCambiar3.place(x=280, y=332,height=29)

    buttonRegistrar3= Button(window, text="Registrar", width=8, command=registrar3)
    buttonRegistrar3.place(x=340,y=270, height=29)


#########################################################
    recuadro04 = Canvas(window, width=420,
                height=158,
                borderwidth=2,
                background='#EEEEEE',
                relief='groove')
    recuadro04.place(x=420, y=200)

    lbl04 = Label(window,width=10, text="Pan", font=("Helvetica",12))#Nombre Producto
    lbl04.place(x=424, y=204)

    #Labels del producto
    lblTipo4 = Label(window,width=10, text="Tipo:", font=("Helvetica",11))
    lblTipo4.place(x=432, y=230)
    lblStock4 = Label(window, width=20, text="Cantidad Bodega:", font=("Helvetica",11))
    lblStock4.place(x=432,y=250)
    lblValorUnitario4 = Label(window, width=20, text="Valor Unitario:", font=("Helvetica",11))
    lblValorUnitario4.place(x=432,y=270)
    lblCantidadVendida4 = Label(window, width=20, text="Cantidad Vendida:", font=("Helvetica",11))
    lblCantidadVendida4.place(x=432,y=290)
    lblCantidadMinima4 = Label(window, width=20, text="Cantidad Minima:", font=("Helvetica",11))
    lblCantidadMinima4.place(x=432,y=310)
    #Entry productos
    global entradaTipo4
    entradaTipo4 = Entry(window, width=20)
    entradaTipo4.place(x=620, y=230)
    global entradaStock4
    entradaStock4 = Entry(window, width=20)
    entradaStock4.place(x=620, y=250)
    global entradaValorUnitario4
    entradaValorUnitario4 = Entry(window, width=20)
    entradaValorUnitario4.place(x=620, y=270)
    global entradaCantidadVendida4
    entradaCantidadVendida4 = Entry(window, width=20)
    entradaCantidadVendida4.place(x=620, y=290)
    global entradaCantidadMinima4
    entradaCantidadMinima4 = Entry(window, width=20)
    entradaCantidadMinima4.place(x=620, y=310)
    #Botones recuadro04
    buttonAbastecer4 = Button(window,width=20, text="Abastecer",command=abastecer4)
    buttonAbastecer4.place(x=424, y=332,height=29)

    buttonVender4 = Button(window, text="Vender",width=20,command=venderProducto4)
    buttonVender4.place(x=564, y=332,height=29)

    buttonCambiar4 = Button(window, text="Cambiar",width=20,command=cambiar4)
    buttonCambiar4.place(x=695, y=332,height=29)

    buttonRegistrar4= Button(window, text="Registrar", width=8, command=registrar4)
    buttonRegistrar4.place(x=760,y=270, height=29)
#########################################################
    recuadro05 = Canvas(window, width=840,
                height=80,
                borderwidth=2,
                background='#EEEEEE',
                relief='groove')
    recuadro05.place(x=0, y=360)

    lbl05 = Label(window,width=10, text="Opciones:", font=("Helvetica",12))
    lbl05.place(x=4, y=364)

    #Botones recuadro05
    buttonProductoMasVendido = Button(window,width=32, text="Producto mas vendido", command=productoMasVendido)
    buttonProductoMasVendido.place(x=4, y=384,height=29)
    global pmv
    pmv=Entry(window,width=35, state=DISABLED)
    pmv.place(x=4,y=414, height=29)

    buttonProductoMenosVendido = Button(window, text="Producto menos vendido",width=32, command=productoMenosVendido)
    buttonProductoMenosVendido.place(x=220, y=384,height=29)
    global pmenosv
    pmenosv=Entry(window,width=34, state=DISABLED)
    pmenosv.place(x=221,y=414, height=29)

    buttonPromedioVentas = Button(window, text="Promedio de ventas",width=32,command=promedioVentas)
    buttonPromedioVentas .place(x=430, y=384,height=29)
    global promVentas
    promVentas=Entry(window,width=31, state=DISABLED)
    promVentas.place(x=431,y=414, height=29)

    buttonDineroCaja = Button(window, text="Dinero en caja",width=32, command=dineroCaja)
    buttonDineroCaja.place(x=622, y=384,height=29)
    global caja
    caja=Entry(window,width=36, state=DISABLED)
    caja.place(x=622,y=414, height=29)




start()
window.mainloop()
