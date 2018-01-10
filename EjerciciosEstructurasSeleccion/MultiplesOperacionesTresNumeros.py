print("######Multiples Operaciones con Tres Numeros######")
num1 = float(input("Ingresar primer numero"))
num2 = float(input("Ingresar segundo numero"))
num3 = float(input("Ingresar tercer numero"))

if num1 == num2:
    if num1 == num3:
        print("Los 3 numeros son iguales, no se efectuara operaciones")
    else:
        print("Dos numeros son iguales, se efectura multiplicacion con el diferente: ", num1 * num3)
elif num1 == num3:
    print("Dos numeros son iguales, se efectura multiplicacion con el diferente: ", num1 * num2)
elif num3 == num2:
    print("Dos numeros son iguales, se efectura multiplicacion con el diferente: ", num2 * num1)
elif num1 > num2:
    if num1 > num3:
        if num2 < num3:
            print("Diferencia del mayor - menor: ", (num1 -num2))
            print("Diferencia del medio - menor: ", (num3 - num2))
        else:
            print("Diferencia del mayor - menor: ", (num1 - num3))
            print("Diferencia del medio - menor: ", (num2 - num3))
    else:
        print("Diferencia del mayor - menor: ", (num3 - num2))
        print("Diferencia del medio - menor: ", (num1 - num2))
else:
    if num2 > num3:
        if num1 > num3:
            print("Diferencia del mayor - menor: ", (num2 - num3))
            print("Diferencia del medio - menor: ", (num1 - num3))
        else:
            print("Diferencia del mayor - menor: ", (num2 - num1))
            print("Diferencia del medio - menor: ", (num3 - num1))
    else:
        print("Diferencia del mayor - menor: ", (num3 - num1))
        print("Diferencia del medio - menor: ", (num2 - num1))