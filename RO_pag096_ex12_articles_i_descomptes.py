#R0_Pag_96_ex_12_articles_i_descomptes.py
'''12. Un local vende sus productos con la siguiente promoción. Si compra hasta 5 artículos,
no hay descuento. Si compra más de 5 artículos, pero menos de 10, el precio unitario se
reduce en 5%. Si compra 10 o más artículos, el precio unitario se reduce en 8%. Ingrese
un dato de cantidad y el valor del precio unitario original. Calcule y muestre el valor total a
pagar.'''
n=int(input("Posi el nombre de productes comprats: "))
p=int(input("Posi el preu unitari dels producters: "))

if n<=5:
    p=p*n
elif n>5 and n<10:
    p=p*n*0.95
elif n>=10:
    p=p*n*0.92
print("El que haurà de pagar son", p, "€")