''' P01_areatriangle.py
***********	AREA TRIANGLE **********************
Describir un algoritmo para calcular el área de un triángulo conocidos sus tres 
 lados (pàgina 20)
'''
# importem la funció arrel del mòdul math
from math import sqrt

# Assignem els valors a les variables a, b i c
a, b, c = 5, 3, 6

# Assignem la semisuma del perímetrea la variable t
t = (a + b + c) /2
# Assignem el resultat del càlcul de l'àrea a la variable s
s = round(sqrt(t*(t-a)*(t-b)*(t-c)),3)

'''
UN ALTRA FORMA DE FER ELMATEIX CALCUL
s = (t*(t-a)*(t-b)*(t-c))**(0.5)
# Arrodonim a 2 decimalsamb la funció round()

s = round(s, 2)
'''

# Treure per cónsola o pantallael resultat obtingut
print("El resultat de l'àrea del triangle és: ", s)



