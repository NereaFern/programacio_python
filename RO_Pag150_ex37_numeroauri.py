#RO_Pag150_ex37_numeroauri.py
'''Escriba un programa en Python que genere todas las parejas de números enteros a, b
con valores entre 1 y n. Pruebe que no existe alguna pareja de este conjunto de números
que satisfagan la ecuación del “número áureo”.'''
n=int(input("Número de numeros: "))
compt=0 #Comptador
for i in range(1,n+1):
    a=i#Primer numero
    for t in range(1,n+1):
        b=t #Segon numero
        if a/b== (a+b)/a:
            print(f"La parella {a,b} compleix la proporció aurea")
            break
        else:
            continue
if a/b != (a+b)/a:
    print(f"No hi ha cap parella de nombres que compleixi la proporció aurea")