from math import pi
def quadrat(a):
    A=a*a
    P=a*4
    print("Àrea = ", A)
    print("Perímetre = ", P)
def triangle(a,b,c,h):
    A= b*h/2
    P=a+b+c
    print("Àrea = ", A)
    print("Perímetre = ", P)
def rectangle(a,b):
    A=b*a
    P=2*(a+b)
    print("Àrea = ", A)
    print("Perímetre = ", P)
def paralelogram(b,h,a):
    A=b*h
    P=2*(a+b)
    print("Àrea = ", A)
    print("Perímetre = ", P)
def romb(D,a,d):
    A=D*d/2
    P=4*a
    print("Àrea = ", A)
    print("Perímetre = ", P)
def estel(D,a,d,b):
    A=d*D/2
    P=2*(b*a)
def trapezi(a,b,B,h,c):
    A=(B+b)*2/h
    P=B+b+a+c
    print("Àrea = ", A)
    print("Perímetre = ", P)
    
def cercle(r):
    A= pi*pow(r,2)
    P=2*pi*r
    print("Àrea = ", A)
    print("Perímetre = ", P)
def poligon_regular(a,b,n):
    P=n*b
    A=P*a/2
def corona_circular(R,r):
    A=pi*(pow(R,2)-pow(r,2))
    print("Àrea = ", A)
def sector_circular(R,n):
    A= pi*pow(R,2)*n/360
    print("Àrea = ", A)
def cub(a):
    A= 6*pow(a,2)
    V= pow(a,3)
    print("Volum = ", V)
    print("Àrea = ", A)
def cilindre(R,h):
    A= 2*pi +R*(h+R)
    V= pi*pow(R,2)*h
    print("Volum = ", V)
    print("Àrea = ", A)
def ortoedre(a,b,c):
    A= 2*(a*b+a*c+b*c)
    V=a*b*c
    print("Volum = ", V)
    print("Àrea = ", A)
def prisma_recte(P,a,h,Ab):
    A= P*(a+h)
    V= Ab*h
def con(h,g,R):
    A= pi*R*(R+g)
    v= pi*pow(R,2)*h/3
    print("Volum = ", V)
    print("Àrea = ", A)
def tronc_de_con(h,g,R,r):
    A= pi*(g*(R+r)+pow(r,2)+pow(R,2))
    V= pi*h*(pow(R,2)+pow(r,2)+R*r)
    print("Volum = ", V)
    print("Àrea = ", A)
def esfera(R):
    A= 4*pi*pow(R,2)
    V= 4*pi*pow(R,3)/3
    print("Volum = ", V)
    print("Àrea = ", A)
def piramide(h,a,b,P,ab):
    A= P*(a+b)/2
    V= ab*h/3
    print("Volum = ", V)
    print("Àrea = ", A)
def tetaedre_rectangular(a):
    A= sqrt(3)*pow(a,2)
    V= sqrt(2)*pow(a,3)/12
def octaedre_regular(a):
    A= 2*sqrt(3)*pow(a,2)
    V= sqrt(2)*pow(a,3)/3
def tronc_piramide(h,P,Pp,a,Ab,Abb):
    A= (P+Pp)/2*a+Ab+Abb
    V= (Ab+Abb+sqrt(Ab*Abb))*h
    print("Volum = ", V)
    print("Àrea = ", A)
def casquet_esféric(h,R):
    A= 2*pi*R*h
    V= pi*pow(h,2)*(3*R-h)/3
    print("Volum = ", V)
    print("Àrea = ", A)
def huso_cuña_esferica(n,R):
    A= 4*pi*pow(R,2)*n/360
    V= 4*pi*pow(R,3)*n/360*3
    print("Volum = ", V)
    print("Àrea = ", A)
def zona_o_segment_esfèric(R,h,r,rr):
    A= 2*pi*R*h
    V= pi*h*(pow(h,2)+3*pow(r,2)+3*pow(rr,2))/6
    print("Volum = ", V)
    print("Àrea = ", A)

# Programa principal main
print("")
print("Càlcul d'arees i perimetres")
print("1. Quadrat")
print("2. Triangle")
print("3. Rectangle")
print("4. Paralelogram")
print("5. Rombe")
print("6. Estel")
print("7. Trapezi")
print("8. Cercle")
print("9. Poligon regular")
print("10. Corona regular")
print("11. Sector circular")
print("12. Cub")
print("13. Cilindre")
print("14. Ortoedre")
print("15. Prisma recte")
print("16. Con")
print("17. Con de tronc")
print("18. Esfera")
print("19. Piramide")
print("20. Tetaedre regular")
print("21. Octaedre regular")
print("22. Tronc de periàmide")
print("23. Casquet esfèric")
print("24. Huso: Cunya esferica")
print("25. Zona o segment esfèric")
opcio=int(input("Escrigui que vol calcular: "))
if opcio==1:
    a=float(input("Costat a: " ))
    quadrat(a)
if opcio==2:
    a=float(input("Costat a: "))
    b=float(input("Costat b: "))
    c=float(input("c: "))
    h=float(input("h: "))
    triangle(a,b,c,h)
if opcio==3:
    a=float(input("Costat a: "))
    b= float(input("Costat b: "))
    rectangle(a,b)
if opcio==4:
    b=float(input("b: "))
    h=float(input("h: "))
    a=float(input("a: "))
if opcio==5:
    D=float(input("D: "))
    a=float(input("a: "))
    d=float(input("d :"))
    romb(D,a,d)