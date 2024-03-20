#algoritmes_amb_cicles_pag_41_ex_1.py

'''. Calcule el mayor valor de los pesos de n paquetes en una bodega. Estos datos ingresan
uno a la vez dentro de un ciclo. Al inicio ingrese el valor de n para especificar la cantidad
de ciclos que se realizarán
###############################################'''
pes_maxim=0
num_paquets=int(input("Possi el nombre de paquets: "))
for n in range(1,num_paquets+1):
    pes_paquet=print("Escrigui el pes del paquet", n, ":")
    pes_paquet = float(input())
    if(pes_paquet>pes_maxim):
        pes_maxim=pes_paquet
print(f"El pes màxim és de {pes_maxim} kg")

#Un altre manera de fer-ho:
'''pes_maxim=0
num_paquets=1
pes_paquet=0
while(num_paquets!=11):
    pes_paquet=print("Escrigui el pes del paquet",num_paquets, ":")
    pes_paquet = float(input())
    if(pes_paquet>pes_maxim):
        pes_maxim=pes_paquet
    num_paquets=num_paquets+1
print(f"El pes màxim és de {pes_maxim} kg")'''