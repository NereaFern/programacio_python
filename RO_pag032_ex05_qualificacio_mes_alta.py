#P12_qualificacio_mes_alta.py
'''Dadas las tres calificaciones de un estudiante, encuentre y muestre la calificación mas
alta
*********************************************************'''

#Definir la variable
q1 = float(input("Posar la qualificació 1 de l'estudiant sobre 10: "))
q2 = float(input("Posar la qualificació 2 de l'estudiant sobre 10: "))
q3 = float(input("Posar la qualificació 3 de l'estudiant sobre 10: "))


#Trobar quin és el valor més gran
if(q1>q2):
    if(q1>q3):
        print(f"La seva qualificació més alta és {q1} sobre 10")
elif(q3>q1):
    print(f"La seva qualificació més alta és {q3} sobre 10")
else:
    print(f"La seva qualificació més alta és {q2} sobre 10")
print("FI DE PROGRAMA")