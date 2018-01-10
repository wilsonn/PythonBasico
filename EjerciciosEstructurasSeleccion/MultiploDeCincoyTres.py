print("##### Multiplo de 5 o 3 #####")
num1 = int(input("Ingrese un numero: "))

if num1%3 == 0 and num1%5 == 0:
    print("Es multiplo de 3 y 5")
elif num1%3 == 0:
    print("Es multiplo de 3")
elif num1%5 == 0:
    print("Es multiplo de 5")
else:
    print("No es multiplo de 3 o 5")
