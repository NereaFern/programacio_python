# exercici_files_5.py
fila=int(input("Nombre files: "))
espais=0
for i in range(fila,0,-2):
    for k in range(espais):
        print(" ",end="")
    espais+=1
    for t in range(i):
        print("*",end="")
    print("")

