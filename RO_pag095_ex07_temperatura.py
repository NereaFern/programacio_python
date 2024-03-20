#R0_Pag_95_ex_7_temperatura.py
'''7. Lea un valor de temperatura t y un código p que puede ser 1 o 2. Si el código es 1
convierta la temperatura t de grados f a grados c con la fórmula c=5/9(t-32). Si el código
es 2 convierta la temperatura t de grados c a f con la fórmula: f=32+9t/5, caso contrario
muestre un mensaje de error. '''

codi = int(input("Escrigui 1 o 2: "))
if(codi==1):
    temperatura = float(input("Escrigui la temperatura en graus farenhait: "))
    temperatura =5/9*(temperatura-32)
    print("La temperatura és de", temperatura, "ºC")
elif(codi==2):
    temperatura = float(input("Escrigui la temperatura en graus centigrafs: "))
    temperatura = 32+9*temperatura/5
    print("La temperatura és de", temperatura, "ºF")
else:
    print("El codi ha de ser 1 o 2")