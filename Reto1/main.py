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
from funcionesReto1 import *
estudiantes = {}
listaAlumnos = []
listaNotas = []
listaNotasAlumno = []

while True:
    entrada = input(f"Elige una opcion:\n1. Agregar Alumno.\n2. Borrar Alumno.\n3. Consultar Alumnos Aprobados.\n4. Buscar alumno.\n5. Ver todos los alumnos\n6. Salir.\n ")
    entrada = entrada.lower()



    if entrada == "1" or entrada == "agregar alumno":
        while True:
            alumno = input("Introduce el nombre del alumno: ")
            if alumno == "":
                break
            
            notas = input("introduce las notas del alumno: ")
            agregacionDeNotas(notas)
                

            
            listaAlumnos.append(alumno)
            listaNotas.append(listaNotasAlumno)
            estudiantes[alumno] = listaNotasAlumno
            listaNotasAlumno = []

    elif entrada == "2" or entrada == "borrar alumno":
        alumnoAEliminar = input("Inserte el nombre del alumno que quiera borrar: ")
        del estudiantes[alumnoAEliminar]
        print( f"El alumno {alumnoAEliminar} ha sido borrado del registro.")


    elif entrada == "3" or entrada == "consultar alumnos aprobados":
        alumnosAprobados = []
        for alumno, notas in estudiantes.items():
            if sacarMedia(notas) > 6:
                alumnosAprobados.append(alumno)

        print(f"Los alumnos aprobados son {alumnosAprobados}")


    elif entrada == "4" or entrada == "buscar alumno":
        alumnoAconsultar = input("Introduzca el nombre del alumno: ")
        print(f"Alumno: {alumnoAconsultar}.\nNotas: {estudiantes[alumnoAconsultar]}")

    elif entrada == "5" or entrada == "ver todo los alumnos":
        for al, marks in estudiantes.items():
            print(f"Alumno: {al}  Nota Media: {sacarMedia(marks)}")    
    
    elif entrada == "6" or entrada == "salir":
        print(f"Gracias por usar nuestro programa!\nSaliendo...")
        break
   