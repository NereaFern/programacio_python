#RO_Pag_147_ex_14_compra.py
'''14.- Una persona tiene una lista con los precios de n artículos y dispone de una cierta
cantidad de dinero. Los artículos son identificados con la numeración natural. Escriba un
programa para leer estos datos y obtener los siguientes resultados
a) Muestre la identificación de los artículos que puede comprar
b) Para cada artículo cuyo precio es menor que la cantidad de dinero disponible, determine
la cantidad que puede comprar.
'''
'''compra=0 #Comptador d'articles
u=0 #comptador d'articles
articles=[545,738,876,999] # Preu dels articles'''
#diners=float(input("Escrigui a continuació el nombre de diners disponibles: "))
'''for i in range (4):
    t=articles[i]
    print(t)
    if diners>=t:
        compra=diners//t
    else:
        compra=0
    print(f"Es poden comprar {compra} articles de l'article {i+1}")'''
        
'''for i in articles:
    print(i)
    if diners>=i:
        compra=diners//i
    else:
        compra==0
    u+=1
    print(f"Es poden comprar {compra} articles de l'article {u}")'''
'''
narticles=int(input("Escrigui el nombre d'articles:"))
particles=[]#Llista per a emplenar el preu dels articles
u = 0 #Comptador d'articles
# Emplenar la llista particles amb els preus demanats per teclat
for i in range (1, narticles+1):
    pn=float(input(f"Escrigui el preu de l'article {i}: "))#Preu que posarem dins la llista particles
    particles +=[pn]
    
# Càlcul del nombre d'articles que es pot comprar amb els diners disponibles
print('Amb el pressupost ingressat anteriorment, podràs comprar:')
for i in particles:
    if diners>=i:
        compra=diners//i
    else:
        compra=0
    u+=1
    print(f"{int(compra)} unitats de l'article {u}")
'''
#initzialitzem variables:
n=int(input("Escrigui el nombre d'articles: "))#Nombre d'articles
preu=[]#Llista on posarem el preu de tots els articles
i=0 #Comptador
#a continuació emplenarem la llista preu
while i<n:
    i+=1
    t=float(input(f"Escrigui el preu de l'article {i}: "))
    preu +=[t]
d=float(input("Ara escrigui el nombre de diners disponibles: "))
i=0
#A continuació calcularem quantes unitats podem tindre de cada article
print("Pots comprar-te:")
while i<len(preu):
    u=d//preu[i]
    i+=1
    print(f"{int(u)} unitats de l'article {i}")

    

    