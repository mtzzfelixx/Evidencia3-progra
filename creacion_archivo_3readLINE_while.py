archivotxt = open("datos.txt", "r")
linea = archivotxt.readline()
while linea != "":
    print(linea, end = "")
    linea = archivotxt.readline()
archivotxt.close()