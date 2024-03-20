#R0_Pag_146_ex_7_valor_mes_gran.py
'''8.- Encuentre el mayor valor de la función f(x)=sen(x)+ln(x), para los valores:
 x = 1.0, 1.1, 1.2, 1.3, ..., 4
'''
from math import*
x=float(1)
m=0
f=float(0)
i=0
while x<=4:
    m=sin((x*pi)/180)+log((x*pi)/180)
    x +=0.1
    if m>f:
        f=m
        i=x
    
print(f"La funció més gran és {round(x,1)}")