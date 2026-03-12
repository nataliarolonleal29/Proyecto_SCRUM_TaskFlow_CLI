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
    