#R0_Pag_96_ex_13_pagament_setmanal.py
'''13. Juan, Pedro y José trabajan en una empresa que paga semanalmente. Ingrese para
cada uno los siguientes datos del trabajo semanal: horas trabajadas, salario por hora, y
descuentos. Calcule el pago semanal que recibirá cada uno y determine cual de los tres
recibirá el mayor pago semanal. No considere el pago de horas extras.'''
jh=int(input("Escrigui les hores treballades pel Juan: "))
js=int(input("Escrigui el salari per hora del Juan: "))
jd=int(input("Escrigui el descompte del Juan (%): "))
ph=int(input("Escrigui les hores treballades pel Pedro: "))
ps=int(input("Escrigui el salari per hora del Pedro: "))
pd=int(input("Escrigui el descompte del Pedro (%): "))
oh=int(input("Escrigui les hores treballades pel José: "))
os=int(input("Escrigui el salari per hora del José: "))
od=int(input("Escrigui el descompte del José (%): "))
jd=jd/100
psj=jh*js*jd
pd=pd/100
psp=ph*ps*pd
od=od/100
pso=ph*ps*pd
if psj==psp and psp==pso:
    print("Els tres salaris son iguals")
elif psj==psp and psp>pso:
    print("Els salaris més alts son el del Juan i el Pedro")
elif psp==pso and psp>psj:
    print("Els salaris més alts on el del Pedro i el José")
elif psj==pso and pso>psp:
    print("Els salaris més alts son el del Juan i el José")
elif psj>pso and psj>psp:
    print("El salri més alt és el del Joan")
elif pso>psj and pso>psp:
    print("El salari més alt és el del José")
elif psp>pso and psp>psj:
    print("El saslari més alt és el del Pedro")