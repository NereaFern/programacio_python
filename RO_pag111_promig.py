#R0_Pag_111_promig.py
''' Calcule y muestre el promedio de un grupo de datos ingresados desde el teclado'''
n=int(input("Quantitat de dades: "))
s=0
for i in range(1,n+1):
    x=int(input(f"Escrigui el {i} nombre: "))
    s+=x
p=s/i
print(x)
