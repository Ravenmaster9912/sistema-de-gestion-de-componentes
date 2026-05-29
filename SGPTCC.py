import tkinter
from tkinter import ttk
import psycopg2
from psycopg2 import sql
from pathlib import Path
import os
import subprocess
import getpass

connection = psycopg2.connect(
host='localhost',
user='postgres',
password='mastered',
database='SGPTCC',
port='5432'
)

def consulta(query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
    except Exception as Ex:
        print(Ex)

def mod(query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        alerta = tkinter.Label(ventana,text="La modificacion se realizo con exito...")
        alerta.place(x=400,y=400)
        def borrar_alerta():
            alerta.destroy()
        ventana.after(2000,borrar_alerta)
    except Exception as Ex:
        print(Ex)
        alerta2 = tkinter.Label(ventana,text="La modificacion ha fallado...")
        alerta2.place(x=400,y=400)
        def borrar_alerta():
            alerta2.destroy()
        ventana.after(2000,borrar_alerta)

def agregarCli():
    lblag = tkinter.Label(ventana, text= "Agregar")
    lblag.place(x=400,y=30)

    p1= tkinter.Label(ventana, text= "Ingresa ID: ")
    p1.place(x=200,y=80)

    en1 = tkinter.Entry(ventana)
    en1.place(x=400,y=80)

    p2 = tkinter.Label(ventana,text="Ingresa el nombre del cliente: ")
    p2.place(x=200,y=130)

    en2 = tkinter.Entry(ventana)
    en2.place(x=400,y=130)

    p3 = tkinter.Label(ventana,text="Ingresa numero de telefono: ")
    p3.place(x=200,y=180)

    en3 = tkinter.Entry(ventana)
    en3.place(x=400,y=180)

    p4 = tkinter.Label(ventana,text="Ingresa correo E. : ")
    p4.place(x=200,y=230)

    en4 = tkinter.Entry(ventana)
    en4.place(x=400,y=230)

    def confirmar():
        id = en1.get()
        nombre = en2.get()
        telefono = en3.get()
        correo = en4.get()
        query = f"INSERT INTO cliente(id_cliente,nombre,telefono,corro) VALUES ({id} ,'{nombre}',{telefono},'{correo}');"
        mod(query)

    confirm = tkinter.Button(ventana,text="Confirmar",command= confirmar)
    confirm.place(x=400,y=280)

    def eliminar():
        lblag.destroy()
        p1.destroy()
        p2.destroy()
        p3.destroy()
        p4.destroy()
        en1.destroy()
        en2.destroy()
        en3.destroy()
        en4.destroy()
        confirm.destroy()
        clear.destroy()
        desbloquear()

    clear = tkinter.Button(ventana,text="Cancelar",command=eliminar)
    clear.place(x=500,y=280)

def agregarPro():
    lblag = tkinter.Label(ventana, text= "Agregar")
    lblag.place(x=400,y=30)

    p1= tkinter.Label(ventana, text= "Ingresa ID: ")
    p1.place(x=200,y=80)

    en1 = tkinter.Entry(ventana)
    en1.place(x=450,y=80)

    p2 = tkinter.Label(ventana,text="Ingresa descripcion: ")
    p2.place(x=200,y=130)

    en2 = tkinter.Entry(ventana)
    en2.place(x=450,y=130)

    p3 = tkinter.Label(ventana,text="Ingresa marca: ")
    p3.place(x=200,y=180)

    en3 = tkinter.Entry(ventana)
    en3.place(x=450,y=180)
    
    p4 = tkinter.Label(ventana,text="Ingresa fecha de recibido (dd/mm/aa): ")
    p4.place(x=200,y=230)

    en4 = tkinter.Entry(ventana)
    en4.place(x=450,y=230)
    
    p5 = tkinter.Label(ventana,text="Ingresa empleado que recibe: ")
    p5.place(x=200,y=280)

    en5 = tkinter.Entry(ventana)
    en5.place(x=450,y=280)
    
    p6 = tkinter.Label(ventana,text="Ingresa proveedor: ")
    p6.place(x=200,y=330)

    en6 = tkinter.Entry(ventana)
    en6.place(x=450,y=330)
    
    p7 = tkinter.Label(ventana,text="Ingresa precio: ")
    p7.place(x=200,y=380)

    en7 = tkinter.Entry(ventana)
    en7.place(x=450,y=380)

    def confirmar():
        id = en1.get()
        des = en2.get()
        marca = en3.get()
        fecha = en4.get()
        emp = en5.get()
        prov = en6.get()
        precio = en7.get()
        query = f"INSERT INTO producto(id_prodcuto,descripcion,marca,fecha_recibido,recibe_empleado,proveedor,precio) VALUES ({id} ,'{des}','{marca}','{fecha}',{emp},{prov},{precio});"
        mod(query)

    confirm = tkinter.Button(ventana,text="Confirmar",command= confirmar)
    confirm.place(x=400,y=430)

    def eliminar():
        lblag.destroy()
        p1.destroy()
        p2.destroy()
        p3.destroy()
        p4.destroy()
        p5.destroy()
        p6.destroy()
        p7.destroy()
        en1.destroy()
        en2.destroy()
        en3.destroy()
        en4.destroy()
        en5.destroy()
        en6.destroy()
        en7.destroy()
        confirm.destroy()
        clear.destroy()
        desbloquear()

    clear = tkinter.Button(ventana,text="Cancelar",command=eliminar)
    clear.place(x=500,y=430)

def agregarEmp():
    lblag = tkinter.Label(ventana, text= "Agregar")
    lblag.place(x=400,y=30)

    p1= tkinter.Label(ventana, text= "Ingresa ID: ")
    p1.place(x=200,y=80)

    en1 = tkinter.Entry(ventana)
    en1.place(x=400,y=80)

    p2 = tkinter.Label(ventana,text="Ingresa el nombre del empleado: ")
    p2.place(x=200,y=130)

    en2 = tkinter.Entry(ventana)
    en2.place(x=400,y=130)

    p3 = tkinter.Label(ventana,text="Ingresa numero de departamento: ")
    p3.place(x=200,y=180)

    en3 = tkinter.Entry(ventana)
    en3.place(x=400,y=180)

    def confirmar():
        id = en1.get()
        nombre = en2.get()
        dep = en3.get()
        query = f"INSERT INTO empleado(id_empleado,nombre_e,departamento) VALUES ({id} ,'{nombre}',{dep});"
        mod(query)

    confirm = tkinter.Button(ventana,text="Confirmar",command= confirmar)
    confirm.place(x=400,y=240)

    def eliminar():
        lblag.destroy()
        p1.destroy()
        p2.destroy()
        p3.destroy()
        en1.destroy()
        en2.destroy()
        en3.destroy()
        confirm.destroy()
        clear.destroy()
        desbloquear()

    clear = tkinter.Button(ventana,text="Cancelar",command=eliminar)
    clear.place(x=500,y=240)

def agregarP():
    lblag = tkinter.Label(ventana, text= "Agregar")
    lblag.place(x=400,y=30)

    p1= tkinter.Label(ventana, text= "Ingresa ID: ")
    p1.place(x=200,y=80)

    en1 = tkinter.Entry(ventana)
    en1.place(x=450,y=80)

    p2 = tkinter.Label(ventana,text="Ingresa el ID del cliente: ")
    p2.place(x=200,y=130)

    en2 = tkinter.Entry(ventana)
    en2.place(x=450,y=130)

    p3 = tkinter.Label(ventana,text="Ingresa fecha de pedido (dd/mm/aa): ")
    p3.place(x=200,y=180)

    en3 = tkinter.Entry(ventana)
    en3.place(x=450,y=180)
    
    p4 = tkinter.Label(ventana,text="Ingresa nombre del cliente: ")
    p4.place(x=200,y=230)

    en4 = tkinter.Entry(ventana)
    en4.place(x=450,y=230)
    
    p5 = tkinter.Label(ventana,text="Ingresa correo del cliente: ")
    p5.place(x=200,y=280)

    en5 = tkinter.Entry(ventana)
    en5.place(x=450,y=280)
    
    p6 = tkinter.Label(ventana,text="Ingresa datos de producto (id a comprar): ")
    p6.place(x=200,y=330)

    en6 = tkinter.Entry(ventana)
    en6.place(x=450,y=330)

    def confirmar():
        id = en1.get()
        cliente = en2.get()
        fecha = en3.get()
        nombre = en4.get()
        correo = en5.get()
        datosP = en6.get()
        query = f"INSERT INTO pedido(id_pedido,cliente,fecha_pedido,nombre_cliente,correo_cliente,datos_producto) VALUES ({id} ,{cliente},'{fecha}','{nombre}','{correo}',{datosP});"
        mod(query)

    confirm = tkinter.Button(ventana,text="Confirmar",command= confirmar)
    confirm.place(x=400,y=400)

    def eliminar():
        lblag.destroy()
        p1.destroy()
        p2.destroy()
        p3.destroy()
        p4.destroy()
        p5.destroy()
        p6.destroy()
        en1.destroy()
        en2.destroy()
        en3.destroy()
        en4.destroy()
        en5.destroy()
        en6.destroy()
        confirm.destroy()
        clear.destroy()
        desbloquear()

    clear = tkinter.Button(ventana,text="Cancelar",command=eliminar)
    clear.place(x=500,y=400)

def agregarProv():
    lblag = tkinter.Label(ventana, text= "Agregar")
    lblag.place(x=400,y=30)

    p1= tkinter.Label(ventana, text= "Ingresa ID: ")
    p1.place(x=200,y=80)

    en1 = tkinter.Entry(ventana)
    en1.place(x=400,y=80)

    p2 = tkinter.Label(ventana,text="Ingresa el nombre de la empresa: ")
    p2.place(x=200,y=130)

    en2 = tkinter.Entry(ventana)
    en2.place(x=400,y=130)

    p3 = tkinter.Label(ventana,text="Ingresa numero de telefono: ")
    p3.place(x=200,y=180)

    en3 = tkinter.Entry(ventana)
    en3.place(x=400,y=180)

    def confirmar():
        id = en1.get()
        nombre = en2.get()
        tel = en3.get()
        query = f"INSERT INTO proveedor(id_proveedor,nombre_empresa,telefono_p) VALUES ({id} ,'{nombre}',{tel});"
        mod(query)

    confirm = tkinter.Button(ventana,text="Confirmar",command= confirmar)
    confirm.place(x=400,y=240)

    def eliminar():
        lblag.destroy()
        p1.destroy()
        p2.destroy()
        p3.destroy()
        en1.destroy()
        en2.destroy()
        en3.destroy()
        confirm.destroy()
        clear.destroy()
        desbloquear()

    clear = tkinter.Button(ventana,text="Cancelar",command=eliminar)
    clear.place(x=500,y=240)

def agregarDep():
    lblag = tkinter.Label(ventana, text= "Agregar")
    lblag.place(x=400,y=30)

    p1= tkinter.Label(ventana, text= "Ingresa ID: ")
    p1.place(x=200,y=80)

    en1 = tkinter.Entry(ventana)
    en1.place(x=400,y=80)

    p2 = tkinter.Label(ventana,text="Ingresa el nombre del departamento: ")
    p2.place(x=200,y=130)

    en2 = tkinter.Entry(ventana)
    en2.place(x=400,y=130)

    def confirmar():
        id = en1.get()
        nombre = en2.get()
        query = f"INSERT INTO departamento(id_departamento,nombre_d) VALUES ({id} ,'{nombre}');"
        mod(query)

    confirm = tkinter.Button(ventana,text="Confirmar",command= confirmar)
    confirm.place(x=400,y=180)

    def eliminar():
        lblag.destroy()
        p1.destroy()
        p2.destroy()
        en1.destroy()
        en2.destroy()
        confirm.destroy()
        clear.destroy()
        desbloquear()

    clear = tkinter.Button(ventana,text="Cancelar",command=eliminar)
    clear.place(x=500,y=180)

def agregarAl():
    lblag = tkinter.Label(ventana, text= "Agregar")
    lblag.place(x=400,y=30)

    p1= tkinter.Label(ventana, text= "Ingresa el producto (id): ")
    p1.place(x=200,y=80)

    en1 = tkinter.Entry(ventana)
    en1.place(x=400,y=80)

    p2 = tkinter.Label(ventana,text="Ingresa descripcion: ")
    p2.place(x=200,y=130)

    en2 = tkinter.Entry(ventana)
    en2.place(x=400,y=130)

    p3 = tkinter.Label(ventana,text="Ingresa cantidad: ")
    p3.place(x=200,y=180)

    en3 = tkinter.Entry(ventana)
    en3.place(x=400,y=180)

    p4 = tkinter.Label(ventana,text="Ingresa precio: ")
    p4.place(x=200,y=230)

    en4 = tkinter.Entry(ventana)
    en4.place(x=400,y=230)

    def confirmar():
        id = en1.get()
        des = en2.get()
        cant = en3.get()
        precio = en4.get()
        query = f"INSERT INTO almacen(codigo_producto,producto,cantidad,precio) VALUES ({id},'{des}',{cant},{precio});"
        mod(query)

    confirm = tkinter.Button(ventana,text="Confirmar",command= confirmar)
    confirm.place(x=400,y=280)

    def eliminar():
        lblag.destroy()
        p1.destroy()
        p2.destroy()
        p3.destroy()
        p4.destroy()
        en1.destroy()
        en2.destroy()
        en3.destroy()
        en4.destroy()
        confirm.destroy()
        clear.destroy()
        desbloquear()

    clear = tkinter.Button(ventana,text="Cancelar",command=eliminar)
    clear.place(x=500,y=280)

def bajas(tabla):
    lblag = tkinter.Label(ventana, text= "Bajas")
    lblag.place(x=400,y=30)
    lbl = tkinter.Label(ventana,text="Ingresa ID a elminiar: ")
    lbl.place(x=200,y=80)
    en1 = tkinter.Entry(ventana)
    en1.place(x=400,y=80)
    cursor = connection.cursor()
    cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{tabla}' ORDER BY ordinal_position;")
    columnas = [columna[0] for columna in cursor.fetchall()]

    cursor.close()
    primerCol = columnas[0]

    def ejecutar():
        id = en1.get()
        query = f"DELETE FROM {tabla} WHERE {primerCol} = {id};"
        mod(query)

    enviar = tkinter.Button(ventana,text="Enviar",command= ejecutar)
    enviar.place(x=200,y=150)

    def eliminar():
        lblag.destroy()
        lbl.destroy()
        en1.destroy()
        enviar.destroy()
        reset.destroy()
        desbloquear()

    reset = tkinter.Button(ventana,text="Cancelar",command=eliminar)
    reset.place(x=300,y=150)

def modificarCli():
    lblag = tkinter.Label(ventana, text= "Cambios")
    lblag.place(x=400,y=30)
    lbl = tkinter.Label(ventana,text="Ingresa ID a modificar: ")
    lbl.place(x=200,y=80)
    en1 = tkinter.Entry(ventana)
    en1.place(x=400,y=80)

    def ejecutar(id):
        lblag = tkinter.Label(ventana, text= "Agregar")
        lblag.place(x=400,y=30)

        p1= tkinter.Label(ventana, text= "Ingresa ID: ")
        p1.place(x=200,y=80)

        en1 = tkinter.Entry(ventana)
        en1.place(x=400,y=80)

        p2 = tkinter.Label(ventana,text="Ingresa el nombre del cliente: ")
        p2.place(x=200,y=130)

        en2 = tkinter.Entry(ventana)
        en2.place(x=400,y=130)

        p3 = tkinter.Label(ventana,text="Ingresa numero de telefono: ")
        p3.place(x=200,y=180)

        en3 = tkinter.Entry(ventana)
        en3.place(x=400,y=180)

        p4 = tkinter.Label(ventana,text="Ingresa correo E. : ")
        p4.place(x=200,y=230)

        en4 = tkinter.Entry(ventana)
        en4.place(x=400,y=230)

        def confirmar(idMod):
            id = en1.get()
            nombre = en2.get()
            telefono = en3.get()
            correo = en4.get()
            query = f"UPDATE cliente SET id_cliente = {id},nombre = '{nombre}',telefono = {telefono},correo = '{correo}' WHERE id_cliente = {idMod};"
            mod(query)

        confirm = tkinter.Button(ventana,text="Confirmar",command= confirmar)
        confirm.place(x=400,y=280)

        def eliminar():
            lblag.destroy()
            p1.destroy()
            p2.destroy()
            p3.destroy()
            p4.destroy()
            en1.destroy()
            en2.destroy()
            en3.destroy()
            en4.destroy()
            confirm.destroy()
            clear.destroy()
            desbloquear()

        clear = tkinter.Button(ventana,text="Cancelar",command=eliminar)
        clear.place(x=500,y=280)

    def id():
        id = en1.get()
        return id
    
    enviar = tkinter.Button(ventana,text="Enviar",command= lambda: (ejecutar(id()),eliminar()))
    enviar.place(x=200,y=150)

    def eliminar():
        lblag.destroy()
        lbl.destroy()
        en1.destroy()
        enviar.destroy()
        reset.destroy()
        desbloquear()

    reset = tkinter.Button(ventana,text="Cancelar",command=eliminar)
    reset.place(x=300,y=150)

def modificarPro():
    lblag = tkinter.Label(ventana, text= "Cambios")
    lblag.place(x=400,y=30)
    lbl = tkinter.Label(ventana,text="Ingresa ID a modificar: ")
    lbl.place(x=200,y=80)
    en1 = tkinter.Entry(ventana)
    en1.place(x=400,y=80)

    def ejecutar(id):
        lblag = tkinter.Label(ventana, text= "Agregar")
        lblag.place(x=400,y=30)

        p1= tkinter.Label(ventana, text= "Ingresa ID: ")
        p1.place(x=200,y=80)

        en1 = tkinter.Entry(ventana)
        en1.place(x=450,y=80)

        p2 = tkinter.Label(ventana,text="Ingresa descripcion: ")
        p2.place(x=200,y=130)

        en2 = tkinter.Entry(ventana)
        en2.place(x=450,y=130)

        p3 = tkinter.Label(ventana,text="Ingresa marca: ")
        p3.place(x=200,y=180)

        en3 = tkinter.Entry(ventana)
        en3.place(x=450,y=180)
        
        p4 = tkinter.Label(ventana,text="Ingresa fecha de recibido (dd/mm/aa): ")
        p4.place(x=200,y=230)

        en4 = tkinter.Entry(ventana)
        en4.place(x=450,y=230)
        
        p5 = tkinter.Label(ventana,text="Ingresa empleado que recibe: ")
        p5.place(x=200,y=280)

        en5 = tkinter.Entry(ventana)
        en5.place(x=450,y=280)
        
        p6 = tkinter.Label(ventana,text="Ingresa proveedor: ")
        p6.place(x=200,y=330)

        en6 = tkinter.Entry(ventana)
        en6.place(x=450,y=330)
        
        p7 = tkinter.Label(ventana,text="Ingresa precio: ")
        p7.place(x=200,y=380)

        en7 = tkinter.Entry(ventana)
        en7.place(x=450,y=380)

        def confirmar(idMod):
            id = en1.get()
            des = en2.get()
            marca = en3.get()
            fecha = en4.get()
            emp = en5.get()
            prov = en6.get()
            precio = en7.get()
            query = f"UPDATE producto SET id_producto = {id},descripcion = '{des}',marca = '{marca}',fecha_recibido = '{fecha}',recibe_empleado = {emp},proveedor = {prov},precio = {precio} WHERE id_producto = {idMod};"
            mod(query)

        confirm = tkinter.Button(ventana,text="Confirmar",command= confirmar)
        confirm.place(x=400,y=430)

        def eliminar():
            lblag.destroy()
            p1.destroy()
            p2.destroy()
            p3.destroy()
            p4.destroy()
            p5.destroy()
            p6.destroy()
            p7.destroy()
            en1.destroy()
            en2.destroy()
            en3.destroy()
            en4.destroy()
            en5.destroy()
            en6.destroy()
            en7.destroy()
            confirm.destroy()
            clear.destroy()
            desbloquear()

        clear = tkinter.Button(ventana,text="Cancelar",command=eliminar)
        clear.place(x=500,y=430)

    def id():
        id = en1.get()
        return id
    
    enviar = tkinter.Button(ventana,text="Enviar",command= lambda: (ejecutar(id()),eliminar()))
    enviar.place(x=200,y=150)

    def eliminar():
        lblag.destroy()
        lbl.destroy()
        en1.destroy()
        enviar.destroy()
        reset.destroy()
        desbloquear()

    reset = tkinter.Button(ventana,text="Cancelar",command=eliminar)
    reset.place(x=300,y=150)

def modificarEmp():
    lblag = tkinter.Label(ventana, text= "Cambios")
    lblag.place(x=400,y=30)
    lbl = tkinter.Label(ventana,text="Ingresa ID a modificar: ")
    lbl.place(x=200,y=80)
    en1 = tkinter.Entry(ventana)
    en1.place(x=400,y=80)

    def ejecutar(id):
        lblag = tkinter.Label(ventana, text= "Modificando...")
        lblag.place(x=400,y=30)

        p1= tkinter.Label(ventana, text= "Ingresa ID: ")
        p1.place(x=200,y=80)

        en1 = tkinter.Entry(ventana)
        en1.place(x=400,y=80)

        p2 = tkinter.Label(ventana,text="Ingresa el nombre del empleado: ")
        p2.place(x=200,y=130)

        en2 = tkinter.Entry(ventana)
        en2.place(x=400,y=130)

        p3 = tkinter.Label(ventana,text="Ingresa numero de departamento: ")
        p3.place(x=200,y=180)

        en3 = tkinter.Entry(ventana)
        en3.place(x=400,y=180)

        def confirmar(idMod):
            nID = en1.get()
            nNombre = en2.get()
            nDep = en3.get()
            query = f"UPDATE empleado SET id_empleado = {nID},nombre_e = '{nNombre}',departamento = {nDep} WHERE id_empleado = {idMod};"
            mod(query)

        confirm = tkinter.Button(ventana,text="Confirmar",command= lambda: confirmar(id))
        confirm.place(x=400,y=240)

        def eliminar():
            lblag.destroy()
            p1.destroy()
            p2.destroy()
            p3.destroy()
            en1.destroy()
            en2.destroy()
            en3.destroy()
            confirm.destroy()
            clear.destroy()
            desbloquear()

        clear = tkinter.Button(ventana,text="Cancelar",command=eliminar)
        clear.place(x=500,y=240)

    def id():
        id = en1.get()
        return id
    
    enviar = tkinter.Button(ventana,text="Enviar",command= lambda: (ejecutar(id()),eliminar()))
    enviar.place(x=200,y=150)

    def eliminar():
        lblag.destroy()
        lbl.destroy()
        en1.destroy()
        enviar.destroy()
        reset.destroy()
        desbloquear()

    reset = tkinter.Button(ventana,text="Cancelar",command=eliminar)
    reset.place(x=300,y=150)

def modificarP():
    lblag = tkinter.Label(ventana, text= "Cambios")
    lblag.place(x=400,y=30)
    lbl = tkinter.Label(ventana,text="Ingresa ID a modificar: ")
    lbl.place(x=200,y=80)
    en1 = tkinter.Entry(ventana)
    en1.place(x=400,y=80)

    def ejecutar(id):
        lblag = tkinter.Label(ventana, text= "Agregar")
        lblag.place(x=400,y=30)

        p1= tkinter.Label(ventana, text= "Ingresa ID: ")
        p1.place(x=200,y=80)

        en1 = tkinter.Entry(ventana)
        en1.place(x=450,y=80)

        p2 = tkinter.Label(ventana,text="Ingresa el ID del cliente: ")
        p2.place(x=200,y=130)

        en2 = tkinter.Entry(ventana)
        en2.place(x=450,y=130)

        p3 = tkinter.Label(ventana,text="Ingresa fecha de pedido (dd/mm/aa): ")
        p3.place(x=200,y=180)

        en3 = tkinter.Entry(ventana)
        en3.place(x=450,y=180)

        p4 = tkinter.Label(ventana,text="Ingresa nombre del cliente: ")
        p4.place(x=200,y=230)

        en4 = tkinter.Entry(ventana)
        en4.place(x=450,y=230)

        p5 = tkinter.Label(ventana,text="Ingresa correo del cliente: ")
        p5.place(x=200,y=280)

        en5 = tkinter.Entry(ventana)
        en5.place(x=450,y=280)

        p6 = tkinter.Label(ventana,text="Ingresa datos de producto (id a comprar): ")
        p6.place(x=200,y=330)

        en6 = tkinter.Entry(ventana)
        en6.place(x=450,y=330)

        def confirmar(idMod):
            id = en1.get()
            cliente = en2.get()
            fecha = en3.get()
            nombre = en4.get()
            correo = en5.get()
            datosP = en6.get()
            query = f"UPDATE pedido SET id_pedido = {id},cliente= {cliente},fecha_pedido = '{fecha}',nombre_cliente = '{nombre}',correo_cliente = '{correo}',datos_producto = {datosP} WHERE id_pedido = {idMod};"
            mod(query)

        confirm = tkinter.Button(ventana,text="Confirmar",command= confirmar)
        confirm.place(x=400,y=400)

        def eliminar():
            lblag.destroy()
            p1.destroy()
            p2.destroy()
            p3.destroy()
            p4.destroy()
            p5.destroy()
            p6.destroy()
            en1.destroy()
            en2.destroy()
            en3.destroy()
            en4.destroy()
            en5.destroy()
            en6.destroy()
            confirm.destroy()
            clear.destroy()
            desbloquear()

        clear = tkinter.Button(ventana,text="Cancelar",command=eliminar)
        clear.place(x=500,y=400)
        
    def id():
        id = en1.get()
        return id
    
    enviar = tkinter.Button(ventana,text="Enviar",command= lambda: (ejecutar(id()),eliminar()))
    enviar.place(x=200,y=150)

    def eliminar():
        lblag.destroy()
        lbl.destroy()
        en1.destroy()
        enviar.destroy()
        reset.destroy()
        desbloquear()

    reset = tkinter.Button(ventana,text="Cancelar",command=eliminar)
    reset.place(x=300,y=150)

def modificarProv():
    lblag = tkinter.Label(ventana, text= "Cambios")
    lblag.place(x=400,y=30)
    lbl = tkinter.Label(ventana,text="Ingresa ID a modificar: ")
    lbl.place(x=200,y=80)
    en1 = tkinter.Entry(ventana)
    en1.place(x=400,y=80)

    def ejecutar(id):
        lblag = tkinter.Label(ventana, text= "Agregar")
        lblag.place(x=400,y=30)

        p1= tkinter.Label(ventana, text= "Ingresa ID: ")
        p1.place(x=200,y=80)

        en1 = tkinter.Entry(ventana)
        en1.place(x=400,y=80)

        p2 = tkinter.Label(ventana,text="Ingresa el nombre de la empresa: ")
        p2.place(x=200,y=130)

        en2 = tkinter.Entry(ventana)
        en2.place(x=400,y=130)

        p3 = tkinter.Label(ventana,text="Ingresa numero de telefono: ")
        p3.place(x=200,y=180)

        en3 = tkinter.Entry(ventana)
        en3.place(x=400,y=180)
        def confirmar(idMod):
            id = en1.get()
            nombre = en2.get()
            tel = en3.get()
            query = f"UPDATE proveedor SET id_proveedor = {id},nombre_e = '{nombre}',departamento = {tel} WHERE id_proveedor = {idMod};"
            mod(query)

        confirm = tkinter.Button(ventana,text="Confirmar",command= confirmar)
        confirm.place(x=400,y=240)

        def eliminar():
            lblag.destroy()
            p1.destroy()
            p2.destroy()
            p3.destroy()
            en1.destroy()
            en2.destroy()
            en3.destroy()
            confirm.destroy()
            clear.destroy()
            desbloquear()

        clear = tkinter.Button(ventana,text="Cancelar",command=eliminar)
        clear.place(x=500,y=240)

    def id():
        id = en1.get()
        return id
    
    enviar = tkinter.Button(ventana,text="Enviar",command= lambda: (ejecutar(id()),eliminar()))
    enviar.place(x=200,y=150)

    def eliminar():
        lblag.destroy()
        lbl.destroy()
        en1.destroy()
        enviar.destroy()
        reset.destroy()
        desbloquear()

    reset = tkinter.Button(ventana,text="Cancelar",command=eliminar)
    reset.place(x=300,y=150)
    
def modificarDep():
    lblag = tkinter.Label(ventana, text= "Cambios")
    lblag.place(x=400,y=30)
    lbl = tkinter.Label(ventana,text="Ingresa ID a modificar: ")
    lbl.place(x=200,y=80)
    en1 = tkinter.Entry(ventana)
    en1.place(x=400,y=80)

    def ejecutar(id):
        lblag = tkinter.Label(ventana, text= "Agregar")
        lblag.place(x=400,y=30)

        p1= tkinter.Label(ventana, text= "Ingresa ID: ")
        p1.place(x=200,y=80)

        en1 = tkinter.Entry(ventana)
        en1.place(x=400,y=80)

        p2 = tkinter.Label(ventana,text="Ingresa el nombre del departamento: ")
        p2.place(x=200,y=130)

        en2 = tkinter.Entry(ventana)
        en2.place(x=400,y=130)

        def confirmar(idMod):
            nID = en1.get()
            nNombre = en2.get()
            query = f"UPDATE departamento SET id_departamento = {nID},nombre_d = '{nNombre}' WHERE id_departamento = {idMod};"
            mod(query)

        confirm = tkinter.Button(ventana,text="Confirmar",command= lambda: confirmar(id))
        confirm.place(x=400,y=180)

        def eliminar():
            lblag.destroy()
            p1.destroy()
            p2.destroy()
            en1.destroy()
            en2.destroy()
            confirm.destroy()
            clear.destroy()
            desbloquear()

        clear = tkinter.Button(ventana,text="Cancelar",command=eliminar)
        clear.place(x=500,y=180)

    def id():
        id = en1.get()
        return id
    
    enviar = tkinter.Button(ventana,text="Enviar",command= lambda: (ejecutar(id()),eliminar()))
    enviar.place(x=200,y=150)

    def eliminar():
        lblag.destroy()
        lbl.destroy()
        en1.destroy()
        enviar.destroy()
        reset.destroy()
        desbloquear()

    reset = tkinter.Button(ventana,text="Cancelar",command=eliminar)
    reset.place(x=300,y=150)

def modificarAl():
    lblag = tkinter.Label(ventana, text= "Cambios")
    lblag.place(x=400,y=30)
    lbl = tkinter.Label(ventana,text="Ingresa ID a modificar: ")
    lbl.place(x=200,y=80)
    en1 = tkinter.Entry(ventana)
    en1.place(x=400,y=80)

    def ejecutar(id):
        lblag = tkinter.Label(ventana, text= "Agregar")
        lblag.place(x=400,y=30)

        p1= tkinter.Label(ventana, text= "Ingresa el producto (id): ")
        p1.place(x=200,y=80)

        en1 = tkinter.Entry(ventana)
        en1.place(x=400,y=80)

        p2 = tkinter.Label(ventana,text="Ingresa descripcion: ")
        p2.place(x=200,y=130)

        en2 = tkinter.Entry(ventana)
        en2.place(x=400,y=130)

        p3 = tkinter.Label(ventana,text="Ingresa cantidad: ")
        p3.place(x=200,y=180)

        en3 = tkinter.Entry(ventana)
        en3.place(x=400,y=180)

        p4 = tkinter.Label(ventana,text="Ingresa precio: ")
        p4.place(x=200,y=230)

        en4 = tkinter.Entry(ventana)
        en4.place(x=400,y=230)

        def confirmar(idMod):
            id = en1.get()
            des = en2.get()
            cant = en3.get()
            precio = en4.get()
            query = f"UPDATE almacen SET codigo_producto = {id},producto = '{des}',cantidad = {cant},precio = {precio} WHERE codigo_producto = {idMod};"
            mod(query)

        confirm = tkinter.Button(ventana,text="Confirmar",command= confirmar)
        confirm.place(x=400,y=280)

        def eliminar():
            lblag.destroy()
            p1.destroy()
            p2.destroy()
            p3.destroy()
            p4.destroy()
            en1.destroy()
            en2.destroy()
            en3.destroy()
            en4.destroy()
            confirm.destroy()
            clear.destroy()
            desbloquear()

        clear = tkinter.Button(ventana,text="Cancelar",command=eliminar)
        clear.place(x=500,y=280)

    def id():
        id = en1.get()
        return id

    enviar = tkinter.Button(ventana,text="Enviar",command= lambda: (ejecutar(id()),eliminar()))
    enviar.place(x=200,y=150)

    def eliminar():
        lblag.destroy()
        lbl.destroy()
        en1.destroy()
        enviar.destroy()
        reset.destroy()
        desbloquear()

    reset = tkinter.Button(ventana,text="Cancelar",command=eliminar)
    reset.place(x=300,y=150)

def mostrar(tabla):
    titulo = tkinter.Label(ventana,text="Tabla: " + tabla)
    titulo.place(x=700,y=10)
    cont = 0
    tree =ttk.Treeview(ventana)
    cursor = connection.cursor()
    cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{tabla}' ORDER BY ordinal_position;")
    columnas = [columna[0] for columna in cursor.fetchall()]

    cursor.close()
    tree["columns"] = tuple(columnas)

    for columna in tree["columns"]:
        tree.column("#0",anchor=tkinter.CENTER, width=len("N.Registro")*5)
        tree.column(columna,anchor= tkinter.CENTER, width=len(columna)*12)
        tree.heading("#0",text="N.Registro",anchor=tkinter.CENTER)
        tree.heading(columna, text=columna, anchor=tkinter.CENTER)

    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {tabla};")
    datos = cursor.fetchall()

    for fila in datos:
        cont = cont + 1
        tree.insert("","end",text=str(cont),values=fila)
        
    cursor.close()

    tree.place(x=250,y=50,width=1050,height=600)
    def limpiar():
        tree.destroy()
        reset.destroy()
        titulo.destroy()
        desbloquear()
    reset = tkinter.Button(ventana,text="Cerrar",command=limpiar)
    reset.place(x=150,y=300)

def submenu(op):
    def cliente(op):
        diccionario = {
            1:agregarCli,
            3:modificarCli
        }
        if op == 2:
            bajas("cliente")
        elif op == 4:
            mostrar("cliente")
        elif op == 5:
            vaciar("cliente")
        else:  
         diccionario[op]()

    def pedido(op):
        diccionario = {
            1:agregarP,
            3:modificarP
        }
        if op == 2:
            bajas("pedido")
        elif op == 4:
            mostrar("pedido")
        elif op == 5:
            vaciar("pedido")
        else:
         diccionario[op]()

    def producto(op):
        diccionario = {
            1:agregarPro,
            3:modificarPro
        }
        if op == 2:
            bajas("producto")
        elif op == 4:
            mostrar("producto")
        elif op == 5:
            vaciar("producto")
        else:
         diccionario[op]()

    def proveedor(op):
        diccionario = {
            1:agregarProv,
            3:modificarProv
        }
        if op == 2:
            bajas("proveedor")
        elif op == 4:
            mostrar("proveedor")
        elif op == 5:
            vaciar("proveedor")
        else:
         diccionario[op]()

    def emp(op):
        diccionario = {
            1:agregarEmp,
            3:modificarEmp
        }
        if op == 2:
            bajas("empleado")
        elif op == 4:
            mostrar("empleado")
        elif op == 5:
            vaciar("empleado")
        else:
         diccionario[op]()

    def dep(op):
        diccionario = {
            1:agregarDep,
            3:modificarDep
        }
        if op == 2:
            bajas("departamento")
        elif op == 4:
            mostrar("departamento")
        elif op == 5:
            vaciar("departamento")
        else:
         diccionario[op]()
        
    def almacen(op):
        diccionario = {
            1:agregarAl,
            3:modificarAl
        }
        if op == 2:
            bajas("almacen")
        elif op == 4:
            mostrar("almacen")
        elif op == 5:
            vaciar("almacen")
        else:
         diccionario[op]()

    botones = tkinter.Frame(ventana,bg="cyan")
    botones.place(x=110,y=0,width=100,height=1000)
    opc = tkinter.Label(botones,text="Elige una\ntabla:",bg="cyan")
    opc.place(x=5,y=10)
    b1 = tkinter.Button(botones,text="cliente",width=11,command=lambda:(cliente(op),limpiar(),bloquear()))
    b1.place(x=8,y=50)
    b2 = tkinter.Button(botones,text="pedido",width=11,command=lambda:(pedido(op),limpiar(),bloquear()))
    b2.place(x=8,y=80)
    b3 = tkinter.Button(botones,text="producto",width=11,command=lambda:(producto(op),limpiar(),bloquear()))
    b3.place(x=8,y=110)
    b4 = tkinter.Button(botones,text="proveedor",width=11,command=lambda:(proveedor(op),limpiar(),bloquear()))
    b4.place(x=8,y=140)
    b5 = tkinter.Button(botones,text="empleado",width=11,command=lambda:(emp(op),limpiar(),bloquear()))
    b5.place(x=8,y=170)
    b6 = tkinter.Button(botones,text="departamento",width=11,command=lambda:(dep(op),limpiar(),bloquear()))
    b6.place(x=8,y=200)
    b7 = tkinter.Button(botones,text="almacen",width=11,command=lambda:(almacen(op),limpiar(),bloquear()))
    b7.place(x=8,y=230)
    def limpiar():
        botones.destroy()
        desbloquear()
    cerrar = tkinter.Button(botones,text="Regresar",width=11,command= lambda: (limpiar(),desbloquear()))
    cerrar.place(x=8,y=400)

def usuario():
    bloquear()
    vCuenta = tkinter.Tk()
    vCuenta.geometry("500x300")
    vCuenta.iconbitmap("majora.ico")
    vCuenta.title("SGPTCC")
    #vCuenta.configure(bg="cyan")

    bienvenida = tkinter.Label(vCuenta,text="Bienvenido al sistema de gestion\npara tienda de componentes de computo")
    bienvenida.place(x=100,y=0)

    lblUser = tkinter.Label(vCuenta,text="Usuario: postgres")
    lblUser.place(x=100,y=40)

    contra = tkinter.Label(vCuenta,text="Ingresa contrasena: ")
    contra.place(x=100,y=70)

    entPass = tkinter.Entry(vCuenta)
    entPass.place(x=250,y=70)

    def cancelar(val):
        if val == 1:
            vCuenta.destroy()
            desbloquear()
        else:
            vCuenta.destroy()
            salir()
        
    def capContra():
        def eliAlerta():
            alerta.destroy()

        con = entPass.get()
        if con == 'mastered':
            cancelar(1)
        else:
            alerta = tkinter.Label(vCuenta,text="Contrasena incorrecta")
            alerta.place(x=100,y=180)
            vCuenta.after(2000,eliAlerta)

    atras = tkinter.Button(vCuenta,text="Salir",command= lambda: cancelar(2))
    atras.place(x=300,y=130)

    entrar = tkinter.Button(vCuenta,text="Ingresar",command=capContra)
    entrar.place(x=200,y=130)

    vCuenta.protocol("WM_DELETE_WINDOW",lambda: cancelar(2))

    def mantener(vCuenta,ventana):
        vCuenta.lift()
        vCuenta.after(1,lambda: mantener(vCuenta,ventana))
    
    mantener(vCuenta,ventana)
    vCuenta.overrideredirect(True)

def respaldo():
    lbl = tkinter.Label(ventana,text="Respaldo")
    lbl.place(x=200,y=30)
    question = tkinter.Label(ventana,text="Esta seguro de realizar el respaldo?")
    question.place(x=200,y=80)

    def regresar():
        lbl.destroy()
        question.destroy()
        b1.destroy()
        b2.destroy()
        desbloquear()

    def ejecutar():
        nomArchivo = "SGPTCC.sql"
        contrasena = 'mastered'
        archivo = Path(nomArchivo)

        def regresar1():
            advert.destroy()
            ad1.destroy()
            ad2.destroy()
            desbloquear()
        
        def con(opc):
            comando = "pg_dump -U postgres -W -h localhost -d SGPTCC > SGPTCC.sql"
            #contra = getpass.getpass('mastered')

            def elim():
                conf.destroy()

            if opc == 1:
                os.remove(archivo)
                try:
                    subprocess.run(f'set PGPASSWORD={contrasena} && {comando}',shell=True)
                    #subprocess.run(comando,shell=True)
                    conf = tkinter.Label(ventana,text="Archivo creado correctamente...")
                    conf.place(x=400,y=400)
                except:
                    conf = tkinter.Label(ventana,text="El archivo no ha sido creado...")
                    conf.place(x=400,y=400)
            elif opc == 2:
                try:
                    subprocess.run(f'set PGPASSWORD={contrasena} && {comando}',shell=True)
                    #subprocess.run(comando,shell=True)
                    conf = tkinter.Label(ventana,text="Archivo creado correctamente...")
                    conf.place(x=400,y=400)
                except:
                    conf = tkinter.Label(ventana,text="El archivo no ha sido creado...")
                    conf.place(x=400,y=400)

            ventana.after(3000,elim)

        if archivo.is_file():
            advert = tkinter.Label(ventana,text="El archivo ya esta creado, quiere reemplazarlo?")
            advert.place(x=200,y=180)
            ad1 = tkinter.Button(ventana,text="Si")
            ad1.place(x=200,y=250)
            ad2 = tkinter.Button(ventana,text="No",command= lambda: (regresar(),regresar1()))
            ad2.place(x=400,y=250)

            con(1)
        else:
            con(2)
            

    b1 = tkinter.Button(ventana,text="Si",command= ejecutar)
    b1.place(x=200,y=130)
    b2 = tkinter.Button(ventana,text="Cancelar",command= regresar)
    b2.place(x=400,y=130)
    
def restaurar():
    lbl = tkinter.Label(ventana,text="Restauracion")
    lbl.place(x=400,y=30)
    lbl1 = tkinter.Label(ventana,text="Estas seguro de restaurar los datos? (Todas las tablas deben estar vacias): ")
    lbl1.place(x=400,y=60)

    def confirmar():

        def elimL1():
            l1.destroy()
            
        try:
            os.system('psql -h localhost -p 5432 -U postgres -f SGPTCC.sql SGPTCC')
            l1 = tkinter.Label(ventana,text="Se ha restaurado con exito...")
            l1.place(x=400,y=600)
            ventana.after(3000,elimL1)
        except:
            l1 = tkinter.Label(ventana,text="No existe el archivo o las tablas aun contienen datos...")
            l1.place(x=400,y=600)
            ventana.after(3000,elimL1)
    
    def regresar():
        lbl.destroy()
        lbl1.destroy()
        b1.destroy()
        b2.destroy()
        desbloquear()
    b1 = tkinter.Button(ventana,text="Si",command= confirmar)
    b1.place(x=400,y=90)
    b2 = tkinter.Button(ventana,text="Cancelar",command= regresar)
    b2.place(x=500,y=90)

def vaciar(tabla):
    lbl = tkinter.Label(ventana,text="Vaciar tabla")
    lbl.place(x=400,y=30)
    lbl1 = tkinter.Label(ventana,text="Estas seguro de borrar todos los datos de la tabla : " + tabla)
    lbl1.place(x=400,y=60)

    def regresar():
        lbl.destroy()
        lbl1.destroy()
        b1.destroy()
        b2.destroy()
        desbloquear()

    def confirmar(tabla):
        query = f"DELETE FROM {tabla};"
        mod(query)

    b1 = tkinter.Button(ventana,text="Si",command= lambda: confirmar(tabla))
    b1.place(x=400,y=90)
    b2 = tkinter.Button(ventana,text="Cancelar",command= regresar)
    b2.place(x=500,y=90)
   
def vaciarT():
    lbl = tkinter.Label(ventana,text="Vaciar todo")
    lbl.place(x=400,y=30)
    lbl1 = tkinter.Label(ventana,text="Estas seguro de borrar todos los datos de las tablas??? " )
    lbl1.place(x=400,y=60)

    def confirmar():
        def elimL1():
            l1.destroy()
        
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM almacen")
            cursor.execute("DELETE FROM pedido")
            cursor.execute("DELETE FROM producto")
            cursor.execute("DELETE FROM empleado")
            cursor.execute("DELETE FROM departamento")
            cursor.execute("DELETE FROM proveedor")
            cursor.execute("DELETE FROM cliente")
            connection.commit()
            l1 = tkinter.Label(ventana,text="Se ha vaciado con exito...")
            l1.place(x=400,y=600)
            ventana.after(3000,elimL1)
        except:
            l1 = tkinter.Label(ventana,text="Ha ocurrido un error")
            l1.place(x=400,y=600)
            ventana.after(3000,elimL1)
        cursor.close()

    def regresar():
        lbl.destroy()
        lbl1.destroy()
        b1.destroy()
        b2.destroy()
        desbloquear()

    b1 = tkinter.Button(ventana,text="Si",command= confirmar)
    b1.place(x=400,y=90)
    b2 = tkinter.Button(ventana,text="Cancelar",command= regresar)
    b2.place(x=500,y=90)

ventana = tkinter.Tk()
ventana.title("SGPTCC")
ventana.geometry("1366x768")
ventana.iconbitmap("majora.ico")
color = tkinter.Label(ventana,bg="skyblue",height=100,width=15)
color.place(x=0,y=0)

def salir():
    ventana.destroy()

def bloquear():
    btn1.configure(state="disable")
    btn2.configure(state="disable")
    btn3.configure(state="disable")
    btn4.configure(state="disable")
    #btn5.configure(state="disable")
    #btn6.configure(state="disable")
    btn7.configure(state="disable")
    btn8.configure(state="disable")

def desbloquear():
    btn1.configure(state="normal")
    btn2.configure(state="normal")
    btn3.configure(state="normal")
    btn4.configure(state="normal")
    #btn5.configure(state="normal")
    #btn6.configure(state="normal")
    btn7.configure(state="normal")
    btn8.configure(state="normal")

lbl = tkinter.Label(ventana,text="SGPTCC",bg="skyblue")
lbl.place(x=10,y=10)
btn1 = tkinter.Button(ventana,text="Altas",command= lambda: (submenu(1),bloquear()),width=10)
btn1.place(x=10,y=60)
btn2 = tkinter.Button(ventana,text="Bajas",width=10,command= lambda: (submenu(2),bloquear()))
btn2.place(x=10,y=90)
btn3 = tkinter.Button(ventana,text="Cambios",width=10,command= lambda: (submenu(3),bloquear()))
btn3.place(x=10,y=120)
btn4 = tkinter.Button(ventana,text="Despliegue \nde \nregistros",width=10,command= lambda: (submenu(4),bloquear()))
btn4.place(x=10,y=150)
#btn5 = tkinter.Button(ventana,text="Respaldar",width=10,command= lambda: (respaldo(),bloquear()))
#btn5.place(x=10,y=210)
#btn6 = tkinter.Button(ventana,text="Restaurar",width=10,command= lambda: (restaurar(),bloquear()))
#btn6.place(x=10,y=240)
btn7 = tkinter.Button(ventana,text="Vaciar tabla",width=10,command= lambda: (submenu(5),bloquear()))
btn7.place(x=10,y=270)
btn8 = tkinter.Button(ventana,text="Vaciar todo",width=10,command= lambda: (vaciarT(),bloquear()))
btn8.place(x=10,y=300)
btn9 = tkinter.Button(ventana,text="Salir",width=10,command= salir)
btn9.place(x=10,y=600)

usuario()

ventana.mainloop()