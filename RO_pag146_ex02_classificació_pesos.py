#R0_Pag_146_ex_2_clasificació_pesos.py
'''2.- Clasifique los pesos de los n objetos de una bodega en tres grupos: menor a 10 Kg.,
entre 10 y 20 Kg., mas de 20 Kg. Los datos ingresan uno a la vez en un ciclo.'''
n=int(input("Escrigui el nombre d'objectes:"))
q=0
menor=0
mitja=0
gran=0
while q<n:
    q+=1
    p=float(input(f"Escrigui el pes del paquet {q} :"))
    if p<10:
        menor=menor+1
    elif p>=10 and p<=20:
        mitja +=1
    else:
        gran +=1
print(f"Hi han {menor} paquets amb un nombre menor a 10 kg, {mitja} entre 10 i 20 kg i {gran} que pessen més de 20 kg")