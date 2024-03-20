#R0_Pag_146_ex_9_coordenades.py
'''9.- Se tienen una lista de las coordenadas x, y de n puntos en un plano. Lea
sucesivamente las coordenadas de cada punto y acumule las distancias del punto al
origen. Muestre la distancia total acumulada. '''
from math import*

n=int(input("Escrigui  el nombre de coordenades: "))
x=0
d_total=0
while x<n:
    x +=1
    print(x)
    x=float(input(f"Posi la coordenada x de la {x} coordenada"))
    y=float(input(f"Posi la coordenada y de la {x} coordenada"))
    distancia=sqrt(pow(x,2)+pow(y,2))
    d_total +=distancia
print("La distància total és de", d_total)