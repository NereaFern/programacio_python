#RO_Pag_180_ex_13_convertir.py
'''13. Escriba una librería o módulo con el nombre convertir que contenga dos funciones:
 [r,fi]=polar(x, y) Recibe las coordenadas cartesianas x,y y entrega las
 coordenadas polares r, t
 [x,y]=cartesiana(r, t) Recibe las coordenadas polares r, t y entrega las
 coordenadas cartesianas x, y'''
from math import*
def polar(x,y):
    r=sqrt(pow(x,2)+pow(y,2))
    fi=(atan(x/y))*180/pi
    return (r,fi)
def cartesianes(r,fi):
    fi=fi*pi/180
    x=cos(fi)*r
    y=sin(fi)*r
    return (x,y)
import RO_Pag_180_ex_13_convertir
print("CONVERTIR POLARS A CARTESIANES O CARTESIANES A POLARA")
print("1. Convertir a polars")
print("2. Convertir a cartesianes")
print("3.Sortir del programa")
opcio=int(input("Escrigui el número del que vol fer: "))
if opcio==1:
    x=float(input("Escrgui el valor de x: "))
    y=float(input("Escrigui el valor de y: "))
    print(polar(x,y))
elif opcio==2:
    r=float(input("Escrigui el modul del vector :"))
    fi=float(input("Escrigui l'angle: "))
    print(cartesianes(r,fi))
else:
    print("Has sortit del programa")
