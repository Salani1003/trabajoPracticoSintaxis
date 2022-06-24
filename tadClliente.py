from datetime import date
#ESTRUCTURA INTERNA DE CLIENTE

""" Cliente{

    nombre=String
    apellido=String
    nro_cliente = Int
    tipo_servicio=String
    precio_servicio=Int
    fecha_alta=Date

} """

#CREA UN NUEVO CLIENTE
def crear_cliente():
    cliente=[0,"","","","",0,0]
    return cliente

def cargar_cliente(cliente,nombre,apellido,nro,tipo,precio,fecha=date.today(),descuento=0):
    cliente[0]=nombre #NOMBRE DEL CLIENTE
    cliente[1]=apellido #APELLIDO DEL CLIENTE
    cliente[2]=nro #NUMERO DEL CLIENTE
    cliente[3]=tipo #TIPO DEL SERVICIO QUE POSEE
    cliente[4]=precio #PRECIO DEL SERVICIO QUE POSEE
    cliente[5]=fecha #FECHA DE ALTA, SE SETEA LA FECHA EN LA QUE SE DA DE ALTA EL CLIENTE.
    cliente[6]=descuento #VARIABLE QUE ME PERMITE SABER SI EL CLIENTE TIENE EL DESCUENTO APLICADO O NO

#VER CAMPOS  DEL CLIENTE
def ver_nombre(cliente):
    return cliente[0]

def ver_apellido(cliente):
    return cliente[1]

def ver_numero_cliente(cliente):
    return cliente[2]

def ver_tipo(cliente):
    return cliente[3]

def ver_precio(cliente):
    return cliente[4]

def ver_fecha_alta(cliente):
    return cliente[5]

def ver_descuento(cliente):
    return cliente[6]


#MODIFICAR CAMPOS DEL CLIENTE.
def modificar_nombre(cliente,nombre):
    cliente[0]=nombre

def modificar_apellido(cliente,apellido):
    cliente[1]=apellido

def modificar_numero_cliente(cliente,nro):
    cliente[2]=nro

def modificar_tipo(cliente,tipo):
    cliente[3]=tipo

def modificar_precio(cliente,precio):
    cliente[4]=precio

def modificar_fecha(cliente,fecha):
    cliente[5]=fecha

def modificar_descuento(cliente,descuento):
    cliente[6]=descuento