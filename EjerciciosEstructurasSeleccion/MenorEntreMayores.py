num1 = int(input("Ingresar primer numero"))
num2 = int(input("Ingresar segundo numero"))
num3 = int(input("Ingresar tercer numero"))

if num1 > num2:
    if num1 > num3:
        if num2 < num3:
            print("Si a= ", num1," ,b= ", num2," ,c= ", num3, ". Entonces sera: [",num3," ,",num2,", ", num1,"]")
        else:
            print("Si a= ", num1, " ,b= ", num2, " ,c= ", num3, ". Entonces sera: [", num2, " ,", num3, ", ", num1, "]")
    else:
        print("Si a= ", num1, " ,b= ", num2, " ,c= ", num3, ". Entonces sera: [", num1, " ,", num2, ", ", num3, "]")
else:
    if num2 > num3:
        if num1 > num3:
            print("Si a= ", num1, " ,b= ", num2, " ,c= ", num3, ". Entonces sera: [", num1, " ,", num3, ", ", num2, "]")
        else:
            print("Si a= ", num1, " ,b= ", num2, " ,c= ", num3, ". Entonces sera: [", num3, " ,", num1, ", ", num2, "]")
    else:
        print("Si a= ", num1, " ,b= ", num2, " ,c= ", num3, ". Entonces sera: [", num2, " ,", num1, ", ", num3, "]")