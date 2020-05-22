""" Ejercicio 4
    No. Control: 19161369
    Alumno: Ojeda Medoza Ricardo Emmanuel
"""
from math import factorial
def numero_combinaciones(m, n):
    return factorial(m) // (factorial(n) * factorial(m - n))

nVeces = int(input("Cuantos numeros deseas comprobar? "))
x = 0
while nVeces>0 :
    x = 1
    n = int(input("Ingresa el numero de puntos: "))
    if n == 0 or n == 1 :
        print(1)
    elif n >= 4 : 
        nRegiones  =  numero_combinaciones(n, 4)
        nRegiones  +=  numero_combinaciones(n, 2)
        print(nRegiones+1)
    else :
        nRegiones = 1
        for i in range(1, n-1) : 
            nRegiones += nRegiones*2    
        print(nRegiones+1)           

    nVeces -= 1   
               

