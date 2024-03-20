#exercici_files_2.py
fila=int(input("Files: "))
for i in range(fila,0,-1):
    for t in range(i):
        print("*", end="")
    print("")