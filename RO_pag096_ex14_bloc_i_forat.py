#R0_Pag_96_ex_14_bloc_i_forat.py
'''14. Lea las dimensiones de un bloque rectangular (largo, ancho y altura del bloque), y el
diámetro de un agujero. Determine si es posible que el bloque pueda pasar por el agujero. '''
from math import*
x=float(input("Escrigui el valor de la llargada del bloc: "))
y=float(input("Escrigui el valor de l'altura del bloc: "))
z=float(input("Escrigui el valor de l'amplada del bloc: "))
d=float(input("Escrigui el valor del diametre del forat: "))
d1=sqrt(pow(x,2)+pow(y,2))
d2=sqrt(pow(x,2)+pow(z,2))
d3=sqrt(pow(y,2)+pow(z,2))
if d1<d:
    print("Sí que pot passar pel forat")
elif d2<d:
    print("Sí que pot passar pel forat")
elif d3<d:
    print("Sí que pot passar pel forat")
else:
    print("No pot passar pel forat")