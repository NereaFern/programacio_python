#R0_Pag_96_ex_15_contrasenya.py
'''15. Un código de tres cifras debe cumplir la siguiente regla para que sea vàlido: La tercera
cifra debe ser igual al mòdulo 10 del producto de las dos primeras cifras. Escriba un
programa que lea un código y verifique si cumple la regla anterior. Muestre un mensaje
correspondiente.'''
from math import*
x1=int(input("Possi el valor de la primera xifra: "))
x2=int(input("Possi el valor de la segona xifra: "))
x3=int(input("Possi el valor de la tercera xifra: "))
x1=sqrt(x1*x2)

if trunc(x1)==x3:
    print("Sí compleix la regla")
else:
    print("No compleix la regla")