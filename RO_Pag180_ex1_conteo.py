#RO_Pag180_ex1_conteo.py
'''1. Escriba una función conteo(n) que entregue la cantidad de divisores enteros positivos
que tiene un número entero dado n. Escriba un programa de prueba que use la función
escrita para encontrar cual número entre 1 y 100 tiene más divisores enteros.
'''
def conteo(n):
    count= 0
    for i in range(1,n+1):   
        if n%i==0:
            count +=1
    return count



#Programa principal
t=0#comptador
for n in range(1,101):
    if conteo(n)>t:
        t=n

print(t)