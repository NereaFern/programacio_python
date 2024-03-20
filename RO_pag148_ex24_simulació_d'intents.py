#RO_Pag_148_ex_24_simulació_d'intents.py
'''24.- Realice la simulación de n intentos de lanzamientos de un dado con las siguientes
reglas: si sale 6 gana $5. Si sale 1 gana $1. Si sale 2, 3, 4 o 5 pierde $2. Determine la
cantidad acumulada al final del juego
'''
from random import*
#Inicialitzem variables
n=int(input("Escrigui el nombre d'intents que faras:" )) #Vegades que tira el dau
d=0 #Nombre total de diners que guanyarà/perdrà després de la partida
#Aquest for servirà per veure el diner aconseguit després dels n intents
for i in range(1,n+1):
    numero=randint(1,6)
    if numero==6:
        d+=5
    elif numero==1:
        d+=1
    else:
        d-=2
print(f"Després de {n} intents hauràs guanyat ${d}")