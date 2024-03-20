#P05_qualificació.py

'''El examen de una materia es el 70% de la nota total. Las lecciones constituyen el 20%
y las tareas el 10% de la nota total. Ingrese como datos la nota del examen calificado
sobre 100 puntos, la nota de una lección calificada sobre 10 puntos, y las notas de tres
tareas calificadas cada una sobre 10 puntos. Calcule la calificación total sobre 100 puntos.
'''

#Determinar el valor de les variables
examen = float(input("Incerti nota de l'exàmen sobre 100: "))
llicons = float(input("Incerti nota de les lliçons sobre 10: "))
deures1 = float(input("Incerti nota dels primers deures realitzats sobre 10: "))
deures2 = float(input("Incerti nota dels segons deures realitzats sobre 10: "))
deures3 = float(input("Incerti nota dels tercers deures realitzats sobre 10: "))
#Calcular la qualificació

deures = (deures1+deures2+deures3)/3
deures*=10
llicons*=10
qualificacio = examen*0.7+llicons*0.2+deures*0.1
print("La seva qualificació final serà de:" , round(qualificacio,2) ,"/100")