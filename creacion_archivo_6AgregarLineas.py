archivo = open('datos.txt', 'a')
archivo.write('Linea Nueva 1\n')
archivo.write('Linea nueva 2\n')
archivo.close()

archivo = open('datos.txt', 'r')
contenido = archivo.read()
print(contenido)
archivo.close()
