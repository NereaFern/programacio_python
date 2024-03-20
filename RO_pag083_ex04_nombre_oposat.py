#RO_pag_83_ex_4_nombre_oposat.py
'''4. Dado un número entero de tres cifras. Muestre el mismo número pero con las cifras en
orden opuesto.'''
nombre=int(input("Escrigui el nombre enter de tres xifres: "))

xifra3= nombre//100
xifra2= (nombre-(xifra3)*100)//10
print(xifra2)
xifra1= nombre-10*(10*xifra3+xifra2)
if(nombre>1):
    nombre = (xifra1)*100+xifra2*10+xifra3
else:
    xifra3 *=(-1)
    print(xifra3, xifra2, xifra1)
    nombre= -1*(xifra1*100+xifra2*10+xifra3)
print(nombre)