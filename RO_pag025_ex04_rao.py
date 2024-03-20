#P04_rao.py
'''La siguiente fórmula proporciona el enésimo término u de una progresión aritmética:
 u = a + (n − 1) r
en donde a es el primer término, n es el la cantidad de términos y r es la razón entre dos
términos consecutivos. Calcular el valor de r dados u, a, n'''
from math import sqrt
#Determina el valor de les variables
u = float(input("Escrigui el valor de l'enésim terme: "))
a = float(input("Escrigui el valor del primer terme: "))
n = float(input("Escrigui el valor de la quantitat de termes: "))
#Trobar el valor de r
r = (u-a)/(n-1)
print("El valor de la raó és de ", round(r, 2))