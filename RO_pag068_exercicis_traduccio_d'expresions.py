#RO_Pag_068_exercicis_traduccio_d'expresions.py
#tan(x***3)
from math import *

x= float(input("Escrigui el valor de x en graus: "))
x = (x*pi)/180
x = tan(pow(x,3))

print("La tangent de x al cub és", x )
#2

y = (cos(pi+0.2)-3)/(tan(sqrt(2)-2)+pow(0.2,3))
print(y,"º")
#3
x = float(input("Escrigui un nou valor: "))
z = ((sqrt(2)+1)/(sin(2)-0.1))/(pow(x,2)-1)+2
print(z)
#4
b = int(input("Escrigui un valor per a b: "))
c =int(input("Escrigui un valor per a c: "))
k = b<5 or c==0
print(k)
#5
a=int(input("Escrigui un valor per a a: "))
b=int(input("Escrigui un nou valor per a b: "))

h = a<b or b==5
print(h)