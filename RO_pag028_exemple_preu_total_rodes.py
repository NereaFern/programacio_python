#P07_preu_total_rodes.py
'''Calcular el valor total que una persona debe pagar por la compra de llantas en un almacén
que tiene la siguiente promoción: Si la cantidad de llantas comprada es mayor a 4, el
precio unitario tiene un descuento de 10%. El algoritmo debe ingresar como datos la
catidad de llantas y el precio inicial de cada llanta. Mediante una comparación el algoritmo
deberá aplicar el descuento.'''

#Determinar el preu de les variables
rodes = int(input("Insereixi el nombre de rodes necessitades: " ))
preu_roda = float(input("Insereixi el preu per cada roda en €: "))

#Calcular el preu total
if (rodes > 4):
    preu_roda *= 0.9
    
preu_total = preu_roda*rodes

print(f"El preu total serà de {round(preu_total,2)} €")
