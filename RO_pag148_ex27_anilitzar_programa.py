#RO_Pag_148_ex_27_anilitzar_programa.py
'''27. Analice el siguiente programa. Escriba los resultados que se obtendrían si el dato que
ingresa para n es 25
'''
n = int(input('Ingrese un dato: '))
r = 0
while n>0:
    d = n%2
    n = n//2
    r = 10*r + d
print(d, n, r) 