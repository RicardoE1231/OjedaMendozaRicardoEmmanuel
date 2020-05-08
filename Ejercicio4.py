""" Ejercicio 4
    No. Control: 19161369
    Alumno: Ojeda Medoza Ricardo Emmanuel
"""

nVeces = int(input("Cuantos numeros deseas comprobar? "))
while nVeces>0 :
    num = int(input("Ingresa un numero mayor a cero: "))
    if num>0 :
        op1 = (num*num) + num + 2
        op1 = int(op1/2)
        print("Total de regiones: " + str(op1))
    else:
        print("Ingresa un numero mayor que cero!")
    nVeces -= 1    