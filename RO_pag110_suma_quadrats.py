#RO_Pag110_suma_quadrats.py
''' Se necesita sumar los cuadrados de los primeros n números naturales.'''
n=int(input("Últim nombre natural: "))
x=0
for n in range (1, n+1):
    x+=pow(n,2)
print(x)