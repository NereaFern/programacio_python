#R0_Pag_146_ex_3_quantitat_de_termes.py
'''3. Determine la cantidad de términos que deben sumarse de la serie 1*1+ 2*2+ 3*3+ 4*4+ ...
para que el valor de la suma sea mayor a un número x ingresado al inicio.'''
x=int(input("Escrigui el nombre que ha de sobrepasar: "))
j=0
n=0
nombres=0
while j<x:
    n+=1
    j=j+pow(n,2)
    nombres +=nombres
print("Es necessiten", n, "nombres")