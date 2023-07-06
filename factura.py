from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter,inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Table, TableStyle, Frame

import pandas as pd


lista_datos=[]
lista_total=[]
lista_factura_2 = []

def generar_factura():

    estilos = getSampleStyleSheet()
    estilo_1 = ParagraphStyle(name='Normal', textColor=colors.black, fontSize=12, parent=estilos['Normal'])
    estilo_2 = ParagraphStyle(name='Normal', textColor=colors.black, fontSize=30, parent=estilos['Normal'])
    estilo_white = ParagraphStyle(name='Normal', textColor=colors.white, fontSize=12, parent=estilos['Normal'])

    texto = "TecnoMundo"

    para_2 = Paragraph("........", estilo_white)
    para_3 = Paragraph("........", estilo_white)
    para_4 = Paragraph(texto, estilo_2)

    para = Paragraph("GGGGGG", estilo_white)

    cliente:str=str(lista_datos[0][0])
    dni_cliente:str=str(lista_datos[0][1])
    nombre_fac = Paragraph("Cliente: "+ cliente, estilo_1)
    dni_fac = Paragraph("DNI: "+ dni_cliente, estilo_1)




    descripcion = pd.DataFrame(lista_factura_2, columns=['cantidad', 'Modelo', 'Descripcion', 'Precio', 'IGV', 'Monto'])

    descripcion['Precio'] = 'S/. ' + descripcion['Precio'].astype(str)
    descripcion['IGV'] = 'S/. ' + descripcion['IGV'].astype(str)
    descripcion['Monto'] = 'S/. ' + descripcion['Monto'].astype(str)

    data = [descripcion.columns.values.tolist()] + descripcion.values.tolist()
    documento = SimpleDocTemplate("factura.pdf", pagesize=letter)
    elementos=[]

        # Agregar estilo a la tabla (opcional)
        # La función setStyle toma como argumento un objeto TableStyle que define el estilo de la tabla.
        # (x,y)
    table = Table(data)
    table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (5, 0), '#d5dae6'), # establece el color de fondo de la primera fila, color hexadecimal.
            ('TEXTCOLOR', (0, 0), (5, 0), '#000000'), # establece el color del texto de la primera fila, color hexadecimal.
            ('ALIGN', (0, 0), (0, -1), 'CENTER'), # centra el contenido de todas las celdas.
            ('ALIGN', (0, 0), (5,0), 'CENTER'),
            ('ALIGN', (2, 0), (2, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (5, 0), 'Helvetica-Bold'), # establece la fuente de la primera fila.
            ('FONTSIZE', (0, 0), (5, 0), 14), # establece el tamaño de fuente de la primera fila en 14.
            ('BOTTOMPADDING', (0, 0), (5, 0), 12), #agrega un relleno inferior de 12 a la primera fila.
            ('BACKGROUND', (0, 1), (-1, -1), '#f7f7f9'), #  establece el color de fondo de todas las filas excepto la primera
            ('GRID', (0, 0), (-1, -1), 1, '#d5dae6'), # agrega una cuadrícula de ancho 1 y color a todas las celdas.
        ]))

    
    data_2 = [["SubTotal", "S/. " + str(lista_total[0][0])],
            ["IGV Total", "S/. " + str(lista_total[0][1])],
            ["% Descuento", str(lista_total[0][2]) + " %"],
            ["Descuento", "S/. " + str(lista_total[0][3])],
            ["Importe a pagar: ","S/. " + str(lista_total[0][4])]]

    table_2 = Table(data_2)
    table_2.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), "#E6E6E6"), # establece el color de fondo izquierda fila, color hexadecimal.
            ('TEXTCOLOR', (0, 0), (-1, -1), "#1e1e2d"), # establece el color del texto de la primera fila, color hexadecimal.
            ('ALIGN', (0, 0), (0,-1), 'RIGHT'), # DERECHA
            ('ALIGN', (-1, 0), (-1,-1), 'LEFT'), # izquierda
            ('ALIGN', (-1, 2), (-1, 2), 'CENTER'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'), # establece la fuente de la primera fila.
            ('FONTSIZE', (0, 0), (0, -1), 10), # establece el tamaño de fuente de la primera fila en 10.
            ('BOTTOMPADDING', (0, 0), (-1, 0), 5), #agrega un relleno inferior de 12 a la primera fila.
            ('BACKGROUND', (-1, 0), (-1, -1), "#f7f7f9"), #  establece el color de fondo de todas las filas excepto la primera
            ('GRID', (0, 0), (-1, -1), 1, '#d5dae6'),
            ('TOPPADDING', (0, 0), (1, 1),5),
            ('LEFTPADDING', (0, 0), (-1, -1),5)
        ]))

    elementos.append(nombre_fac)
    elementos.append(dni_fac)
    
    elementos.append(para_4)
    elementos.append(para_3)
    elementos.append(para_2)
    elementos.append(para)
    elementos.append(table)
    elementos.append(table_2)
    
    
    documento.build(elementos)

if __name__=='__main__':
    generar_factura()
