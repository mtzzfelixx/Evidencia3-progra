archivotxt = open('datos.txt', 'r')
lineas = archivotxt.readlines()
print('El archivo tiene:', len(lineas), 'lineas')
print('El contenido del archivo:')
for linea in lineas:
    print(linea, end = "")
archivotxt.close()