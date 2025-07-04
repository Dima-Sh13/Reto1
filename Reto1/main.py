"""
Desarrolla un programa en Python que permita registrar y gestionar las notas de
varios estudiantes. El sistema debe cumplir las siguientes funcionalidades básicas:
● Agregar estudiantes: El usuario podrá ingresar el nombre de un estudiante y sus
tres notas (valores entre 0 y 10).
● Quitar estudiantes: El usuario podrá eliminar un registro de un estudiante dado el
nombre.
● Mostrar estudiantes aprobados: Mostrar solo los estudiantes cuyo promedio sea
mayor o igual a 6.
● Buscar estudiante por nombre y mostrar su promedio.
● Mostrar todos los estudiantes con sus promedios.
● Salir del programa.
● Subir el programa a su repositorio remoto GIT.
"""
estudiantes = {}
listaAlumnos = []
listaNotas = []
listaNotasAlumno = []
while True:
    alumno = input("Introduce el nombre del alumno: ")
    if alumno == "":
        break
    notas = input("introduce las notas del alumno: ")
    for nota in notas:
        listaNotasAlumno.append(nota)
        

        
    listaAlumnos.append(alumno)
    listaNotas.append(listaNotasAlumno)
    listaNotasAlumno = []

    