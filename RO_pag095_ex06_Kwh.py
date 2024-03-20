#R0_Pag_95_ex_6_Kwh.py
'''6. Lea la cantidad de Kw que ha consumido una familia y el precio por Kw. Si la cantidad
es mayor a 700, incremente el precio en 5% para el exceso de Kw sobre 700. Muestre el
valor total a pagar.
'''

kwh = float(input("Escrigui la quantitat de Kwh que ha consumit la familia: "))
preu = float(input("Ara escrigui el preu del Kwh: "))

if(kwh>700):
    preu_total = (preu*kwh)*1.05
else:
    preu_total = preu*kwh
print("El preu que haureu de pagar és de", preu_total, "€")