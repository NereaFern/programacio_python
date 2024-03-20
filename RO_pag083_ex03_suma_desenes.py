#RO_Pag_83_ex_3_suma_desenes.py
'''3. Lea dos números de tres cifras cada uno. Sume la cifra central del primer número con la
cifra central del segundo número y muestre el resultado.'''

n1=int(input("Posi el valor del primer nombre de tres xifres :"))
n2=int(input("Posi el valor del segon nombre de tres xifres :"))

n1= n1%100
n1=n1//10
n2 = n2%100
n2 = n2//10
suma = n1+n2
print(suma)