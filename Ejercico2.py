""" Ejercicio 2
    No. Control: 19161369
    Alumno: Ojeda Medoza Ricardo Emmanuel
"""

num = int (input("Ingresa un numero: "))
suma = 0
if abs(num)>0 and abs(num)<(10^4) :
    if num>0 :
        for i in range (1, num + 1) :
            suma += i
    elif num<0 :
        for i in range (-1, num - 1, -1) :
            suma += i
    print(suma)             
elif num==0 :
    print("Ingresa Un Numero Mayor Que 0!!")
elif abs(num)>(10^4):
    print("Ingresa Un Numero Mayor Que 0!!")    