""" Ejercicio 5
    No. Control: 19161369
    Alumno: Ojeda Medoza Ricardo Emmanuel
    Numeros Perfectos
"""

nVeces = int(input("Cuantos numeros desea comprobar? "))
es_feo = False
salida = " = 1"
while nVeces>0 :
    num = int(input("Ingresa un numero mayor a cero: "))
    if num==0 :
        print("Ingresa un numero mayor que cero!!")
    elif num<0 :
        nVeces = 0
        print("Ciclo terminado error!")    
    elif num>0 :
        nPerfecto = 0
        for i in range(1, num) :
            if (num%i == 0) :
                nPerfecto += i
                if i > 1 : salida += " + " + str(i)         
        if nPerfecto==num :
            print(str(num) + " Si es un numero perfecto!")
            print(str(num) + salida)
            
        else:
            print(str(num) + " No es un numero perfecto!")
    nVeces -= 1        
