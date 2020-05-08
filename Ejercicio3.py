""" Ejercicio 3
    No. Control: 19161369
    Alumno: Ojeda Medoza Ricardo Emmanuel
    NUMEROS FEOS
"""
nVeces = int (input("Cuantos numeros deseas comprobar? "))
while (nVeces>0) :
    num = int (input ("Ingresa un numero: "))
    x = num
    while (x%2 == 0):#Verificando si el residuo  2 is igual que 0.
        x = x / 2
    while (x%3 == 0):#Verificando si el residuo  2 is igual que 0.
        x = x / 3
    while (x%5 == 0):#Verificando si el residuo  5 is igual que 0.
        x = x / 5
    #Despues de todas las divisiones si el numero es igual a 1 es un numero feo
    if x == 1:
        print(str(num) + " Si es un numero feo")
    elif x != 1:
        print(str(num) + " No es un numero feo")
    nVeces -= 1
    print("=====================================")
    