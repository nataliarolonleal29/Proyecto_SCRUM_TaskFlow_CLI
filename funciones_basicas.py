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
    
tareas = []

def listar_tareas (tareas):
    if len(tareas) == 0:
        print("No hay tareas registradas.")
    else:
        print("Lista de tareas: ")
        for i, tarea in enumerate(tareas, start=1):
            print(i, "-", tarea)


from data import load_data, save_data

def eliminar_tareas (tareas):
    data = load_data()
    if len(tareas) == 0:
        print("No hay tareas registradas aún.")
    else:
        print("Lista de tareas: ")
        for i, tarea in enumerate(tareas, start=1):
            print(i, "-", tarea)
        opcion = input("Indique cuál tarea desea eliminar.")
        if opcion == "tarea":
            data ["tareas"].remove(tarea)
            save_data(data)
            print("Tarea eliminada.")

