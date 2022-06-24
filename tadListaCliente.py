#ESTRUCTURA INTERNA DE LA LISTA DE CLIENTES

""" 
    LISTA DE CLIENTES : [cliente1,cliente2] 
"""


from datetime import date
from http import client
from tadClliente import*

#CREAR LA NUEVA LISTA VACIA
def crear_lista_cliente():
    lista_cliente=[]
    return lista_cliente

#AGREGA UN NUEVO CLIENTE A LA LISTA
def agregar_cliente(lista,cliente):
    lista.append(cliente)

#RETORNA EL TAMAÑO DE LA LISTA
def tamanio(lista):
    return len(lista)

#RECIBE UNA LISTA Y UN INDICE, DEVUELVE EL CLIENTE ALOJADO EN ESE INDICE 
def recuperar_cliente(lista,index):
    return lista[index]

#RECIBE UNA LISTA Y UN CLIENTE, ELIMINA ESE CLIENTE DE LA LISTA  
def eliminar_cliente(lista,cliente):
    lista.remove(cliente)

#RETORNA LA DIFERENCIA EN MESES ENTRE DOS FECHAS.
def diferencia_de_meses(f1,f2):
    return (f1.year - f2.year) * 12 + f1.month - f2.month

#RETORNA EL MONTON APLICANDOLE UN 10% DE DESCUENTO
def calcular_descuento(cliente):
    monto=ver_precio(cliente)-ver_precio(cliente)*0.10
    return monto

#SI EL CLIENTE TIENE MAS DE TRES AÑOS DE ANTIGUEDAD Y TODAVIA NO SE LE APLICARON DESCUENTOS, LOS APLICA.
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

#ME DEVUELVE LOS CLIENTES QUE TIENEN DESCUENTO APLICADOS. 
def listar_clientes_con_descuento_aplicado(lista):
    if(tamanio(lista)!=0):
        cantCl=0
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