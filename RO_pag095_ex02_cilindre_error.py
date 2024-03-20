#RO_Pag_95_ex_2_cilindre_error.py
'''2. Dados el radio y altura de un cilindro, si la altura es mayor al radio calcule y muestre el
valor del volumen, caso contrario muestre el mensaje: 'Error'
'''
from math import *
radi=float(input("Posi el valor del radi del cilindre en cm: "))
altura=float(input("Posi el valor de l'altura del cilindre en cm: "))


if(altura>radi):
    volum=2*pi*pow(radi,2)
    print("El volum és de", volum,"cm3")
else:
    print("Error")