print("Programa de evalución de notas de alumnos")

notaAlumno= input("Introduce la nota del alumno") #acceso por teclado

def evaluacion(nota):
    valoracion="aprobado"
    if nota < 5:
        valoracion="suspenso"
    return valoracion

print(evaluacion(int(notaAlumno))) #conversion de cadena a entero

print("verificacion de acceso")

edad_usuario=int(input("Introduce tu edad, por favor: "))

if edad_usuario < 18:
    print("No puedes pasar")
elif edad_usuario > 110:
    print("Edad Incorrecta")
else:    
    print("puedes pasar")

salario_presidente = int(input("Introduce salario presidente "))
print("Salario presidente: " + str(salario_presidente))

salario_director = int(input("Introduce salario director "))
print("Salario director: " + str(salario_director))

salario_administrativo = int(input("Introduce salario administrativo "))
print("Salario administrativo: " + str(salario_administrativo))              

if salario_administrativo < salario_director < salario_presidente:
    print("todo va bien")
else:
    print("algo va mal")

#40km, 2 hermano y salario familiar 20000
print("Programa de becas 2021")    
distancia_colegio = int(input("Introduce distancia "))
print("Distancia: " + str(distancia_colegio))

hermano = int(input("Introduce hermanos "))
print("Hermanos: " + str(hermano))

salario_familiar = int(input("Introduce salario familiar "))
print("Salario: " + str(salario_familiar))

if distancia_colegio>40 and hermano>2 or salario_familiar<=20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")


print("Asignaturas Optativas 2021")
print("Informatica Grafica - Pruebas de Software - Usabilidad y Accesibilidad")
asignatura = input("Esbribe la asignatura: ");

if asignatura in ("Informatica Grafica", "Pruebas de Software", "Usabilidad y Accesibilidad"):
    print("Asignatura elegida: " + asignatura)
else:
    print("Debe elegir una asignatura de la lista")

    
