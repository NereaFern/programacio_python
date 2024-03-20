#Programació_nombres_primers_while.py
n = int(input("Escrigui un nombre sencer ="))
x=2
if(n==1 or n==2):
    print(n, "és un nombre primer")
while x<n:
    if n%x==0:
        print(n, "no és un nombre primer")
        break
    else:
        x=x+1
if n==x:
    print(n, "és primer")
    
    
    
    
