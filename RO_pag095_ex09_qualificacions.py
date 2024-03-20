#R0_Pag_96_ex_10_tipus_de_triangles.py
'''10. Dados los tres lados de un triángulo determine su tipo: Equilátero, Isòsceles, o
Escaleno'''
x=float(input("Escrigui el primer costat del triangle ="))
y=float(input("Escrigui el segon costat del triangle ="))
z=float(input("Escrigui el tercer costat del triangle ="))
if(x==y and y==z):
    print("És un triangle equilater")
elif(x==y and z != y):
    print("És un triange isoceles")
elif(y==z and z != x):
    print("És un triange isoceles")
elif(z==x and z != y):
    print("És un triange isoceles")
else:
    print("És un triangle escaler")