#RO_Pag_148_ex_29_joc_noms.py
'''29.- En un juego se debe asignar a cada persona un número mágico que se obtiene con la
siguiente regla: Se suman los dígitos de la fecha de nacimiento y se suman nuevamente
los dígitos del resultado hasta obtener obtener un solo dígito, como en el siguiente
ejemplo:'''
#Inicialitzem variables
d=int(input("Escrigui el dia del seu aniversari: "))
m=int(input("Escrigui el més del seu aniversari: "))
a=int(iput("Escrigui el any en el que va neixer: "))
t=0
i=0
t=d+m+a
llista=[1000,100,10,1]
for i in range llista:
    i=