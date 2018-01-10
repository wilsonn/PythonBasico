print("##### Menor de Cuatro numeros #####")

num1 = float(input("Ingresar primer numero"))
num2 = float(input("Ingresar segundo numero"))
num3 = float(input("Ingresar tercer numero"))
num4 = float(input("Ingresar cuarto numero"))

if num1 < num2:
    if num1 < num3:
        if num1 < num4:
            print("El numero menor es: ", num1)
        else:
            print("El numero menor es: ", num4)
    else:
        if num3 < num4:
            print("El numero menor es: ", num3)
        else:
            print("El numero menor es: ", num4)
else:
    if num2 < num3:
        if num2 < num4:
            print("El numero menor es: ", num2)
        else:
            print("El numero menor es: ", num4)
    else:
        if num3 < num4:
            print("El numero menor es: ", num3)
        else:
            print("El numero menor es: ", num4)
