#cramer_2x2.py
print("*****************Primera equació***********************")
x1=float(input("Escrigui el nombre que acompanya a la x: "))
y1=float(input("Escrigui el nombre que acompanya a la y: "))
a=float(input("Escrigui el resultat de l'equació: "))
print("*****************Segona equació***********************")
x2=float(input("Escrigui el nombre que acompanya a la x: "))
y2=float(input("Escrigui el nombre que acompanya a la y: "))
b=float(input("Escrigui el resultat de l'equació: "))
Az=(x1*y2)-(x2*y1)
x=((a*y2)-(b*y1))/Az
y=((x1*b)-(x2*a))/Az
print(f'La solució per aquesta equació és:x={x} i y={y}')