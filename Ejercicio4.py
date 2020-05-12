""" Ejercicio 4
    No. Control: 19161369
    Alumno: Ojeda Medoza Ricardo Emmanuel
"""

nVeces = int(input("Cuantos numeros deseas comprobar? "))
x = 0
while nVeces>0 :
    x = 1
    nPuntos = int(input("Ingresa el numero de puntos: "))
    while (nPuntos>1) :
        x = x*2
        nPuntos -= 1
    print(x)    
    nVeces -= 1    