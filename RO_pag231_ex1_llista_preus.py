#RO_pag231_ex1_llista_preus.py
'''1. Una persona tiene una lista con los precios de n artículos y dispone de una cierta
cantidad de dinero. Escriba un programa para leer estos datos y almacenarlos en un
vector:
a) Muestre los numeros de los artículos que puede comprar
b) Para cada artículo cuyo precio es menor que la cantidad de dinero disponible, determine
cuantas unidades puede comprar'''
preus=[]
n_articles=0
n_preus=int(input("Posi el nombre d'articles dels quals vols saber el  preu: "))
diner=float(input("Escrigui la quantitat de diner que disposa: "))
diner_total=diner
for i in range (1,n_preus+1):
    x=float(input(f"Escrigui el preu de l'article {i}: "))
    preus+=[x]
for t in preus:
    while diner_total>=t:
        diner_total-=t
        n_articles+=1
    print(f"Et pots comprar {n_articles}")
    n_articles=0
    diner_total=diner