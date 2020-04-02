import json

with open("productos.json", encoding='utf-8') as archivoProducto:
    listaProductos = json.load(archivoProducto)

def guardarCambios():
    with open("productos.json", "w") as archivoP:
        json.dump(listaProductos,archivoP)

def agregarProducto(nombre,tipo,cantidadB,valorUnitario,cantindadV,cantidadM):
    dic = dict()
    dic["nombre"] = nombre
    dic["tipo"] = tipo
    dic["cantidad_bodega"] = cantidadB
    dic["valor_unitario"] = valorUnitario
    dic["cantidad_vendida"] = cantindadV
    dic["cantidad_minima"] = cantidadM
    listaProductos.append(dic)
    guardarCambios()

def listaProdcutos():
    return listaProductos

def restablecerValoresVendidos():
    for un_producto in listaProductos:
        un_producto["cantidad_vendida"] = 0

def cambiarProducto(nombreActual,nombreNew,tipo,cantidadB,valorUnitario,cantidadM):
    for un_producto in listaProductos:
        if nombreActual==un_producto["nombre"]:
            un_producto["nombre"] = nombreNew
            un_producto["tipo"] = tipo
            un_producto["cantidad_bodega"] = cantidadB
            un_producto["valor_unitario"] = valorUnitario
            un_producto["cantidad_vendida"] = 0
            un_producto["cantidad_minima"] = cantidadM
            guardarCambios()

def venderProducto(nombre,cant):
    for un_producto in listaProductos:
        if un_producto["nombre"]==nombre:
            if un_producto["cantidad_bodega"]>=cant:
                un_producto["cantidad_bodega"] -= cant
                un_producto["cantidad_vendida"] += cant
                guardarCambios()
            else:
                error = 0-"asd"

def precioFinal(producto,cant):
    total = producto["valor_unitario"]*cant
    if producto["tipo"] == 0:
        res = total*0.16
        total = total+res
    elif producto["tipo"] == 1:
        res = total*0.4
        total = total+res
    elif producto["tipo"] == 2:
        res = total*0.12
        total = total+res
    return total

def comprarProducto(nombre,cant):
    for un_producto in listaProductos:
        if nombre==un_producto["nombre"]:
            if un_producto["cantidad_bodega"]<=un_producto["cantidad_minima"]:
                un_producto["cantidad_bodega"] += cant
                guardarCambios()
            else:
                error = "asd"-5

def productoMasVendido():
    mayor = 0
    pd_mayor = ""
    for un_producto in listaProductos:
        cant=un_producto["cantidad_vendida"]
        if cant>mayor:
            mayor = cant
            pd_mayor=un_producto["nombre"]
        elif pd_mayor == "":
            pd_mayor = "Ninguno fue vendido"
    return pd_mayor

def productoMenosVendido():
    menor = 10000000
    pd_mayor = ""
    for un_producto in listaProductos:
        cant=un_producto["cantidad_vendida"]
        if cant<=menor:
            menor = cant
            pd_mayor=un_producto["nombre"]
    return pd_mayor

def totalVendidos():
    cant = 0
    for un_producto in listaProductos:
        cant+=un_producto["cantidad_vendida"]
    return cant
