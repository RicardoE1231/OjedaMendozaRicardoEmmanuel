""" Ejercicio 1
    No. Control: 19161369
    Alumno: Ojeda Medoza Ricardo Emmanuel
"""
txt = input("Ingresa dos numeros separados por un espacio: ")
if 2 < len(txt) :
    x = txt.split(" ")
    a = int (x[0])
    b = int (x[1])
    suma = a + b
    print(suma)
else :
    print("Datos incorrectos!!")    