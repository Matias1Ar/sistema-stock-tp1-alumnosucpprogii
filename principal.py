from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.configure(bg='black')
root.withdraw()

window = Toplevel()
window.title("Programación II - Sistema Stock A.Ozuna")
window.geometry('955x675')
window.resizable(False,False)
window.configure(bg='black')
window.protocol("WM_DELETE_WINDOW", root.destroy)

but = Button(window, text='deiconify')
but['command'] = root.deiconify
but.pack()

#Variables globales
entr_var=0
triples =[[18, 0, 5, 550,"Papelería"],[25, 0, 8, 106.5, "Droguería"],[30, 0, 10, 207.3,"Papelería"],[15, 0, 20, 150,"Supermercado"]]

#Imagen Lápiz
path_lapiz=r'C:\Users\Agus\Documents\GitHub\sistema-stock-tp1-alumnosucpprogii\images\pencil.jpg'
Frame_X_Lapiz=0
Frame_Y_Lapiz=0
posiciones_labels_Lapiz=[20,40, 0, 0, 200,30,70,110,150,190]
posiciones_entrys_Lapiz=[330,35,75,115,155,195]

#Imagen Amoxicilina
path_pill=r'C:\Users\Agus\Documents\GitHub\sistema-stock-tp1-alumnosucpprogii\images\pill.png'
Frame_X_pill=478
Frame_Y_pill=0
posiciones_labels_pill=[498,40, 478, 0, 678,30,70,110,150,190]
posiciones_entrys_pill=[808,35,75,115,155,195]

#Imagen Trincheta
path_trincheta=r'C:\Users\Agus\Documents\GitHub\sistema-stock-tp1-alumnosucpprogii\images\trench.png'
Frame_X_trincheta=0
Frame_Y_trincheta=260
posiciones_labels_trincheta=[20, 300, 0, 260, 200, 295, 335, 375, 415,455]
posiciones_entrys_trincheta=[330, 295, 335, 375, 415,455]

#Imagen Huevos
path_huevos=r'C:\Users\Agus\Documents\GitHub\sistema-stock-tp1-alumnosucpprogii\images\eggs.png'
Frame_X_huevos=478
Frame_Y_huevos=260
posiciones_labels_huevos=[498, 300, 478, 260, 678, 295, 335, 375, 415,455]
posiciones_entrys_huevos=[808, 295, 335, 375, 415,455]

def seccion(path,Producto, Frame_X, Frame_Y, posiciones_labels, posiciones_entrys, Cantidad_Inicial, cantidad_minima, Tipo_, valor_unitario,x):
    global triples
    Frame_seccion = Frame(window, width=491, height=250,bg='black',relief=RAISED,bd=25)
    Frame_seccion.place(x=Frame_X,y=Frame_Y)
    Cantidad_inicial_var=IntVar(value=Cantidad_Inicial)
    Cantidad_minima_var=IntVar(value=cantidad_minima)
    Cantidad_vendidas_var=IntVar(0)
    Valor_unitario_var=IntVar(value=valor_unitario)
    Tipo_var=StringVar(window, triples[x][4])
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image = img, relief=SUNKEN)
    panel.place(x=posiciones_labels[0],y=posiciones_labels[1])
    panel.image = img
    label_producto = Label(window, text=Producto,bg='black',font=('Open Sans',16),fg='white', relief=RAISED)
    label_producto.place(x=posiciones_labels[2],y=posiciones_labels[3]) #Label2
    Tipo = Label(window, text='Tipo: ',bg='black',fg='purple', font=('Open Sans',10))
    Tipo.place(x=posiciones_labels[4],y=posiciones_labels[5]) #Label3
    Entry_Tipo = Entry(window,relief=SUNKEN, justify=CENTER, textvariable=Tipo_var, state=DISABLED)
    Entry_Tipo.place(x=posiciones_entrys[0],y=posiciones_entrys[1]) #Entry1
    Cantidad_bodega = Label(window, text='Cantidad bodega: ',bg='black',fg='purple', font=('Open Sans',10))
    Cantidad_bodega.place(x=posiciones_labels[4],y=posiciones_labels[6]) #Label4
    Entry_Cantidad_bodega = Entry(window,relief=SUNKEN, textvariable=Cantidad_inicial_var, justify=CENTER, state=DISABLED)
    Entry_Cantidad_bodega.place(x=posiciones_entrys[0],y=posiciones_entrys[2]) #Entry2
    Valor_unitario = Label(window, text='Valor unitario',bg='black',fg='purple', font=('Open Sans',10))
    Valor_unitario.place(x=posiciones_labels[4],y=posiciones_labels[7]) #Label5
    Entry_Valor_unitario = Entry(window,relief=SUNKEN, textvariable=Valor_unitario_var, justify=CENTER, state=DISABLED)
    Entry_Valor_unitario.place(x=posiciones_entrys[0],y=posiciones_entrys[3]) #Entry3
    Cantidad_vendidas = Label(window, text='Cantidad vendidas: ',bg='black',fg='purple', font=('Open Sans',10))
    Cantidad_vendidas.place(x=posiciones_labels[4],y=posiciones_labels[8]) #Label6
    Entry_Cantidad_vendidas = Entry(window,relief=SUNKEN, justify=CENTER, textvariable=Cantidad_vendidas_var, state=DISABLED)
    Entry_Cantidad_vendidas.place(x=posiciones_entrys[0],y=posiciones_entrys[4]) #Entry4
    Cantidad_minima = Label(window, text='Cantidad mínima: ',bg='black',fg='purple', font=('Open Sans',10))
    Cantidad_minima.place(x=posiciones_labels[4],y=posiciones_labels[9]) #Label7
    Entry_Cantidad_minima = Entry(window,relief=SUNKEN, textvariable=Cantidad_minima_var, justify=CENTER, state=DISABLED)
    Entry_Cantidad_minima.place(x=posiciones_entrys[0],y=posiciones_entrys[5]) #Entry5
    botones = Frame(window, height=20,width=47)
    botones.place(x=Frame_X,y=Frame_Y+235)
    def Abastecer():
        global entr_var
        root.deiconify()
        entr_var=IntVar()
        lbl = Label(root, text='Ingrese la cantidad',bg='black',fg='purple',font=('Open Sans',12))
        lbl.pack()
        entr = Entry(root, textvariable=entr_var, justify=CENTER)
        entr.pack()
        def Aceptar():
            global triples, Cantidad_Minima_
            if triples[x][0]<=triples[x][2]:
                triples[x][0]=triples[x][0]+entr_var.get()
                Cantidad_inicial_var.set(triples[x][0])
            elif triples[x][0]>triples[x][2]:
                string= "El stock aún no ha alcanzado la cantidad minima: ",triples[x][2]
                messagebox.showinfo('Error de restock',string)
            root.withdraw()
            lbl.destroy()
            entr.destroy()
            Botton_Aceptar.destroy()
        Botton_Aceptar = Button(root, text='Aceptar', command=Aceptar, relief=SUNKEN,bg='black',fg='purple',width=10,justify=CENTER, font=('Open Sans',12))
        Botton_Aceptar.pack()
    Abastecer = Button(botones, text='Abastecer', command=Abastecer, relief=SUNKEN,bg='black',fg='purple',width=21,justify=CENTER, font=('Open Sans',9))
    Abastecer.pack(side=LEFT)
    def Vender():
        global entr_var
        root.deiconify()
        entr_var=IntVar()
        lbl = Label(root, text='Ingrese la cantidad',bg='black',fg='purple',font=('Open Sans',12))
        lbl.pack()
        entr = Entry(root, textvariable=entr_var, justify=CENTER)
        entr.pack()
        def Aceptar():
            global triples,entr_var
            if triples[x][0]>0 and entr_var.get()<=triples[x][0]:
                triples[x][0]=triples[x][0]-entr_var.get()
                Cantidad_inicial_var.set(triples[x][0])
                triples[x][1]=triples[x][1]+entr_var.get()
                Cantidad_vendidas_var.set(triples[x][1])
            elif triples[x][0]==0:
                messagebox.showinfo('Faltante de Stock',"No hay unidades disponibles.")
            elif entr_var.get()>triples[x][0]:
                string = "Sólo hay "+str(triples[x][0])+" unidades disponibles."
                messagebox.showinfo('Faltante de Stock',string)
            root.withdraw()  
            lbl.destroy()
            entr.destroy()
            Botton_Aceptar.destroy()
        Botton_Aceptar = Button(root, text='Aceptar', command=Aceptar, relief=SUNKEN,bg='black',fg='purple',width=10,justify=CENTER, font=('Open Sans',12))
        Botton_Aceptar.pack()
    Vender = Button(botones, text='Vender', command= Vender, relief=SUNKEN,bg='black',fg='purple',width=21,justify=CENTER, font=('Open Sans',9))
    Vender.pack(side=LEFT)
    def Cambiar():
        Entry_Tipo.configure(state=NORMAL) #Entry1
        Entry_Cantidad_bodega.configure(state=NORMAL) #Entry2
        Entry_Valor_unitario.configure(state=NORMAL) #Entry3
        Entry_Cantidad_vendidas.configure(state=NORMAL) #Entry4
        Entry_Cantidad_minima.configure(state=NORMAL) #Entry5
        botones.place(x=-5000,y=-5000)
        def Aplicar_Cambios():
            global triples
            Entry_Tipo.configure(state=DISABLED) #Entry1
            Tipo_var.set(Tipo_var.get())
            triples[x][4]=Tipo_var.get()
            Entry_Cantidad_bodega.configure(state=DISABLED) #Entry2
            Cantidad_inicial_var.set(Cantidad_inicial_var.get())
            triples[x][0]=Cantidad_inicial_var.get()
            Entry_Valor_unitario.configure(state=DISABLED) #Entry3
            Valor_unitario_var.set(Valor_unitario_var.get())
            triples[x][3]=Valor_unitario_var.get()
            Entry_Cantidad_vendidas.configure(state=DISABLED) #Entry4
            Cantidad_vendidas_var.set(Cantidad_vendidas_var.get())
            triples[x][1]=Cantidad_vendidas_var.get()
            Lista_variables_secciones[x]=Cantidad_vendidas_var.get()
            Entry_Cantidad_minima.configure(state=DISABLED) #Entry5 
            Cantidad_minima_var.set(Cantidad_minima_var.get())
            triples[x][2]=Cantidad_minima_var.get()
            Botton_Aplicar.destroy()
            botones.place(x=Frame_X,y=Frame_Y+235)
        Botton_Aplicar = Button(window, text='Aplicar cambios', command=Aplicar_Cambios,width=30, relief=SUNKEN,bg='black',fg='purple',justify=CENTER, font=('Open Sans',9))
        Botton_Aplicar.place(x=(Frame_X+491)/4,y=Frame_Y+235)
    Cambiar = Button(botones, text='Cambiar', command=Cambiar, relief=SUNKEN,bg='black',fg='purple',width=22,justify=CENTER, font=('Open Sans',9))
    Cambiar.pack(side=LEFT)
    def opciones():
        canvas = Canvas(window, width=976, height=150,bg='black')
        canvas.place(x=0,y=520)
        canvas.create_line(95,0,980,0,fill='purple',width=25)
        canvas.create_line(0,700,0,20,fill='purple',width=25)
        label = Label(canvas, text='Opciones',bg='black',fg='white', font=('Open Sans',16), relief=RAISED)
        label.place(x=2,y=3)
        botones = Frame(window, height=60,width=98)
        botones.place(x=60,y=560)
        def Producto_mas_vendido():
            global triples
            lista_ventas = [triples[0][1], triples[1][1], triples[2][1], triples[3][1]]
            if lista_ventas.index(max(lista_ventas))==0:
                id_producto_mas_vendido="Lápiz"
            elif lista_ventas.index(max(lista_ventas))==1:
                id_producto_mas_vendido="Amoxicilina"
            elif lista_ventas.index(max(lista_ventas))==2:
                id_producto_mas_vendido="Trincheta"
            elif lista_ventas.index(max(lista_ventas))==3:
                id_producto_mas_vendido="Huevos"
            valor_Producto_mas_vendido=max(lista_ventas)
            string=str('El producto más vendido es: ',id_producto_mas_vendido,"con ",str(valor_Producto_mas_vendido)," unidades.")
            root.deiconify()
            lbl=Label(root, text=string,bg='black',fg='purple')
            lbl.pack()  
        Producto_mas_vendido = Button(botones, text='Producto más vendido', command=Producto_mas_vendido, relief=SUNKEN,bg='black',fg='purple',width=30,height=5, justify=CENTER, font=('Open Sans',9))
        Producto_mas_vendido.pack(side=LEFT)
        def Producto_menos_vendido():
            global triples,lista_ventas
            if lista_ventas.index(min(lista_ventas))==0:
                id_producto_menos_vendido="Lápiz"
            elif lista_ventas.index(min(lista_ventas))==1:
                id_producto_menos_vendido="Amoxicilina"
            elif lista_ventas.index(min(lista_ventas))==2:
                id_producto_menos_vendido="Trincheta"
            elif lista_ventas.index(min(lista_ventas))==3:
                id_producto_menos_vendido="Huevos"
            valor_Producto_menos_vendido=min(lista_ventas)
            string='El producto menos vendido es: ',id_producto_menos_vendido,"con ",str(valor_Producto_menos_vendido)," unidades."
            root.deiconify()
            lbl=Label(root, text=string,bg='black',fg='purple')
            lbl.pack() 
        Producto_menos_vendido = Button(botones, text='Producto menos vendido', command=Producto_menos_vendido, relief=SUNKEN,bg='black',fg='purple',width=30,height=5, justify=CENTER, font=('Open Sans',9))
        Producto_menos_vendido.pack(side=LEFT)
        def Promedio_ventas():
            global triples
            lista_ventas = [triples[0][1], triples[1][1], triples[2][1], triples[3][1]]
            promedio=sum(lista_ventas)/len(lista_ventas)
            string='El promedio de ventas es de: ',promedio,' unidades.'
            root.deiconify()
            lbl=Label(root, text=string,bg='black',fg='purple')
            lbl.pack()
        Promedio_ventas = Button(botones, text='Promedio ventas', command=Promedio_ventas, relief=SUNKEN,bg='black',fg='purple',width=30,height=5, justify=CENTER, font=('Open Sans',9))
        Promedio_ventas.pack(side=LEFT)
        def Dinero_en_caja():
            global triples
            dinero_por_producto = [0,0,0,0]
            dinero_por_producto[0]=triples[0][1]*triples[0][3]
            dinero_por_producto[1]=triples[1][1]*triples[1][3]
            dinero_por_producto[2]=triples[2][1]*triples[2][3]
            dinero_por_producto[3]=triples[3][1]*triples[3][3]
            total_caja=sum(dinero_por_producto)
            string='El dinero total en caja es de: $',total_caja
            root.deiconify()
            lbl=Label(root, text=string,bg='black',fg='purple')
            lbl.pack()  
        Dinero_en_caja = Button(botones, text='Dinero en caja', command=Dinero_en_caja, relief=SUNKEN,bg='black',fg='purple',width=30,height=5, justify=CENTER, font=('Open Sans',9))
        Dinero_en_caja.pack(side=LEFT)
    opciones()
      
seccion(path_lapiz, "Lápiz", 0 , 0,  posiciones_labels_Lapiz, posiciones_entrys_Lapiz, triples[0][0], triples[0][2],"Papelería", triples[0][3],0)
seccion(path_pill, "Amoxicilina", 478 , 0,  posiciones_labels_pill, posiciones_entrys_pill, triples[1][0], triples[1][2],"Droguería", triples[1][3], 1)
seccion(path_trincheta, "Trincheta", 0 , 260,  posiciones_labels_trincheta, posiciones_entrys_trincheta, triples[2][0], triples[2][2],"Papelería", triples[2][3], 2)
seccion(path_huevos, "Huevos", 478 , 260,  posiciones_labels_huevos, posiciones_entrys_huevos, triples[3][0], triples[3][2],"Supermercado", triples[3][3], 3)

window.mainloop()

