""" Ejercicio 2
    No. Control: 19161369
    Alumno: Ojeda Medoza Ricardo Emmanuel
"""

num = int (input("Ingresa un numero: "))
suma = 0
if num>0 :
    for i in range (1, num + 1) :
        suma += i
    print(suma)        
elif num<0 or num==0 :
    print("Ingresa Un Numero Mayor Que 0!!")