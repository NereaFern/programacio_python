#P15_algoritme
#Determinar el valor de les variables
a = int(input("Posa el primer nombre: "))
b = int(input("Posa el segon nombre: "))
c = int(input("Posa el tercer nombre: "))

if(a<b):
    t= a+b
elif(c <=b):
    t= a+b
else:
    t=b-c
print(f"{a},{t}")
print(f"{b},{t}")

'''Una altre manera de fer-ho:
if(a<b) or (c<=b):
    t= a+b
else:
    t= b-c
print(f"{a},{t}")
print(f"{b},{t}")'''