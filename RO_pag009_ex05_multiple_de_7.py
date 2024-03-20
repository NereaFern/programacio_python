#R0_Pag_9_ex_5_multiple_de_7.py
'''5. Lea un número. Determine si es entero y múltiplo de 7'''
nombre=float(input("Escrigui un nombre d'una xifra: "))

if (round(nombre,0)==nombre):
    print("El nombre  és enter")
else:
    print("El nombre no és enter")
if (nombre%7==0):
    print("El nombre és multimple de 7")
else:
    print("El nombre no és multiple de 7")