#RO_Pag_180_ex_2_nombre_primer.py
'''2. Escriba un programa de prueba que use la función primo y encuentre dos números
enteros aleatorios menores que 100 tales que su suma sea también un número primo.
'''
from random import*
n=randint(1,100)
for i in range(2,n):
    if n%i==0:
        print(f"El numero {n} no és primer")
        break
    else:
        continue
if n%i!=0:
    print(f"El numero {n} és primer")