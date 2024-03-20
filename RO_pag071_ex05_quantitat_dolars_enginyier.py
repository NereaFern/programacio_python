#RO_Pag_071_exercici_5_quantitat_dolars_enginyier.py
'''5) Un ingeniero desea tener una cantidad de dólares acumulada en su cuenta de ahorros
para su retiro luego de una cantidad de años de trabajo. Para este objetivo planea
depositar un valor mensualmente.'''
from math import*
nombre_diposits = int(input("Nombre de diposits mensuals realitzats: "))
interes_mensual = float(input("Posi el valor nominal de l'interés mensual: "))
valor_diposit = int(input("Escrigui el valor de cada diposit mensual: "))

a = valor_diposit*(pow(1+interes_mensual,nombre_diposits)-1)/interes_mensual
print(a)