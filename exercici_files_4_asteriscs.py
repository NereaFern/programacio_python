# exercici_files_4.py
fila=int(input("Files:"))
for i in range(fila):
    for columna in range(i+1):
        print(" ",end="")
    for t in range(fila-i):
        print("*",end="")
    print("")