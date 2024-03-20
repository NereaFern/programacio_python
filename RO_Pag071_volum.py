#RO_Pag071_volum.py
'''calcule el volumen y el área total de un cilindro de radio 5 metros y altura 4 metros
'''
from math import*
radi = float(input("Posi el valor del radi en metres: "))
altura = float(input("Posi el valor de l'altura en metres: "))

volum= pi*pow(radi,2)*altura
area= altura*radi*2
print("El volum del cilindre és de",volum,"m3 i la seva àrea és de", area,"m2")