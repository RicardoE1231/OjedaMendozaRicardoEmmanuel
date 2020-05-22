""" Ejercicio 3
    No. Control: 19161369
    Alumno: Ojeda Medoza Ricardo Emmanuel
    NUMEROS FEOS
"""
continuar = True
while(continuar) : 
    x = 0
    nVeces = 0
    num = 0 
    contador = 0
    nVeces = int (input("Ingresa un numero "))
    contador = nVeces
    if nVeces != 0 :
        while (nVeces>0) :
                num +=1 
                x = num
                while (x%2 == 0):#Verificando si el residuo  2 is igual que 0.
                    x = x / 2
                while (x%3 == 0):#Verificando si el residuo  2 is igual que 0.
                    x = x / 3
                while (x%5 == 0):#Verificando si el residuo  5 is igual que 0.
                    x = x / 5
                #Despues de todas las divisiones si el numero es igual a 1 es un numero feo
                if x == 1:
                    contador -= 1
                    nVeces -= 1
                if contador == 0 : 
                    print(num)     
    elif nVeces <= 0 :
        print("El programa termino...")  
        continuar = False           