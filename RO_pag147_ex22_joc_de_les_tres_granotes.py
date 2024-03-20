#RO_Pag_147_ex_22_joc_de_les_tres_granotes.py
'''22.- Simule el siguiente juego entre tres ranas. Las ranas están al inicio de una pista de 20
m. En turnos cada rana realiza un salto. El salto es aleatorio y puede ser:
a) Brinca y cae en el mismo lugar
b) Salta 0.5 m en la dirección correcta
c) Salta 1 m en la direccion correcta
d) Salta 0.5 m retrocediendo.
Determine cual de las tres ranas llega primero a la meta.'''
from random import choice
#Inicialitzem les variables:
granota1=0#Posició de la primera granota
granota2=0#Posició de la segona granota
granota3=0#Posició de la tercera granota
salt=[0.5,1,-0.5,0]
#A continuació mirarem quina granota arriba abans:
while granota1!=20 and granota2!=20 and granota3!=20:
    n=choice(salt)
    granota1+=n
    n=choice(salt)
    granota2+=n
    n=choice(salt)
    granota3+=n
if granota1==20:
    g=1
elif granota2==20:
    g=2
elif granota3==20:
    g=3
print(f"La gronata guanyadora és la granota {g}")

    