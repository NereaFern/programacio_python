#exercici_files_3.py
fila=int(input("Escrigui el nombre de files: "))
x=1
for i in range(fila,0,-1):
    for t in range(i):
        print(" ", end="")
    for h in range(x):
        print("*",end="")
    x+=1
    print("")
    