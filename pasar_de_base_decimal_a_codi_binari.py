#pasar_de_base_decimal_a_codi_binari.py
def binari(d):
    l=[]
    while d!=0:
        u=d%2
        d=d//2
        l.insert(0,str(u))
    while l[0]==0:
        l-=l[0]
    l="".join(l)
    return l

print(binari(35))
        