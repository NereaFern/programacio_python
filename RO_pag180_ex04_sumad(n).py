#RO_pag180_ex04_sumad(n).py
'''4. Escriba una función sumad(n) que entregue la suma de las cifras de un número dado n.
Con esta función escriba un programa que genere 10 números aleatorios entre 1 y 100 y
encuentre cual de ellos tiene la mayor suma de sus cifras.
'''
def sumad(n):
    k=9#El quoficient que ens sortirà de dividir el nostre numero n/comp
    comp=1#10 elevat a x
    suma=0#Suma de les xifres del número donat
    cd=0
    while k>1:
        k=n/comp
        if k<1:
            comp/=10
        elif k==1:
            comp=comp
        else:
            comp*=10
    for i in range(comp+1,1,-10):
        cd=n-q
        suma+=cd//i
        q=i
    return suma
n=int(2808)
print(sumad(n))