from data import load_data, save_data

def crear_tarea ():
    data = load_data()
    tarea = {
        "titulo" : input("Titulo de la tarea: "),
        "descripcion": input("Descripción de la tarea: "),
        "fecha": input("Fecha: DIA/MES/AÑO: "),
        "hora_de_inicio": input("Hora de inicio: "),
        "hora_de_fin": input("Hora de fin: "),
        "estado_de_la_tarea": "Programada" 
    }

    data ["tareas"].append(tarea)
    save_data(data)
    print("")
    print("Tarea programada correctamente")
    


def listar_tareas ():
    data = load_data()
    if len(data["tareas"]) == 0:
        print("No hay tareas registradas.")
    else:
        print("Lista de tareas: ")
        for tarea in data["tareas"]:
            print("---------------")
            print(tarea) 


from data import load_data, save_data

def eliminar_tareas ():
    data = load_data()
    if len(data["tareas"]) == 0:
        print("No hay tareas registradas aún.")
    else:
        print("Lista de tareas: ")
        for tarea in data["tareas"]:
            print(tarea["titulo"]) 
        print("-------------------------")
        opcion = input("Escriba el nombre de la tarea que desea eliminar: ")
        for tarea in data["tareas"]:
            if opcion == tarea["titulo"]:
                data["tareas"].remove(tarea)
        
    save_data(data)
    print("----------------")
    print("Tarea eliminada.")

def editar_tarea ():
    data = load_data()
    for tarea in data["tareas"]:
        print(tarea["titulo"])
    print("----------------------------------------------")
    print("Escribe el nombre de la tarea que desea editar")
    seleccion = input(": ")
    for tarea in data["tareas"]:
        if seleccion == tarea["titulo"]:
            print("")
            print("¿Que desea editar de esta tarea?")
            print("1. Titulo")
            print("2. Descripcion")
            print("3. Fecha")
            print("4. Hora de inicio")
            print("5. Hora de fin")
            print("--------------------------------")
            seleccion_dos = input(": ")
            if seleccion_dos == "1":
                nuevoTitulo = input("Nuevo titulo: ")
                tarea["titulo"] = nuevoTitulo
            elif seleccion_dos == "2":
                nuevaDescripcion = input("Nueva descripcion: ")
                tarea["descripcion"] = nuevaDescripcion
            elif seleccion_dos == "3":
                nuevaFecha = input("Nueva fecha: DIA/MES/AÑO: ")
                tarea["fecha"] = nuevaFecha
            elif seleccion_dos == "4":
                nuevaHoraDeInicio = input("Nueva hora de inicio: ")
                tarea["hora_de_inicio"] = nuevaHoraDeInicio
            elif seleccion_dos == "5":
                nuevaHoraDeFin = input("Nueva hora de fin: ")
                tarea["hora_de_fin"] = nuevaHoraDeFin

    save_data(data)
    print("")
    print("Datos actualizados correctamente")

def actualizar_estado ():
    data = load_data()
    for tarea in data["tareas"]:
        if tarea["estado_de_la_tarea"] == "Programada":
            print(tarea["titulo"])
    print("--------------------------------------------------")
    print("Escribe el nombre de la tarea que desea actualizar")
    seleccion = input(": ")
    for tarea in data["tareas"]:
        if tarea["titulo"] == seleccion:
            tarea["estado_de_la_tarea"] = "Completada"

    save_data(data)
    print("")
    print("Estado de la tarea actualizada satisfactoriamente")