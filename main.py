from data_productos import Formato_inventario
from data_productos import inventario_general
from exportar_inventario import *
from factura import *


inventario:Formato_inventario=[]
def cargar_data():
    for data in inventario_general:
        inventario.append(Formato_inventario(data["codigo"],
                                            data["modelo"],
                                            data["cantidad"],
                                            data["precio_u"],
                                            data["costo_p"]))

def registrar_producto():
    codigo:str= input("Código: ")
    modelo:str= input("Modelo: ")
    cantidad:float= input("Cantidad: ")
    precio_u:float= input("Precio unitario: S/.")
    costo_p:float= input("Costo al Público: S/.")
    formato:Formato_inventario = Formato_inventario(codigo,modelo,cantidad,precio_u,costo_p)
    formato_2=[{"codigo":codigo,
                "modelo":modelo,
                "cantidad":cantidad,
                "precio_u": precio_u ,
                "costo_p": costo_p }]   
    inventario_general.extend(formato_2)  # el método extend permite agregar una lista a un diccionario.
    inventario.append(formato)            # le método append permite agregar un elemente al final de una lista.
    return True

def ver_inventario():
    for formato in inventario:
        print(formato.estructura_inventario())



def opcion_inventario():
    programa:bool=True
    while programa:
        print(" 1: Ver el inventario ")
        print(" 2: Registrar un nuevo producto ")
        print(" 3: Menú anterior ")
        opciones:str=str(input("Ingrese una opción: "))
        match opciones:
                case "1":
                    print("----------------------------------------------------------------------------------------------------------------------------")
                    ver_inventario()
                    exportar_inventario()
                    print("----------------------------------------------------------------------------------------------------------------------------")
                case "2":
                    registrar_producto()
                case "3":
                    main()




lista_factura=[]
def facturar_producto():
    codigo:str = input("Ingrese el codigo del producto: ")
    for elemento in inventario:
        if elemento.codigo == codigo:
            cuantos:int = int (input("Cantidad: "))
            agregar:list=(elemento.cantidad, elemento.codigo, elemento.modelo, elemento.costo_p, elemento.costo_p*0.18, elemento.costo_p*cuantos)
            lista_factura.append(agregar)
            
            for tupla in lista_factura:
                nueva_tupla = list(tupla)
                nueva_tupla[0] = cuantos 
                lista_factura_2.append(tuple(nueva_tupla))
            
    for elemento in inventario_general:
        if elemento['codigo'] == codigo:
            # Restar uno a la cantidad del producto
            elemento['cantidad'] = elemento['cantidad'] - cuantos
            return True

def opcion_venta():
    nombre:str=str(input("Nombre: "))
    dni:str=str(input("DNI: "))
    lista_datos.append((nombre, dni))
    programa:bool=True
    while programa:
        print(" 1: Agregar productos ")
        print(" 2: Guardar carrito ")
        print(" 3: Menú anterior ")
        opciones:str=str(input("Ingrese una opción: "))
        match opciones:
                case "1":
                    facturar_producto()
                case "2":
                    print("Nombre: ", nombre, "DNI: ", dni)
                    print(lista_factura)

                    for tupla in lista_factura:
                        subtotal= 0 + tupla[-1]
                    print("subtotal: ",subtotal)

                    igv_total=subtotal*0.18
                    print("IGV Total: ", igv_total)

                    porcentaje:int=int(input("Ingrese el %Descuento: "))
                    descuento=(subtotal/100)*porcentaje
                    print("Descuento: ",descuento)

                    total_importe = subtotal-descuento
                    print("Total a pagar: ",total_importe)

                    lista_total.append((subtotal, igv_total, porcentaje, descuento, total_importe))
                    print(lista_datos[0][0])
                    print(lista_factura_2)
                    print(lista_total)
                case "3":
                    main()

def menu_inicio():
    print("===========MENÚ============")
    print(" 1: Nueva venta")
    print(" 2: Inventario")
    print(" 3: Generar Factura")
    print(" exit")
    print("---------------------------")
    return True

def main():
    programa:bool=True
    while programa:
        menu_inicio()
        opciones_inicio:str=str(input("Ingrese una opción: "))
        match opciones_inicio:
            case "1":
                opcion_venta()
            case "2":
                opcion_inventario()
            case "3":
                generar_factura()
            case "exit":
                print(" CIERRE DEL DÍA ")
                programa= False
            case __:
                print("¡¡ Opción Inválida !!")

if __name__=='__main__':
    cargar_data()
    main()

