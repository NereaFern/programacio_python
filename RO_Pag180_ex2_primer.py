#RO_Pag180_ex2_primer.py
'''2. Escriba un programa de prueba que use la función primo y encuentre dos números
enteros aleatorios menores que 100 tales que su suma sea también un número primo.'''
from random import randint
def conteo(n):
    count= 0
    for i in range(1,n+1):   
        if n%i==0:
            count +=1
    return count
