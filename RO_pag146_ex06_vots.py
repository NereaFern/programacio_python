#R0_Pag_146_ex_6_vots.py
'''6.- Lea los votos de n personas. Cada voto es un número 1, 2, o 3 correspondiente a tres
candidatos. Si el dato es 0 es un voto en blanco. Si es otro número es un voto nulo.
Determine el total de votos de cada candidato y el total de votos blancos y nulos.'''
n=int(input("Nombre de votacions :"))
x=0
candidat1=0
candidat2=0
candidat3=0
blanc=0
nul=0
while x<n:
    x +=1
    vot=int(input(f"Escrigui la votació de la {x} persona (1 per candidat 1, dos pel candidat 2 i 3 pel candidat 3 i 0 per a blanc): "))
    if vot==1:
        candidat1 +=1
    elif vot==2:
        candidat2 +=1
    elif vot==3:
        candidat3 +=1
    elif vot==0:
        blanc +=1
    else:
        nul +=1
print(f'''Hi han:
-{candidat1} bots pel candidat 1
-{candidat2} bots pel candidat 2
-{candidat3} bots pel candidat 3
-{blanc} bots en blanc
-{nul} bots nuls''')