#RO_Pag150_ex36_suma.py
'''36. Escriba un programa que reciba un valor para n y otro para m y muestre el
resultado de la siguiente suma:'''
n=int(input("Escrrigui el valor de n: "))
m=int(input("Escrigui el valor de m: "))
suma=0
for i in range(1,n+1):
    for j in range(1,m+1):
        suma+=(pow(i,2)+pow(j,2)+i*j)
print(f"La suma dona un resultat de {suma}")