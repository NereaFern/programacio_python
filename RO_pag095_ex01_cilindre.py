#RO_Pag_95_ex_1_cilindre.py
'''1. Dados el radio y altura de un cilindro, si la altura es mayor al radio calcule y muestre el
valor del volumen del cilindro, caso contrario muestre el valor del área del cilindro.'''
from math import *
radi=float(input("Posi el valor del radi del cilindre en cm: "))
altura=float(input("Posi el valor de l'altura del cilindre en cm: "))

if(altura>radi):
    volum=2*pi*pow(radi,2)*altura
    print("El volum és de ", volum, "cm3")
else:
    area=2*(2*pi*pow(radi,2))+2*pi*radi*altura
    print("L'àrea és de", area, "cm2")