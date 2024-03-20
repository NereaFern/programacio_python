#R0_Pag_96_ex_11_coordonades.py
'''11. Dadas la abscisa y ordenada de dos puntos, calcule su distancia al origen y determine
cual de los dos puntos (primero o segundo) está más cerca del origen. La respuesta
deberá ser un mensaje: ‘Punto 1’ o ‘Punto 2’
'''
from math import*
t1=float(input("Posi el valor x del primer punt: "))
t2=float(input("Posi el valor y del primer punt: "))
o1=float(input("Posi el valor x del segon punt: "))
o2=float(input("Posi el valor y del segon punt: "))
t= sqrt(pow(t1,2)+pow(t2,2))
o= sqrt(pow(o1,2)+pow(o2,2))
if o==t:
    print("Els dos estan a la mateixa distància de l'origen")
elif t>o:
    
    print("Punt 2")
elif o>t:
    print("Punt 1")