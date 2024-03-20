#RO_pag220_exemple_major_nombre.py
def majornombre(n):
    v=[]
    r=0
    p=0
    for i in range(n):
        x=int(input("Escrigui un nombre per la llista :"))
        v.append(x)
    for t in v:
        if t>p:
            p=t
            r+=1
    return f"Posició {r} numero {p}"
n=int(input("Numero de nombres: "))
print(majornombre(n))