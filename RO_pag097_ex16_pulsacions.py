#R0_Pag_97_ex_16_pulsacions.py
'''16. El número de pulsaciones que debe tener una persona por cada 10 segundos de
ejercicio aeróbico se calcula con la fórmula:
Género femenino (1): número de pulsaciones = (220 - edad en años)/10
Género masculino (2): número de pulsaciones = (210 - edad en años)/10
Lea la edad y el género y muestre el número de pulsaciones. '''

g=input("Escrigui 1 si te génere femení i 2 si té génere masculí: ")
e=int(input("Escrigui la seva edat: "))

if g=="1":
    p=(220-e)/10
elif g=="2":
    p=(210-e)/10
print("Les pulsacions que hauria de tindre son", p, "cada 10 segons")