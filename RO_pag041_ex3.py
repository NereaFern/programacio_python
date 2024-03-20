#Pag_41_ex_3.py
'''3. Determine la suma de los n primeros números de la serie: 1, 1, 2, 3, 5, 8, 13, 21, ....
en la cual cada término, a partir del tercero, se obtiene sumando los dos términos
anteriores
'''
#Assignar el valor a les variables:
primer_nombre=int(input("Posi el valor del primer nombre: "))
segon_nombre=int(input("Posi el valor del segon nombre: "))
for n in range(primer_nombre+segon_nombre,22):
    seguent_nombre = primer_nombre+segon_nombre
    print(seguent_nombre)
    primer_nombre=segon_nombre
    segon_nombre = seguent_nombre
    
