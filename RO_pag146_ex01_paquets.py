#R0_Pag_146_ex_1_paquets.py
'''1.- Calcule el promedio, el menor valor y el mayor valor de los pesos de n paquetes en una
bodega. Estos datos ingresan uno a la vez dentro de un ciclo. n es un dato ingresado al
inicio'''
n=int(input("Escrigui el nombre de paquets: "))
i=1
pg=0
pp=pow(99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999,9999999999999999999)
promig=0
while i<=n:
    p=float(input("Escrigui el pes del paquet: "))
    promig=promig+p
    i=i+1
    if p>pg:
        pg=p
    elif p<pp:
        pp=p
promig = promig/n
print("El paquet que pesa més pesa", pg)
print("El paquet que pesa menys pesa",pp)
print("El promitg és de", promig)