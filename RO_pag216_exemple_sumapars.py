#RO_pag216_exemple_sumapars.py
def sumapars(n):
    v=[]
    s=0
    for i in range(n):
        x=int(input("Escrigui el seguent nombre: "))
        v.append(x)
    for t in v:
        if t%2==0:
            s+=t
    return s
n=int(input("Nombre de números: "))
print(sumapars(n))