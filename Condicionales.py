print("Programa de evalución de notas de alumnos")

notaAlumno= input("Introduce la nota del alumno") #acceso por teclado

def evaluacion(nota):
    valoracion="aprobado"
    if nota < 5:
        valoracion="suspenso"
    return valoracion

print(evaluacion(int(notaAlumno))) #conversion de cadena a entero
