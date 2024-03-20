''' P02_area_volum_cilindre.py
Dados el radio y altura de un cilindro calcule el área total y el volumen
'''
from math import pi

# Demanem a l'usuari amb la funció input que introdueixi un número i a més ens assegurem de que sigui float perquè la funció input nomésentra tipus string (caracters)
r = float(input("Introdueix el radi del cilindre en cm: ")) # string 'str'
h = float(input("Introdueix l'altura del cilindre en cm: "))

# Calculem l'àrea i assignem a la variable a i el volum la variable v

a_base = pi * pow(r,2) # pow(r,2) és el mateix que r**2
a_lateral = 2 * pi * r  * h
a_total = 2 * a_base + a_lateral

v = a_base * h

print("L'àrea total del cilindre és: ", round(a_total, 2) , "cm2")
print("El volum del cilindre és: ", round(v, 2) , "cm3")


