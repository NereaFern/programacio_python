#RO_pag182_ex21_f(n).py
'''21. Los números triangulares f(n) tienen la regla de formación descrita con el siguiente
grafico para n=1, 2, 3, 4, 5, ...
'''
def triangular_for(n):
    triangle=0
    for i in range(1,n+1):
        triangle+=i
        print(triangle)
def triangular_while(n):
    triangle=0
    compt=1
    while compt<=n:
        triangle+=compt
        compt+=1
        print(triangle)

def suma_triangular(n):
    suma=0
    triangle=0
    for i in range(1,n+1):
        triangle+=i
        suma+=triangle
    return suma
q=int(input("Escrigui un nombre n: "))
'''
triangular_while(q)
triangular_for(q)'''
suma=0
for i in range(1,q+1):
    suma+=suma_triangular(q)
    print(suma)