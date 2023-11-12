archivotxt = open('datos.txt', 'r')
for linea in archivotxt:
    print(linea, end = "")
archivotxt.close()