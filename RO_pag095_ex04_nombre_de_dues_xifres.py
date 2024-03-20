#R0_Pag_95_ex_4_nombre_de_dues_xifres.py
'''4. Lea un número de dos cifras. Determinar si la suma de ambas cifras es un número par o
impar. Muestre un mensaje
'''

numero=int(input("Escrigui un valor de dues xifres: "))
xifra1= numero//10
xifra2= numero-(xifra1*10)
suma = xifra1+xifra2
if(suma%2==0):
    print("La suma de les dues xifres és un nombre par")
else:
    print("La suma de les dues xifres és un nombre impar")
print(xifra1, xifra2)