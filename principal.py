from tkinter import *

ventana = Tk()
ventana.geometry("800x700")
ventana.title("Tienda")

lblTitulo = Label(ventana, text="Productos", font=("Arial Bold", 16))
lblTitulo.place(x=320, y=10)

dinero = 0
total = 0
totalVendidos = 0
######################################LAPIZ########################################
lblLapiz = DoubleVar()
lblLapiz.set("LAPIZ")
txtLapiz = Entry(ventana, text=lblLapiz, state='disabled')
txtLapiz.place(x=5, y=30)

lblTipoL = Label(ventana, text="Tipo", font=("Arial Bold", 12))
lblTipoL.place(x=5, y=60)

lblCantidadBL = Label(ventana, text="Cantidad en bodega", font=("Arial Bold", 12))
lblCantidadBL.place(x=5, y=90)

lblPrecioUL = Label(ventana, text="Precio Unitario", font=("Arial Bold", 12))
lblPrecioUL.place(x=5, y=120)

lblCantidadVL = Label(ventana, text="Cantidad de vendidos", font=("Arial Bold", 12))
lblCantidadVL.place(x=5, y=150)

lblCantidadML = Label(ventana, text="Cantidad minima", font=("Arial Bold", 12))
lblCantidadML.place(x=5, y=180)


tipoL = DoubleVar()
tipoL.set("Papelería")
txtTipoL = Entry(ventana, text=tipoL, state='disabled')
txtTipoL.place(x=180, y=65)

CantidadBL = DoubleVar()
CantidadBL.set(18)
txtCantidadBL = Entry(ventana, text=CantidadBL, state='disabled')
txtCantidadBL.place(x=180, y=95)

valorL = DoubleVar()
valorL.set(30)
txtValorL = Entry(ventana, text=valorL, state='disabled')
txtValorL.place(x=180, y=125)

CantidadVL = DoubleVar()
CantidadVL.set(0)
txtCantidadVL = Entry(ventana, text=CantidadVL, state='disabled')
txtCantidadVL.place(x=180, y=155)

CantidadML = DoubleVar()
CantidadML.set(5)
txtCantidadML = Entry(ventana, text=CantidadML, state='disabled')
txtCantidadML.place(x=180, y=185)

lapizMinimo = int(txtCantidadML.get())
lapizBodega = int(txtCantidadBL.get())
lapizVenta = int(txtCantidadVL.get())
precioLapiz = float(txtValorL.get())
if txtTipoL.get() == "Papelería":
    precioLapiz = precioLapiz+(precioLapiz*0.16)
elif txtTipoA.get() == "Droguería":
    precioAspirina = precioAspirina+(precioAspirina*0.12)
elif txtTipoP.get() == "Supermercado":
    porcentaje = (precioPan/100)*4
    precioPan += porcentaje
######BOTONES DE LAPIZ######
def AbastecerL():
    global lapizBodega
    agregar = lapizBodega + 1
    CantidadBL.set(agregar)
    lapizBodega += 1
def VenderL():
    txtVender = Entry(ventana)
    txtVender.place(x=80, y=230)
    def CantidadVenta():
        global lapizVenta
        global lapizBodega
        global lapizMinimo
        obVenta = int(txtVender.get())
        bodega = lapizBodega - obVenta
        if bodega >= lapizMinimo:
            quitar = lapizBodega - obVenta
            CantidadBL.set(quitar)
            agregar = lapizVenta + obVenta
            CantidadVL.set(agregar)
            lapizVenta += obVenta
            lapizBodega -= obVenta
        else:
            lblError = Label(ventana, text="Sobrepasa la cantidad mínima en bodega", font=("Arial Bold", 12))
            lblError.place(x=5, y=180)
            def btn():
                lblError.destroy()
                btnOK.destroy()
            btnOK = Button(ventana, text="OK", command=btn)
            btnOK.place(x=300, y=180)
        txtVender.destroy()
        btnAceptar.destroy()
    btnAceptar = Button(ventana, text="Aceptar", command=CantidadVenta)
    btnAceptar.place(x=150, y=230)

def CambiarL():
    txtLapiz.config(state="normal")
    txtTipoL.config(state="normal")
    txtValorL.config(state="normal")
    txtCantidadBL.config(state="normal")
    txtCantidadVL.config(state="normal")
    txtCantidadML.config(state="normal")

    def Aceptar():
        obTipo = txtTipoL.get()
        obValor = int(txtValorL.get())
        obCantidadB = int(txtCantidadBL.get())
        obCantidadV = int(txtCantidadVL.get())
        obCantidadM = int(txtCantidadML.get())
        tipoL.set(obTipo)
        valorL.set(obValor)
        CantidadBL.set(obCantidadB)
        CantidadVL.set(obCantidadV)
        CantidadML.set(obCantidadM)
        txtLapiz.config(state="disabled")
        txtTipoL.config(state="disabled")
        txtValorL.config(state="disabled")
        txtCantidadBL.config(state="disabled")
        txtCantidadVL.config(state="disabled")
        txtCantidadML.config(state="disabled")

    btnAceptar = Button(ventana, text="Aceptar", command=Aceptar)
    btnAceptar.place(x=200, y=205)

btnAbastecerL = Button(ventana, text="Abastecer", command=AbastecerL)
btnAbastecerL.place(x=5, y=205)
btnVenderL = Button(ventana, text="Vender", command=VenderL)
btnVenderL.place(x=80, y=205)
btnCambiarL = Button(ventana, text="Cambiar", command=CambiarL)
btnCambiarL.place(x=140, y=205)

##################################BORRADOR###############################################
lblBorrador = DoubleVar()
lblBorrador.set("BORRADOR")
txtBorrador = Entry(ventana, text=lblBorrador, state='disabled')
txtBorrador.place(x=5, y=260)

lblTipoB = Label(ventana, text="Tipo", font=("Arial Bold", 12))
lblTipoB.place(x=5, y=290)

lblCantidadBB = Label(ventana, text="Cantidad en bodega", font=("Arial Bold", 12))
lblCantidadBB.place(x=5, y=320)

lblPrecioUB = Label(ventana, text="Precio Unitario", font=("Arial Bold", 12))
lblPrecioUB.place(x=5, y=350)

lblCantidadVB = Label(ventana, text="Cantidad de vendidos", font=("Arial Bold", 12))
lblCantidadVB.place(x=5, y=380)

lblCantidadMB = Label(ventana, text="Cantidad minima", font=("Arial Bold", 12))
lblCantidadMB.place(x=5, y=410)

tipoB = DoubleVar()
tipoB.set("Papelería")
txtTipoB = Entry(ventana, text=tipoB, state='disabled')
txtTipoB.place(x=180, y=295)

CantidadBB = DoubleVar()
CantidadBB.set(20)
txtCantidadBB = Entry(ventana, text=CantidadBB, state='disabled')
txtCantidadBB.place(x=180, y=325)

valorB = DoubleVar()
valorB.set(25)
txtValorB = Entry(ventana, text=valorB, state='disabled')
txtValorB.place(x=180, y=355)

CantidadVB = DoubleVar()
CantidadVB.set(2)
txtCantidadVB = Entry(ventana, text=CantidadVB, state='disabled')
txtCantidadVB.place(x=180, y=385)

CantidadMB = DoubleVar()
CantidadMB.set(5)
txtCantidadMB = Entry(ventana, text=CantidadMB, state='disabled')
txtCantidadMB.place(x=180, y=415)

borradorMinimo = int(txtCantidadMB.get())
borradorBodega = int(txtCantidadBB.get())
borradorVenta = int(txtCantidadVB.get())
precioBorrador = float(txtValorB.get())
if txtTipoL.get() == "Papelería":
    precioBorrador = precioBorrador+(precioBorrador*0.16)
elif txtTipoP.get() == "Supermercado":
    porcentaje = (precioPan/100)*4
    precioPan += porcentaje
######BOTONES BORRADOR#########
def AbastecerB():
    global borradorBodega
    agregar = borradorBodega + 1
    CantidadBB.set(agregar)
    borradorBodega += 1


def VenderB():
    txtVender = Entry(ventana)
    txtVender.place(x=80, y=480)

    def CantidadVenta():
        global borradorVenta
        global borradorBodega
        global borradorMinimo
        obVenta = int(txtVender.get())
        bodega = borradorBodega - obVenta
        if bodega >= borradorMinimo:
            quitar = borradorBodega - obVenta
            CantidadBB.set(quitar)
            agregar = borradorVenta + obVenta
            CantidadVB.set(agregar)
            borradorVenta += obVenta
            borradorBodega -= obVenta
        else:
            lblError = Label(ventana, text="Sobrepasa la cantidad mínima en bodega", font=("Arial Bold", 12))
            lblError.place(x=5, y=410)
            def btn():
                lblError.destroy()
                btnOK.destroy()

            btnOK = Button(ventana, text="OK", command=btn)
            btnOK.place(x=300, y=410)

        txtVender.destroy()
        btnAceptar.destroy()
    btnAceptar = Button(ventana, text="Aceptar", command=CantidadVenta)
    btnAceptar.place(x=150, y=480)

def CambiarB():
    txtBorrador.config(state="normal")
    txtTipoB.config(state="normal")
    txtValorB.config(state="normal")
    txtCantidadBB.config(state="normal")
    txtCantidadVB.config(state="normal")
    txtCantidadMB.config(state="normal")

    def Aceptar():
        obTipo = txtTipoB.get()
        obValor = int(txtValorB.get())
        obCantidadB = int(txtCantidadBB.get())
        obCantidadV = int(txtCantidadVB.get())
        obCantidadM = int(txtCantidadMB.get())
        tipoB.set(obTipo)
        valorB.set(obValor)
        CantidadBB.set(obCantidadB)
        CantidadVB.set(obCantidadV)
        CantidadMB.set(obCantidadM)
        txtBorrador.config(state="disabled")
        txtTipoB.config(state="disabled")
        txtValorB.config(state="disabled")
        txtCantidadBB.config(state="disabled")
        txtCantidadVB.config(state="disabled")
        txtCantidadMB.config(state="disabled")

    btnAceptar = Button(ventana, text="Aceptar", command=Aceptar)
    btnAceptar.place(x=200, y=450)

btnAbastecerB = Button(ventana, text="Abastecer", command=AbastecerB)
btnAbastecerB.place(x=5, y=450)
btnVenderB = Button(ventana, text="Vender", command=VenderB)
btnVenderB.place(x=80, y=450)
btnCambiarB = Button(ventana, text="Cambiar", command=CambiarB)
btnCambiarB.place(x=140, y=450)

############################ASPIRINA###########################################
lblAspirina = DoubleVar()
lblAspirina.set("ASPIRINA")
txtAspirina = Entry(ventana, text=lblAspirina, state='disabled')
txtAspirina.place(x=450, y=30)

lblTipoA = Label(ventana, text="Tipo", font=("Arial Bold", 12))
lblTipoA.place(x=450, y=60)

lblCantidadBA = Label(ventana, text="Cantidad en bodega", font=("Arial Bold", 12))
lblCantidadBA.place(x=450, y=90)

lblPrecioUA = Label(ventana, text="Precio Unitario", font=("Arial Bold", 12))
lblPrecioUA.place(x=450, y=120)

lblCantidadVA = Label(ventana, text="Cantidad de vendidos", font=("Arial Bold", 12))
lblCantidadVA.place(x=450, y=150)

lblCantidadMA = Label(ventana, text="Cantidad minima", font=("Arial Bold", 12))
lblCantidadMA.place(x=450, y=180)

tipoA = DoubleVar()
tipoA.set("Droguería")
txtTipoA = Entry(ventana, text=tipoA, state='disabled')
txtTipoA.place(x=625, y=65)

CantidadBA = DoubleVar()
CantidadBA.set(25)
txtCantidadBA = Entry(ventana, text=CantidadBA, state='disabled')
txtCantidadBA.place(x=625, y=95)

valorA = DoubleVar()
valorA.set(20)
txtValorA = Entry(ventana, text=valorA, state='disabled')
txtValorA.place(x=625, y=125)

CantidadVA = DoubleVar()
CantidadVA.set(2)
txtCantidadVA = Entry(ventana, text=CantidadVA, state='disabled')
txtCantidadVA.place(x=625, y=155)

CantidadMA = DoubleVar()
CantidadMA.set(8)
txtCantidadMA = Entry(ventana, text=CantidadMA, state='disabled')
txtCantidadMA.place(x=625, y=185)

aspirinaMinimo = int(txtCantidadMA.get())
aspirinaBodega = int(txtCantidadBA.get())
aspirinaVenta = int(txtCantidadVA.get())
precioAspirina = float(txtValorA.get())
if txtTipoA.get() == "Droguería":
    precioAspirina = precioAspirina+(precioAspirina*0.12)
elif txtTipoP.get() == "Supermercado":
    porcentaje = (precioPan/100)*4
    precioPan += porcentaje
elif txtTipoL.get() == "Papelería":
    precioLapiz = precioLapiz+(precioLapiz*0.16)

######BOTONES ASPIRINA##########
def AbastecerA():
    global aspirinaBodega
    agregar = aspirinaBodega + 1
    CantidadBA.set(agregar)
    aspirinaBodega += 1

def VenderA():
    txtVender = Entry(ventana)
    txtVender.place(x=520, y=230)

    def CantidadVenta():
        global aspirinaVenta
        global aspirinaBodega
        global aspirinaMinimo
        obVenta = int(txtVender.get())
        bodega = aspirinaBodega - obVenta
        if bodega >= aspirinaMinimo:
            quitar = aspirinaBodega - obVenta
            CantidadBA.set(quitar)
            agregar = aspirinaVenta + obVenta
            CantidadVA.set(agregar)
            aspirinaVenta += obVenta
            aspirinaBodega -= obVenta
        else:
            lblError = Label(ventana, text="Sobrepasa la cantidad mínima en bodega", font=("Arial Bold", 12))
            lblError.place(x=450, y=180)

            def btn():
                lblError.destroy()
                btnOK.destroy()
            btnOK = Button(ventana, text="OK", command=btn)
            btnOK.place(x=750, y=180)
        txtVender.destroy()
        btnAceptar.destroy()
    btnAceptar = Button(ventana, text="Aceptar", command=CantidadVenta)
    btnAceptar.place(x=600, y=230)

def CambiarA():
    txtAspirina.config(state="normal")
    txtTipoA.config(state="normal")
    txtValorA.config(state="normal")
    txtCantidadBA.config(state="normal")
    txtCantidadVA.config(state="normal")
    txtCantidadMA.config(state="normal")

    def Aceptar():
        obTipo = txtTipoA.get()
        obValor = int(txtValorA.get())
        obCantidadB = int(txtCantidadBA.get())
        obCantidadV = int(txtCantidadVA.get())
        obCantidadM = int(txtCantidadMA.get())
        tipoA.set(obTipo)
        valorA.set(obValor)
        CantidadBA.set(obCantidadB)
        CantidadVA.set(obCantidadV)
        CantidadMA.set(obCantidadM)
        txtAspirina.config(state="disabled")
        txtTipoA.config(state="disabled")
        txtValorA.config(state="disabled")
        txtCantidadBA.config(state="disabled")
        txtCantidadVA.config(state="disabled")
        txtCantidadMA.config(state="disabled")

    btnAceptar = Button(ventana, text="Aceptar", command=Aceptar)
    btnAceptar.place(x=630, y=205)

btnAbastecerA = Button(ventana, text="Abastecer", command=AbastecerA)
btnAbastecerA.place(x=450, y=205)
btnVenderA = Button(ventana, text="Vender", command=VenderA)
btnVenderA.place(x=520, y=205)
btnCambiarA = Button(ventana, text="Cambiar", command=CambiarA)
btnCambiarA.place(x=575, y=205)

######################################PAN########################################3

lblPan = DoubleVar()
lblPan.set("PAN")
txtPan = Entry(ventana, text=lblPan, state='disabled')
txtPan.place(x=450, y=260)
lblTipo = Label(ventana, text="Tipo", font=("Arial Bold", 12))
lblTipo.place(x=450, y=290)

lblCantidadB = Label(ventana, text="Cantidad en bodega", font=("Arial Bold", 12))
lblCantidadB.place(x=450, y=320)

lblPrecioU = Label(ventana, text="Precio Unitario", font=("Arial Bold", 12))
lblPrecioU.place(x=450, y=350)

lblCantidadV = Label(ventana, text="Cantidad de vendidos", font=("Arial Bold", 12))
lblCantidadV.place(x=450, y=380)

lblCantidadM = Label(ventana, text="Cantidad minima", font=("Arial Bold", 12))
lblCantidadM.place(x=450, y=410)


tipoP = DoubleVar()
tipoP.set("Supermercado")
txtTipoP = Entry(ventana, text=tipoP, state='disabled')
txtTipoP.place(x=625, y=295)

CantidadBP = DoubleVar()
CantidadBP.set(100)
txtCantidadBP = Entry(ventana, text=CantidadBP, state='disabled')
txtCantidadBP.place(x=625, y=325)

valorP = DoubleVar()
valorP.set(30)
txtValorP = Entry(ventana, text=valorP, state='disabled')
txtValorP.place(x=625, y=355)

CantidadVP = DoubleVar()
CantidadVP.set(10)
txtCantidadVP = Entry(ventana, text=CantidadVP, state='disabled')
txtCantidadVP.place(x=625, y=385)

CantidadMP = DoubleVar()
CantidadMP.set(15)
txtCantidadMP = Entry(ventana, text=CantidadMP, state='disabled')
txtCantidadMP.place(x=625, y=415)

panMinimo = int(txtCantidadMP.get())
panBodega = int(txtCantidadBP.get())
panVenta = int(txtCantidadVP.get())
precioPan = float(txtValorP.get())
if txtTipoP.get() == "Supermercado":
    porcentaje = (precioPan/100)*4
    precioPan += porcentaje
elif txtTipoA.get() == "Droguería":
    precioAspirina = precioAspirina+(precioAspirina*0.12)
elif txtTipoL.get() == "Papelería":
    precioLapiz = precioLapiz+(precioLapiz*0.16)

######BOTONES PAN##########
def AbastecerP():
    global panBodega
    agregar = panBodega + 1
    CantidadBP.set(agregar)
    panBodega += 1

def VenderP():
    txtVender = Entry(ventana)
    txtVender.place(x=520, y=480)
    def CantidadVenta():
        global panVenta
        global panBodega
        global panMinimo
        obVenta = int(txtVender.get())
        bodega = panBodega - obVenta
        if bodega >= panMinimo:
            quitar = panBodega - obVenta
            CantidadBP.set(quitar)
            agregar = panVenta + obVenta
            CantidadVP.set(agregar)
            panVenta += obVenta
            panBodega -= obVenta
        else:
            lblError = Label(ventana, text="Sobrepasa la cantidad mínima en bodega", font=("Arial Bold", 12))
            lblError.place(x=450, y=410)

            def btn():
                lblError.destroy()
                btnOK.destroy()

            btnOK = Button(ventana, text="OK", command=btn)
            btnOK.place(x=750, y=410)
        txtVender.destroy()
        btnAceptar.destroy()
    btnAceptar = Button(ventana, text="Aceptar", command=CantidadVenta)
    btnAceptar.place(x=600, y=480)

def CambiarP():
    txtPan.config(state="normal")
    txtTipoP.config(state="normal")
    txtValorP.config(state="normal")
    txtCantidadBP.config(state="normal")
    txtCantidadVP.config(state="normal")
    txtCantidadMP.config(state="normal")

    def Aceptar():
        obTipo = txtTipoP.get()
        obValor = int(txtValorP.get())
        obCantidadB = int(txtCantidadBP.get())
        obCantidadV = int(txtCantidadVP.get())
        obCantidadM = int(txtCantidadMP.get())
        tipoP.set(obTipo)
        valorP.set(obValor)
        CantidadBP.set(obCantidadB)
        CantidadVP.set(obCantidadV)
        CantidadMP.set(obCantidadM)
        txtPan.config(state="disabled")
        txtTipoP.config(state="disabled")
        txtValorP.config(state="disabled")
        txtCantidadBP.config(state="disabled")
        txtCantidadVP.config(state="disabled")
        txtCantidadMP.config(state="disabled")

    btnAceptar = Button(ventana, text="Aceptar", command=Aceptar)
    btnAceptar.place(x=630, y=450)

btnAbastecerP = Button(ventana, text="Abastecer", command=AbastecerP)
btnAbastecerP.place(x=450, y=450)
btnVenderP = Button(ventana, text="Vender", command=VenderP)
btnVenderP.place(x=520, y=450)
btnCambiarP = Button(ventana, text="Cambiar", command=CambiarP)
btnCambiarP.place(x=575, y=450)

################################OPCIONES##########################################
lblOpciones = Label(ventana, text="Opciones", font=("Arial Bold", 13))
lblOpciones.place(x=320, y=500)


def masVendido():
    if lapizVenta > borradorVenta and lapizVenta > aspirinaVenta and lapizVenta > panVenta:
        lblMasVendido = Label(ventana, text="El producto más vendido es: Lápiz ", font=("Arial Bold", 12))
        lblMasVendido.place(x=10, y=600)
    elif borradorVenta > lapizVenta and borradorVenta > aspirinaVenta and borradorVenta >  panVenta:
        lblMasVendido = Label(ventana, text="El producto más vendido es: Borrador ", font=("Arial Bold", 12))
        lblMasVendido.place(x=10, y=600)
    elif aspirinaVenta > lapizVenta and aspirinaVenta > borradorVenta and aspirinaVenta > panVenta:
        lblMasVendido = Label(ventana, text="El producto más vendido es: Aspirina ", font=("Arial Bold", 12))
        lblMasVendido.place(x=10, y=600)
    elif panVenta > lapizVenta and panVenta > borradorVenta and panVenta > aspirinaVenta:
        lblMasVendido = Label(ventana, text="El producto más vendido es: Pan ", font=("Arial Bold", 12))
        lblMasVendido.place(x=10, y=600)
    def btn():
        lblMasVendido.destroy()
        btnOK.destroy()
    btnOK = Button(ventana, text="OK", command=btn)
    btnOK.place(x=300, y=600)

def menosVendido():
    if lapizVenta < borradorVenta and lapizVenta < aspirinaVenta and lapizVenta < panVenta:
        lblMenosVendido = Label(ventana, text="El producto menos vendido es: Lápiz ", font=("Arial Bold", 12))
        lblMenosVendido.place(x=10, y=600)
    elif borradorVenta < lapizVenta and borradorVenta < aspirinaVenta and borradorVenta <  panVenta:
        lblMenosVendido = Label(ventana, text="El producto menos vendido es: Borrador ", font=("Arial Bold", 12))
        lblMenosVendido.place(x=10, y=600)
    elif aspirinaVenta < lapizVenta and aspirinaVenta < borradorVenta and aspirinaVenta < panVenta:
        lblMenosVendido = Label(ventana, text="El producto menos vendido es: Aspirina ", font=("Arial Bold", 12))
        lblMenosVendido.place(x=10, y=600)
    elif panVenta < lapizVenta and panVenta < borradorVenta and panVenta < aspirinaVenta:
        lblMenosVendido = Label(ventana, text="El producto menos vendido es: Pan ", font=("Arial Bold", 12))
        lblMenosVendido.place(x=10, y=600)
    def btn():
        lblMenosVendido.destroy()
        btnOK.destroy()
    btnOK = Button(ventana, text="OK", command=btn)
    btnOK.place(x=300, y=600)

def calculos():
    global total
    global totalVendidos
    LapicesDinOb = precioLapiz*lapizVenta
    BorradoresDinOb = precioBorrador*borradorVenta
    AspirinasDinOb = precioAspirina*aspirinaVenta
    PanDinOb = precioPan*panVenta
    total= LapicesDinOb+BorradoresDinOb+AspirinasDinOb+PanDinOb
    totalVendidos = lapizVenta+borradorVenta+aspirinaVenta+panVenta

def dineroCaja():
    calculos()
    lblTotal = Label(ventana, text=f"${total} obtenidos", font=("Arial Bold", 12))
    lblTotal.place(x=10, y=600)
    def btn():
        lblTotal.destroy()
        btnOK.destroy()
    btnOK = Button(ventana, text="OK", command=btn)
    btnOK.place(x=300, y=600)
def promedio():
    calculos()
    promedioDinero = total/totalVendidos
    lblPromedio = Label(ventana, text=f"${promedioDinero} de promedio por producto", font=("Arial Bold", 12))
    lblPromedio.place(x=10, y=600)
    def btn():
        lblPromedio.destroy()
        btnOK.destroy()
    btnOK = Button(ventana, text="OK", command=btn)
    btnOK.place(x=400, y=600)



btnMasVendido = Button(ventana, text="Producto más vendido", command=masVendido)
btnMasVendido.place(x=10, y=550)

btnMenosVendido = Button(ventana, text="Producto menos vendido", command=menosVendido)
btnMenosVendido.place(x=150, y=550)

btnPromedio = Button(ventana, text="Promedio",command=promedio)
btnPromedio.place(x=300, y=550)

btnDineroCaja = Button(ventana, text="Dinero en caja", command=dineroCaja)
btnDineroCaja.place(x=370, y=550)

ventana.mainloop()

