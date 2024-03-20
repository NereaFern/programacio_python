#RO_pag218_exemple_restar.py
n=int(input("Numero de nombres: "))
v=[]
u=[]
for i in range(n):
    x=int(input("Escrigui un nombre: "))
    v.append(x)
for t in v:
    if t not in u:
        u.append(t)
print(u)
