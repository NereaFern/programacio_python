#P04Area_total_i_volum_rectangle_pag25.py
'''Dadas las tres dimensiones de un bloque rectangular calcule y muestre su área total y
su volumen'''
#Demanar valors de variables
llargada = float(input("Escrigui el valor de la llargada del bloc en cm a continuació: "))
amplada = float(input("Escrigui el valor de l'amplada del bloc en cm a continuació: "))
profunditat = float(input("Escrigui el valor de la llargada del bloc en cm a continuació: "))

#Calcular el volum i àrea
v = llargada * amplada * profunditat
a = 2 * llargada * profunditat + 2 * amplada * llargada + 2 * amplada * profunditat
print("El volum és de" , v , "cm3")
print("L'àrea és de" , a , "cm2")