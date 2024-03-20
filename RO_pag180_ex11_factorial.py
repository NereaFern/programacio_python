#RO_Pag_180_ex_11_factorial.py
'''11. Escriba una función fact(n) que reciba un numero entero n y devuelva su factorial.
Escriba un programa de prueba que genere un número aleatorio entero k entre 1 y 10. Use
la función y muestre la suma de los factoriales de los primeros k números naturales
'''
from random import randint
def fact(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    return factorial
'''
Programa de prova
k=randint(1,10)
print(k,fact(k))'''
#Programa principal
k=int(input("Escrigui l'últim numero: "))
suma=0
for i in range(1,k+1):
    suma+=fact(i)
print(f"La suma dels factorials dels {k} nombres és {suma}")