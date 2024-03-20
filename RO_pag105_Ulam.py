#R0_Pag105_Ulam.py
'''. Dado un número entero, genere una secuencia numérica con la siguiente regla.
Esta secuencia se denomina de Ulam. Esta secuencia siempre llega al número 1 '''
x=int(input("Escrigui el valor final:"))
while x!=1:
    if x%2==0:
        x=x/2
    else:
        x=3*x+1
    print(x)