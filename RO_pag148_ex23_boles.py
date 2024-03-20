#R0_Pag_148_ex_23_boles.py
'''23.- Escriba un programa para simular la extracción de n bolas de una caja que contiene m
bolas numeradas con los números naturales del 1 al m. Cada vez que se saca la bola se
muestra el número y se la devuelve a la caja, por lo tanto pueden salir bolas repetidas. '''
from random import choice
#Inicialitzem variables
m=int(input("Escrigui el nombre total de boles: "))
n=int(input("Escrigui les boles que s'han d'extreure: "))
llista=[]
#Emplenem la llista llista
for i in range(1,m+1):
    llista+=[i]
numero=[]
for i in range (n):
    t=choice(llista)
    numero+=[t]
print(f"Les boles extretes son {numero}")