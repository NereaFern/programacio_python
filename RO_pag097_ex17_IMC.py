#R0_Pag_97_ex_17_IMC.py
'''17. El índice de masa corporal IMC de una persona se calcula con la fórmula IMC=P/T2
en donde P es el peso en Kg. y T es la talla en metros.
Lea un valor de P y de T, calcule el IMC y muestre su estado según la siguiente tabla:
 IMC Estado
Menos de 18.5 Desnutrido
[18.5 a 25.5] Peso Normal
Más de 25.5 Sobrepeso'''
from math import*
p=float(input("Posi el seu pes en kg: "))
t=float(input("Posi la seva talla en m: "))

imc=p/pow(t,2)
if imc<18.5:
    print("Està desnutrit")
elif imc>=18.5 and imc<=25.5:
    print("Té pes normal")
else imc<25.5:
    print("Té sobrepés")
