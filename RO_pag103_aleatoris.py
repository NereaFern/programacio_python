#RO_Pag103_aleatoris.py
'''Simular lanzamientos de un dado. Muestre el resultado en cada intento. Finalice
cuando salga el número 6.'''
from random import*
i=0
x=0
while x!= 6:
    x=randint(1,6)
    i+=1
print(i)