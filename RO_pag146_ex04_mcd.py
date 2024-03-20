#R0_Pag_146_ex_4_mcd.py
'''4.- Dado dos números enteros a, b, determine su máximo común divisor m.
Ejemplo: a = 36, b = 45 entonces m = 9'''
a=int(input("Introdueix el primer nombre: "))
b=int(input("Introdueixi el segon nombre: "))
c=1
mcd=1
while c<a and c<b and a/c!=1 or b/c!=1: 
    if c==10 :
        c=1
    if a/c == a//c and b/c == b//c:
        a=a/c
        b=b/c
        mcd =c*mcd
    c+=1
    print(mcd)
print("El MCD és", mcd)