def agregacionDeNotas(*notas):
     for nota in notas:
        int(nota)
        listaNotasAlumno.append(nota)

def sacarMedia(notasdelalumno):
    contador = 0
    acum = 0
    listaNumerica = notasdelalumno[0].split(",")
    for n in listaNumerica :
        acum += int(n)
        contador += 1

    notaMedia = acum / contador 
    return notaMedia   





