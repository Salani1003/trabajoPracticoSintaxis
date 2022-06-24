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
    cantEli=0
    if(tamanio(lista)!=0):
        numero=int(input("INGRESE EL NUMERO DEL CLIENTE: "))
        tam=tamanio(lista)
        i=0
        while i < tam:
            client=recuperar_cliente(lista,i)
            if(ver_numero_cliente(client)==numero):
                
                eliminar_cliente(lista,client)
                tam-=1
                cantEli+=1
            i+=1
        if(cantEli>0):
            print("CLIENTE NUMERO",numero,"ELIMINADO CON EXITO")
    else:
        print("LA LISTA ESTA VACIA") 


def listar_clientes(lista):
    print("OPCION ELEGIDA -->",opcion ,"\n")
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

def eliminar_cliente_por_tipo(lista):
    print("OPCION ELEGIDA -->",opcion ,"\n")
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

#DEFINIMOS UN CLIENTE DE PRUEBA Y LO CARGAMOS EN LA LISTA
#ASI TENEMOS ALGUN DATO CON FECHA VIEJA PARA MOSTRAR COMO SE HACE EL DESCUENTO.

cliente1=crear_cliente()
fecha=date(2017, 12,25)
cargar_cliente(cliente1,"pablo","salani",15,"plus",1500,fecha)
agregar_cliente(lista,cliente1)

#EL SISTEMA NO PERMITE LA MODIFICACION DE LA FECHA DE ALTA Y NUMERO DE CLIENTE. 
#ESTO SE DEBE A QUE CONSIDERAMOS QUE LA FECHA DE ALTA ES UNICA, Y SE DEBE TOMAR LA FECHA EN LA QUE EL CLIENTE FUE CREADO
#ADEMAS TOMAMOS EL NUMERO DEL CLIENTE COMO UN IDENTIFICADOR UNICO,(EN UNA BASE DE DATOS ES UN ID AUTOINCREMENTAL) POR LO QUE NO VEO CORRECTO CAMBIARLO UNA VEZ QUE ESTA SETEADO.

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
    elif(opcion==3): #ELIMINO EL CLIENTE QUE COINCIDA CON EL NUMERO DE CLIENTE INGRESADO
        clearConsole()
        eliminar_cliente_por_numero(lista)
    elif(opcion==4): #LISTO TODOS LOS CLIENTES
        clearConsole()
        listar_clientes(lista)
    elif(opcion==5): #ELIMINO LOS CLIENTES QUE COINCIDAN CON EL TIPO INGRESADO.
        clearConsole()
        eliminar_cliente_por_tipo(lista)
    elif(opcion==6): #REALIZO EL DESCUENTO A LOS CLIENTES QUE CORRESPONDE
        clearConsole()
        realizar_descuento(lista)
    elif(opcion==7): #LISTAR TODOS LOS CLIENTES QUE TIENEN APLICADOS DESCUENTOS. 
        clearConsole()
        listar_clientes_con_descuento(lista)

    elif(opcion==0): #TERMINA LA EJECUCION
        print("OPCION ELEGIDA -->",opcion ,"\n")
        print("Fin de la ejecucion... \n")
        res='no'
    else:
        print("LA OPCION ELEGIDA ES ERRONEA..... \n")


