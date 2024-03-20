#RO_Pag_48_ex_28_mateix_programa.py
'''28. Analice el siguiente programa que usa un ciclo for. Escriba un programa equivalente
que produzca el mismo resultado, pero sustituyendo el ciclo for por un ciclo while Debe
definir una variable para conteo de repeticiones y la condición para salir del ciclo.
'''
#Inicialitzem les variables
n = int(input("Ingrese un dato: "))
s = 0
i=0 #Comptador
while i<n:
    s = s + i**2
    i+=1
print(s)
