#P10_temperatura.py
'''Lea un valor de temperatura t y un código p que puede ser 1 o 2. Si el código es 1
convierta la temperatura t de grados f a grados c con la fórmula c=5/9(t-32). Si el código
es 2 convierta la temperatura t de grados c a f con la fórmula: f=32+9t/5. Muestre el
resultado.
*****************************************************
'''

#Determinar el valor de les variables
temperatura = float(input("Posi la temperatura: "))
codi = input("Marqui si la temperatura està en graus centigrags (C) o en farenhait (F): ")

#Calcular temperatura
if (codi == "F"):
    temperatura = 5/9*(temperatura-32)
    print(f"La temperatura és de {round(temperatura, 2)} ºC")
else:
    temperatura = 32+9*temperatura/5
    print(f"La temperatura és de {round(temperatura, 2)} ºF")