#Pag_41_ex_2.py
'''2. Lea los votos de n personas en una consulta. Cada voto es un número 0, o 1
correspondiente a la opción a favor (1) o en contra (0). Al inicio lea el valor de n para
especificar la cantidad de ciclos que se realizarán. Muestre el resultado de la consulta.'''
#Assignar el valor de les variables
n = int(input("Introdueixi el nombre de vots: "))
opcio_favor = 0
opcio_contra = 0
vot = 0
#Començament del programa
for i in range(1,n+1):
    vot = print("Posi si està a favor (1) o en contra (0) :")
    vot = int(input())
    if(vot==1):
        opcio_favor = opcio_favor+1
    if(vot==0):
        opcio_contra = opcio_contra+1
print("Hi han", opcio_favor, "vots a favor i", opcio_contra, "vots en contra")
    