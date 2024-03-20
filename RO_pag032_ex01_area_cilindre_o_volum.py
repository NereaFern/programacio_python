''' P07_Condicional_1.py
 Dados el radio y altura de un cilindro, si la altura es mayor al radio calcule y muestre el 
valor del volumen del cilindro, caso contrario muestre el valor del área del cilindro.
'''
from math import pi
# Introduir dades
radi = float(input("Introdueix el radi del cilindre en cm: ")) # string 'str'
altura = float(input("Introdueix l'altura del cilindre en cm: "))

#Càluls
a_base = pi * pow(radi,2)
a_lateral = 2 * pi * radi  * altura
a_total = 2 * a_base + a_lateral
volum = a_base * altura

if (altura > radi):
    print("El volum del cilindre en cm3 és de: ", round(volum, 2), "cm3")

else:
    print("L'àrea del cilindre és:" , round(a_total, 2), "cm2")

print("FI del programa")
    
    