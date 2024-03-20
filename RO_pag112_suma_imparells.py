#RO_Pag112_suma_imparells.py
'''Describir en notación Python una solución al siguiente problema: Dado un
entero positivo n, se desea verificar que la suma de los primeros n números impares es
igual a n**2
'''
n=int(input("Escrigui un nombre: "))
s=0
q=n//2
print(q)
for i in range(1,n+q+1,2):
        s+=i
        print(i)

