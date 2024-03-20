#R0_Pag_146_ex_12_
'''12.- El inventor del juego del ajedréz pidió a su rey que como recompensa le diera por la
primera casilla 2 granos de trigo, por la segunda, 4 granos, por la tercera 8, por la cuarta
16, y así sucesivamente hasta llegar a la casilla 64. El rey aceptó. Suponga que cada Kg.
de trigo consta de 20000 granos de trigo. Si cada tonelada tiene 1000 Kg. describa un
algoritmo para calcular la cantidad de toneladas de trigo que se hubiesen necesitado.'''
y=0
grams=0
while y<64:
    y+=1
    grams=grams+pow(2,y)
print(grams
      ç