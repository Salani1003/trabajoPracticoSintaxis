#ESTRUCTURA INTERNA DE LA LISTA DE CLIENTES

""" 
    LISTA DE CLIENTES 
 """
from datetime import date
from http import client
from tadClliente import*


def crear_lista_cliente():
    lista_cliente=[]
    return lista_cliente

def agregar_cliente(lista,cliente):
    lista.append(cliente)

def tamanio(lista):
    return len(lista)

def recuperar_cliente(lista,index):
    return lista[index]

def eliminar_cliente(lista,cliente):
    lista.remove(cliente)

def listar_todos_clientes(lista):
    if(tamanio(lista)!=0):
        for i in lista:
            print("------------------------")
            print("NUMERO DE CLIENTE: ",ver_numero_cliente(i))
            print("NOMBRE: ",ver_nombre(i))
            print("APELLIDO: ",ver_apellido(i))
            print("FECHA DE ALTA: ",ver_fecha_alta(i))
            print("TIPO DE SERVICIO: ",ver_tipo(i))
            print("PRECIO DEL SERVICIO: ",ver_precio(i))
            print("")
    else:
        print("LA LISTA ESTA VACIA") 

def eliminar_por_tipo(lista):
    if(tamanio(lista)!=0):
        tam=tamanio(lista)
        cantEli=0
        tipo=input("INGRESE EL TIPO DE SERVICIO: ")
        i=0

        while i < tam:
            client=recuperar_cliente(lista,i)
            if(ver_tipo(client)==tipo):
                eliminar_cliente(lista,client)
                tam -=1
                cantEli+=1
            else:
                i = i+1
        print("SE ELIMINARON",cantEli,"CLIENTES DE TIPO",tipo)  
        
    else:
        print("LA LISTA ESTA VACIA") 

def diferencia_de_meses(f1,f2):
    return (f1.year - f2.year) * 12 + f1.month - f2.month

def calcular_descuento(cliente):
    monto=ver_precio(cliente)-ver_precio(cliente)*0.10
    return monto

def descontar(lista):
    if(tamanio(lista)!=0):
        tam=tamanio(lista)
        cantDes=0
        i=0
        while i < tam:
            client=recuperar_cliente(lista,i)
            f_inicio=date.today()
            f_fin=ver_fecha_alta(client)
            if(diferencia_de_meses(f_inicio,f_fin)>=36 and ver_descuento(client)==0):
                modificar_precio(client,calcular_descuento(client))
                cantDes+=1
                modificar_descuento(client,1)
            i+=1
        print("CANTIDAD DE CLIENTES QUE SE LE APLICO EL DESCUENTO : ", cantDes)
    else:
        print("LA LISTA ESTA VACIA")

def listar_clientes_con_descuento_aplicado(lista):
    if(tamanio(lista)!=0):
        cantCl=0
        print("entro al if")
        for i in range(0,tamanio(lista)):
            client=recuperar_cliente(lista,i)
            if(ver_descuento(client)==1):
                print("------------------------")
                print("NUMERO DE CLIENTE: ",ver_numero_cliente(client))
                print("NOMBRE: ",ver_nombre(client))
                print("APELLIDO: ",ver_apellido(client))
                print("FECHA DE ALTA: ",ver_fecha_alta(client))
                print("TIPO DE SERVICIO: ",ver_tipo(client))
                print("PRECIO DEL SERVICIO: ",ver_precio(client))
                print("")
                cantCl+=1
        if(cantCl==0):
            print("NO HAY CLIENTES CON DESCUENTO APLICADO")
    else:
        print("LA LISTA ESTA VACIA")