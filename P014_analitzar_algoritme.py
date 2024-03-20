#P014_analitzar_algoritme.py

#Determinar el valor de les variables
a = int(input("Posa el primer nombre: "))
b = int(input("Posa el segon nombre: "))
c = int(input("Posa el tercer nombre: "))

if(a<b):
    if(b>c):
        print(a)

print(f"{b},{c}")

'''Un altre manera de fer-ho
if(a<b) and (b>c):
    print(a)
print(b,c)'''