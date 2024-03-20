#P13_creixement_bacteries
'''
En un cultivo se tiene una cantidad inicial de bacterias. Cada día esta cantidad se duplica. 
Determine en que día la cantidad excede a un valor máximo.
'''
#Declaració de variables
bacteris= int(input("Introdueix el nombre de bacteris inicial: "))
bacteris_maxim= int(input("Introdueix el nombre màxim de bacteris: "))
dies = 0

while(bacteris <= bacteris_maxim):
    dies += 1
    bacteris *= 2
print(f'El nombre de dies es {dies} i el nombre de bacteris és de {bacteris}')

