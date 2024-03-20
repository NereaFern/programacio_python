#RO_pag231_ex2_caixes.py
'''2. Lea una lista de los pesos de las n cajas en un contenedor. Determine cuantas cajas
tienen el peso mayor al peso promedio del grupo.
'''
preus=[]
suma=0
n=int(input("Escrigui el nombre de caixes: "))
#For per a emplenar la llista i més o menys la mitjana
for i in range(1,n+1):
    x=float(input(f"Escrigui el preu de la caixa {i}: "))
    preus+=[x]
    suma+=x
mitjana=suma/len(preus)
#For per imprimir els nombres que estan per sobre la mitjana
for z in range preus:
    if z>mitjana:
        