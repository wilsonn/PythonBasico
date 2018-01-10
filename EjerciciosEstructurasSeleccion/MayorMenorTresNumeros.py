print("######Mayor y Menor de Tres Numeros######")
num1 = float(input("Ingresar primer numero"))
num2 = float(input("Ingresar segundo numero"))
num3 = float(input("Ingresar tercer numero"))

if num1 > num2:
    if num1 > num3:
        if num2 < num3:
            print("El numero mayor es: ", num1)
            print("El numero menor es: ", num2)
        else:
            print("El numero mayor es: ", num1)
            print("El numero menor es: ", num3)
    else:
        print("El numero mayor es: ", num3)
        print("El numero menor es: ", num2)
else:
    if num2 > num3:
        if num1 > num3:
            print("El numero mayor es: ", num2)
            print("El numero menor es: ", num3)
        else:
            print("El numero mayor es: ", num2)
            print("El numero menor es: ", num1)
    else:
        print("El numero mayor es: ", num3)
        print("El numero menor es: ", num1)