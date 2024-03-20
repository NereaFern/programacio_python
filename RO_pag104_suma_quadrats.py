#RO_Pag104_suma_quadrats.py
'''Suma de los cuadrados de los primeros números naturales'''
n=int(input("Escrigui el valor final: "))
x=0
u=1
t=0
c=0
while c<=n:
    u+=1
    t=pow(u,2)
    c=t+u
    
print(c)
    