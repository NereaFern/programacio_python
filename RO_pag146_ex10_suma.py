#R0_Pag_146_ex_10_suma.py
'''10.- Determine la suma de los términos de la serie 1*1*1+2*2*2+3*3*3+ ... + n*n*n
en donde n es un número natural
'''

n=int(input("Escrigui l'últim nombre de la serie: "))

suma=0
for i in range (n+1):
    suma=suma+pow(i,3)
   
print("La suma final és", suma)