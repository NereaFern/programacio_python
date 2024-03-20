# exercici_triangle_normal.py
fila=int(input("Nombre de files: "))
u=fila+1
for i in range(0,fila+4,2):
    if i==0:
        for q in range(u-1):
            print(" ",end="")
        print("*",end="")
    else:
        for q in range(u):
            print(" ",end="")
        for q in range(i):
            print("*",end="")
    u-=1
    print("")
    
    

