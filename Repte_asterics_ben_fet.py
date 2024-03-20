#exercici_dels_asterics

fila=int(input("Escrigui el nombre de files: "))

for i in range(0,fila):
    for t in range(i+1):
        print("*",end="")
    print("")