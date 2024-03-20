#cramer_3x3.py
print("*****************Primera equació***********************")
x1=float(input("Escrigui el nombre que acompanya a la x: "))
y1=float(input("Escrigui el nombre que acompanya a la y: "))
z1=float(input("Escrigui el nombre que acompanya a la z: "))
a=float(input("Escrigui el resultat de l'equació: "))
print("*****************Segona equació***********************")
x2=float(input("Escrigui el nombre que acompanya a la x: "))
y2=float(input("Escrigui el nombre que acompanya a la y: "))
z2=float(input("Escrigui el nombre que acompanya a la z: "))
b=float(input("Escrigui el resultat de l'equació: "))
print("*****************Tercera equació***********************")
x3=float(input("Escrigui el nombre que acompanya a la x: "))
y3=float(input("Escrigui el nombre que acompanya a la y: "))
z3=float(input("Escrigui el nombre que acompanya a la z: "))
c=float(input("Escrigui el resultat de l'equació: "))
Az=((x1*y2*z3)+(x2*y3*z1)+(x3*y1*z2))-((x3*y2*z1)+(y3*z2*x1)+(z3*x2*y1))
x=(((a*y2*z3)+(b*y3*z1)+(c*y1*z2))-((c*y2*z1)+(y3*z2*a)+(z3*b*y1)))/Az
y=(((x1*b*z3)+(x2*c*z1)+(x3*a*z2))-((x3*b*z1)+(c*z2*x1)+(z3*x2*a)))/Az
z=(((x1*y2*c)+(x2*y3*a)+(x3*y1*b))-((x3*y2*a)+(y3*b*x1)+(c*x2*y1)))/Az
print(f'La solució per aquesta eqüació és: x={x} y={y} i z={z}')