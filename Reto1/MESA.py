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



