#Pag_41_ex_4.py
'''4. Calcule un valor aproximado para la constante π usando la siguiente expresión:
 π/4 = 1 – 1/3 + 1/5 – 1/7 + 1/9 – 1/11 + 1/13 ...'''
n = 3
pi=1-1/n
for n in range(5,1000,4):
    n +=2
    pi=pi-1/n
for n in range(3,1000,4):
    n +=2
    pi=pi+1/n
pi=pi*4
    
print(pi)
