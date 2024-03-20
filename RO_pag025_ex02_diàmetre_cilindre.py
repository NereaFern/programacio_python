#P03_diàmetre_cilindre.py
'''Se tiene un recipiente cilíndrico con capacidad en litros. Su altura es un dato en metros.
Determine el diámetro de la base
'''
from math import sqrt, pi
#Primer determinem el valor de les variables
h = float(input(" Dona'm l'altura del recipent en metres: "))
c = float(input("Dona'm la capacitat del recipient en litres: "))
#Ara, farem la conversió de litres a metres cúbics
c = c / pow(10 , 3)
#Ja podem buscar el diàmetre
d = sqrt((c*4)/(h*pi))
print("El diàmetre de la base serà de" , round(d , 2), "m")