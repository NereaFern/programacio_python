#R0_Pag_95_ex_8_qualificacions.py
'''8. Dadas las tres calificaciones de dos estudiantes. La calificación final de cada uno es la
suma de sus dos mejores calificaciones. Muestre un mensaje que indique cual estudiante
(1 o 2) tiene la mayor calificación final.'''

estudiant_1_q1=float(input("Posi la primera qualificació del primer estudiant: "))
estudiant_1_q2=float(input("Posi la segona qualificació del primer estudiant: "))
estudiant_1_q3=float(input("Posi la tercera qualificació del primer estudiant: "))

estudiant_2_q1=float(input("Posi la primera qualificació del segon estudiant: "))
estudiant_2_q2=float(input("Posi la segona qualificació del segon estudiant: "))
estudiant_2_q3=float(input("Posi la primera qualificació del terccer estudiant: "))

if(estudiant_1_q1==estudiant_1_q2 and estudiant_1_q1==estudiant_1_q3):
    q=estudiant_1_q1*2
elif(estudiant_1_q1==estudiant_1_q2 and estudiant_1_q1>estudiant_1_q3):
    q=estudiant_1_q1*2
elif(estudiant_1_q1==estudiant_1_q2 and estudiant_1_q1<estudiant_1_q3):
    q=estudiant_1_q1+estudiant_1_q3
elif(estudiant_1_q1==estudiant_1_q3 and estudiant_1_q1>estudiant_1_q2):
    q=estudiant_1_q1*2
elif(estudiant_1_q1==estudiant_1_q3 and estudiant_1_q1<estudiant_1_q2):
    q=estudiant_1_q1+estudiant_1_q2
elif(estudiant_1_q2==estudiant_1_q3 and estudiant_1_q2>estudiant_1_q1):
    q=estudiant_1_q2*2
elif(estudiant_1_q2==estudiant_1_q3 and estudiant_1_q2<estudiant_1_q3):
    q=estudiant_1_q1+estudiant_1_q2
elif(estudiant_1_q1>estudiant_1_q2 and estudiant_1_q1>estudiant_1_q3):
    if(estudiant_1_q2>estudiant_1_q3):
        q=estudiant_1_q1+estudiant_1_q2
    else:
        q=estudiant_1_q1+estudiant_1_q3
elif(estudiant_1_q2>estudiant_1_q1 and estudiant_1_q2>estudiant_1_q3):
    if(estudiant_1_q1>estudiant_1_q3):
        q=estudiant_1_q1+estudiant_1_q2
    else:
        q=estudiant_1_q2+estudiant_1_q3
elif(estudiant_1_q3>estudiant_1_q2 and estudiant_1_q3>estudiant_1_q1):
    if(estudiant_1_q2>estudiant_1_q1):
        q=estudiant_1_q3+estudiant_1_q2
    else:
        q=estudiant_1_q1+estudiant_1_q3
#Estudiant_2

if(estudiant_2_q1==estudiant_2_q2 and estudiant_2_q1==estudiant_2_q3):
    q2=estudiant_2_q1*2
elif(estudiant_2_q1==estudiant_2_q2 and estudiant_2_q1>estudiant_2_q3):
    q2=estudiant_2_q1*2
elif(estudiant_2_q1==estudiant_2_q2 and estudiant_2_q1<estudiant_2_q3):
    q2=estudiant_2_q1+estudiant_2_q3
elif(estudiant_2_q1==estudiant_2_q3 and estudiant_2_q1>estudiant_2_q2):
    q2=estudiant_2_q1*2
elif(estudiant_2_q1==estudiant_2_q3 and estudiant_2_q1<estudiant_2_q2):
    q2=estudiant_2_q1+estudiant_2_q2
elif(estudiant_2_q2==estudiant_2_q3 and estudiant_2_q2>estudiant_2_q1):
    q2=estudiant_2_q2*2
elif(estudiant_2_q2==estudiant_2_q3 and estudiant_2_q2<estudiant_2_q3):
    q2=estudiant_2_q1+estudiant_2_q2
elif(estudiant_2_q1>estudiant_2_q2 and estudiant_2_q1>estudiant_2_q3):
    if(estudiant_2_q2>estudiant_2_q3):
        q2=estudiant_2_q1+estudiant_2_q2
    else:
        q2=estudiant_2_q1+estudiant_2_q3
elif(estudiant_2_q2>estudiant_2_q1 and estudiant_2_q2>estudiant_2_q3):
    if(estudiant_2_q1>estudiant_2_q3):
        q2=estudiant_2_q1+estudiant_2_q2
    else:
        q2=estudiant_2_q2+estudiant_2_q3
elif(estudiant_2_q3>estudiant_2_q2 and estudiant_2_q3>estudiant_2_q1):
    if(estudiant_2_q2>estudiant_2_q1):
        q2=estudiant_2_q3+estudiant_2_q2
    else:
        q2=estudiant_2_q1+estudiant_2_q3
if(q2==q):
    print("Els dos tenen la mateixa nota final", q2)
elif(q2>q):
    print("L'estudiant 2 té més nota que el 1", q2)
else:
    print("L'estudiant 1 té més nota que el 2", q)
    