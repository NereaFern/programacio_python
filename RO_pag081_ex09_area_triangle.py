#RO_Pag_81_ex_9_area_triangle.py
'''. Lea la abscisa y ordenada de dos puntos P, Q en el plano: (a, b), (c, d).
Estos puntos y el origen (0, 0) conforman un triángulo.
Calcule y encuentre el área del triángulo.
Fórmula de la distancia del punto P al punto Q:
Fórmula del área del triángulo sabiendo que x, y, z representan el valor de los tres lados del triángulo'''
from math import*
Px = float(input("Posi el valor de la component x del punt P: "))
Py = float(input("Posi el valor de la component y del punt P: "))
Qx = float(input("Posi el valor de la component x del punt Q: "))
Qy = float(input("Posi el valor de la component y del punt Q: "))
x = sqrt(pow(Px,2)+pow(Py,2))
y = sqrt(pow(Qx,2)+pow(Qy,2))
z = sqrt(pow(Qx-Px,2)+pow(Qy-Py,2))
t  =  (x+y+z)/2
s = sqrt(t*(t-x)*(t-y)*(t-z))
print("L'àrea del triangle és",s)