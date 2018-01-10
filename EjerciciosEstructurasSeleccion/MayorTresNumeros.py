print("#####Mayor de Tres Numeros#####")
numA = float(input("Ingresa primer numero: "))
numB = float(input("Ingresa segundo numero:"))
numC = float(input("Ingresa tercer numero:"))

if numA > numB:
    if numA > numC:
        print("El numero mayor es: ",numA)
    else:
        print("El numero mayor es: ",numC)
else:
    if numB > numC:
        print("El numero mayor es: ", numB)
    else:
        print("El numero mayor es: ", numC)
