#RO_Pag_81_ex_6_nota_total.py
'''6. El examen de una materia es el 70% de la nota total. Las lecciones constituyen el 20%
y las tareas el 10% de la nota total. Ingrese como datos la nota del examen calificado
sobre 100 puntos, la nota de una lección calificada sobre 10 puntos, y las notas de tres
tareas calificadas cada una sobre 10 puntos. Calcule la calificación total sobre 100 puntos.
'''
nota_examen=float(input("Escrigui la nota de l'exàmen sobre 100 punts: "))
nota_llicons=float(input("Escrigui la nota de les lliçons sobre 10 punts: "))
nota_feines=float(input("Escrigui la nota de les feines sobre 10 punts: "))

nota_total=nota_examen*0.7+nota_llicons*10*0.2+nota_feines*10*0.1
print("La nota total de l'alumne és de", nota_total, "sobre 100")