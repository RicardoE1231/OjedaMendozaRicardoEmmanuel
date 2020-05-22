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
    nRegiones  =  numero_combinaciones(n, 4)
    nRegiones  +=  numero_combinaciones(n, 2)
    print(nRegiones+1)

