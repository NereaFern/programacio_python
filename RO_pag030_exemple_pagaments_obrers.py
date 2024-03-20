#P08_pagaments_obrers.py
'''Para el pago semanal a un obrero se consideran los siguientes datos: horas trabajadas,
tarifa por hora y descuentos. Si la cantidad de horas trabajadas en la semana es mayor a
40, se le debe pagar las horas en exceso con una bonificación de 50% adicional a la tarifa
normal. 
****************************************************************'''

#Determinar valor de les variables
hores_treballades = float(input("Insereixi el nombre d'hores treballades: "))
tarifa_per_hores = float(input("Insereixi la tarifa per hora en euros: "))
descomptes = float(input("Insereixi els descomptes adquirits en euros: "))

#Calcular el valor de la tarifa normal
if(hores_treballades > 40):
    tarifa_hores_extra = (hores_treballades-40)*1.5*tarifa_per_hores
    tarifa_total = tarifa_hores_extra+ 40*tarifa_per_hores+descomptes
else:
    tarifa_total = hores_treballades*tarifa_per_hores+descomptes
print(f" La teva tarifa total serà de {round(tarifa_total , 2)} €")
