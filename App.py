import os
from tadClliente import*
from tadListaCliente import*
from datetime import date

# INICIO DE LA SECCION DE FUNCIONES NECESARIAS PARA EL USO DEL SISTEMA.
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def crear_nuevo_cliente():
    
    print("OPCION ELEGIDA -->",opcion ,"\n")
    client=crear_cliente()
    nombre=input("\nINGRESE NOMBRE: ")
    apellido=input("\nINGRESE APELLIDO: ")
    nro=int(input("\nINGRESE NUMERO DE CLIENTE: "))
    tipo=input("\nINGRESE TIPO DE SERVICIO: ")
    precio=int(input("\nINGRESE PRECIO DEL SERVICIO: "))
    print("\n")

    cargar_cliente(client,nombre,apellido,nro,tipo,precio)
    agregar_cliente(lista,client)
    print("<===== CLIENTE AGREGADO =====>")

def modificar_cliente(lista):
    print("OPCION ELEGIDA -->",opcion ,"\n")

    if(tamanio(lista)!=0):

        rta="si"
        tam=tamanio(lista)
        numero=int(input("INGRESE EL NUMERO DEL CLIENTE: "))

        for i in range(0,tam):
            client=recuperar_cliente(lista,i)
            if(ver_numero_cliente(client)==numero):
                clearConsole()
                while rta=="si":
                
                    print(" MODIFICAR NOMBRE              (1) ")
                    print(" MODIFICAR APELLIDO            (2) ")
                    print(" MODIFICAR TIPO DE SERVICIO    (3) ")
                    print(" MODIFICAR PRECIO DEL SERVICIO (4) ")
                    dato=int(input("INGRESE OPCION -->  "))

                    if(dato==1):
                        nuevo_nombre=input("INGRESE NUEVO NOMBRE: ")
                        modificar_nombre(client,nuevo_nombre)
                        print("<===== NOMBRE MODIFICADO=====>")
                    elif(dato==2):
                        nuevo_apellido=input("INGRESE NUEVO APELLIDO: ")
                        modificar_apellido(client,nuevo_apellido)
                        print("<===== APELLIDO MODIFICADO=====>")
                    elif(dato==3):
                        nuevo_tipo=input("INGRESE NUEVO TIPO DE SERVICIO: ")
                        modificar_tipo(client,nuevo_tipo)
                        print("<===== TIPO DE SERVICIO MODIFICADO=====>")
                    elif(dato==4):
                        nuevo_precio=input("INGRESE NUEVO PRECIO PARA EL SERVICIO")
                        modificar_precio(client,nuevo_precio)
                        print("<===== PRECIO DE SERVICIO MODIFICADO=====>")
                    else:
                        print("OPCION INGRESADA NO ES VALIDA")

                    rta=input("¿DESEA SEGUIR MODIFICANDO ESTE CLIENTE?")
            else:
                clearConsole()
                print("NO EXISTE UN CLIENTE CON ESE NUMERO")
    else:
        print("LA LISTA ESTA VACIA")

    
def eliminar_cliente_por_numero(lista):
    print("OPCION ELEGIDA -->",opcion ,"\n")
    tam=tamanio(lista)
    if(tamanio(lista)!=0):
        numero=int(input("INGRESE EL NUMERO DEL CLIENTE: "))
        for i in range(0,tam):
            client=recuperar_cliente(lista,i)
            if(ver_numero_cliente(client)==numero):
                clearConsole()
                eliminar_cliente(lista,client)
                print("CLIENTE ELIMINADO CON EXITO")
            else:
                clearConsole()
                print("NO EXISTE UN CLIENTE CON ESE NUMERO")
    else:
        print("LA LISTA ESTA VACIA") 


def listar_clientes(lista):
    print("OPCION ELEGIDA -->",opcion ,"\n")
    listar_todos_clientes(lista)

def eliminar_cliente_por_tipo(lista):
    print("OPCION ELEGIDA -->",opcion ,"\n")
    eliminar_por_tipo(lista)
    
def realizar_descuento(lista):
    print("OPCION ELEGIDA -->",opcion ,"\n")
    descontar(lista)

def listar_clientes_con_descuento(lista):
    print("OPCION ELEGIDA -->",opcion ,"\n")
    listar_clientes_con_descuento_aplicado(lista)

print("<===== INICIO DE LA APLICACION =====>")
print("\n")
print(" MENU \n")


client=crear_cliente()
lista=crear_lista_cliente()

cliente1=crear_cliente()
fecha=date(2017, 12,25)
cargar_cliente(cliente1,"pablo","salani",15,"plus",1500,fecha)
agregar_cliente(lista,cliente1)

res='si'

while(res=='si'):
    
    
    print("  ----------->> MENU <<------------ \n")
    
    print(" 1) --> AGREGAR CLIENTE ")
    print(" 2) --> MODIFICAR CLIENTE ")
    print(" 3) --> ELIMINAR CLIENTE ")
    print(" 4) --> LISTADO DE CLIENTES ")
    print(" 5) --> ELIMINAR CLIENTES POR TIPO DE SERVICIO ")
    print(" 6) --> REALIZAR DESCUENTO ")
    print(" 7) --> LISTADO DE CLIENTES CON PROMOCION ")
    print("\n")
    print(" 0) --> SALIR DE LA APP ")
    print("\n")
    
    print("  ----------->> || <<------------ ")
    print("\n")

    opcion=int(input("INGRESE OPCION -->  "))
    print("\n")

    if(opcion==1): #AGREGO CLIENTE
        clearConsole()
        crear_nuevo_cliente()

    elif(opcion==2): #MODIFICO UN CLIENTE POR NRO DE CLIENTE
        clearConsole()
        modificar_cliente(lista)
    elif(opcion==3):
        clearConsole()
        eliminar_cliente_por_numero(lista)
    elif(opcion==4):
        clearConsole()
        listar_clientes(lista)
    elif(opcion==5):
        clearConsole()
        eliminar_cliente_por_tipo(lista)
    elif(opcion==6):
        clearConsole()
        realizar_descuento(lista)
    elif(opcion==7):
        clearConsole()
        listar_clientes_con_descuento(lista)

    elif(opcion==0): #TERMINA LA EJECUCION
        print("OPCION ELEGIDA -->",opcion ,"\n")
        print("Fin de la ejecucion... \n")
        res='no'
    else:
        print("LA OPCION ELEGIDA ES ERRONEA..... \n")


