#RO_Pag_071_exercici_3_ganancia_i_articles.py
'''3) El costo mensual c en dólares al fabricar una cantidad x de artículos está dado por:
c = 50 + 2x, mientras que el ingreso por la venta de x artículos está dada por: v = 2.4x
a) Calcule la ganancia que se obtendrá al fabricar y vender 400 artículos
b) Determine cuantos artículos deben fabricarse y venderse para que el ingreso iguale
a los gastos'''
articles_fabricats = int(input("Nombre d'articles fabricats: "))
articles_venuts = int(input("Nombre d'articles venuts: "))

despeses = 50+2*articles_fabricats
ganancies = 2.4*articles_venuts
guany_total = ganancies-despeses
print("El guany total és de", guany_total, "$") 