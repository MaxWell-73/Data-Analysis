import PyPDF2

# Abre los archivos PDF a fusionar
pdf1 = open('D:/Fisica\Física Semestre 7/Cuantica 1/Notas MIT/1-MC.pdf','rb')
pdf2 = open('D:/Fisica/Física Semestre 7/Cuantica 1/Notas MIT/2-MC.pdf','rb')
pdf3 = open('D:/Fisica/Física Semestre 7/Cuantica 1/Notas MIT/3-MC.pdf','rb')
pdf4 = open('D:/Fisica/Física Semestre 7/Cuantica 1/Notas MIT/4-MC.pdf','rb')
pdf5 = open('D:/Fisica/Física Semestre 7/Cuantica 1/Notas MIT/5-MC.pdf','rb')
pdf6 = open('D:/Fisica/Física Semestre 7/Cuantica 1/Notas MIT/6-MC.pdf','rb')
pdf7 = open('D:/Fisica/Física Semestre 7/Cuantica 1/Notas MIT/7-MC.pdf','rb')
pdf8 = open('D:/Fisica/Física Semestre 7/Cuantica 1/Notas MIT/8-MC.pdf','rb')
pdf9 = open('D:/Fisica/Física Semestre 7/Cuantica 1/Notas MIT/9-MC.pdf','rb')
pdf10 = open('D:/Fisica/Física Semestre 7/Cuantica 1/Notas MIT/10-MC.pdf','rb')
pdf11 = open('D:/Fisica/Física Semestre 7/Cuantica 1/Notas MIT/11-MC.pdf','rb')
pdf12 = open('D:/Fisica/Física Semestre 7/Cuantica 1/Notas MIT/12-MC.pdf','rb')
pdf13 = open('D:/Fisica/Física Semestre 7/Cuantica 1/Notas MIT/13-MC.pdf','rb')
pdf14 = open('D:/Fisica/Física Semestre 7/Cuantica 1/Notas MIT/14-15-MC.pdf','rb')
pdf15 = open('D:/Fisica/Física Semestre 7/Cuantica 1/Notas MIT/16-MC.pdf','rb')
pdf16 = open('D:/Fisica/Física Semestre 7/Cuantica 1/Notas MIT/17-MC.pdf','rb')
pdf17 = open('D:/Fisica/Física Semestre 7/Cuantica 1/Notas MIT/18-MC.pdf','rb')
pdf18 = open('D:/Fisica/Física Semestre 7/Cuantica 1/Notas MIT/19-MC.pdf','rb')
pdf19 = open('D:/Fisica/Física Semestre 7/Cuantica 1/Notas MIT/20-21-MC.pdf','rb')
pdf20 = open('D:/Fisica/Física Semestre 7/Cuantica 1/Notas MIT/21-22-MC.pdf','rb')

# Crea un objeto de escritura PDF
writer = PyPDF2.PdfWriter()

def fusionar(pdf):
    # Agrega los archivos PDF a fusionar al objeto de escritura
    reader = PyPDF2.PdfReader(pdf)
    for pageNum in range(len(reader.pages)):
        page = reader.pages[pageNum]
        writer.add_page(page)
    # reader2 = PyPDF2.PdfReader(pdf2)
    # for pageNum in range(len(reader2.pages)):
    #     page = reader2.pages[pageNum]
    #     writer.add_page(page)
    
fusionar(pdf1)
fusionar(pdf2)
fusionar(pdf3)
fusionar(pdf4)
fusionar(pdf5)
fusionar(pdf6)
fusionar(pdf7)
fusionar(pdf8)
fusionar(pdf9)
fusionar(pdf10)
fusionar(pdf11)
fusionar(pdf12)
fusionar(pdf13)
fusionar(pdf14)
fusionar(pdf15)
fusionar(pdf16)
fusionar(pdf17)
fusionar(pdf18)
fusionar(pdf19)
fusionar(pdf20)

# Crea un nuevo archivo PDF fusionado
outputPdf = open('D:/Fisica/Física Semestre 7/Cuantica 1/Notas MIT/MecanicaCuanticaMIT.pdf', 'wb')
writer.write(outputPdf)

# Cierra los archivos PDF
pdf1.close()
pdf2.close()
outputPdf.close()
