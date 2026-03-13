from funciones_basicas import crear_tarea, editar_tarea, listar_tareas, eliminar_tareas, actualizar_estado
bool = True

while bool == True:
    print("--menu tareas--")
    print("1. crear tarea")
    print("2. Editar")
    print("3. listar tarea")
    print("4. marcar tarea como completada")
    print("5. eliminar tarea")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("Bienvenido a la seccion de creacion de una nueva tarea")
        print("------------------------------------------------------")
        crear_tarea()

    elif opcion == "2":
        print("Bienvenido a la seccion de edición de tareas")
        print("--------------------------------------------")
        editar_tarea()

    elif opcion == "3":
        print("Bienvenido a la seccion de listar tareas")
        print("----------------------------------------")
        listar_tareas()

    elif opcion == "4":
        print("Bienvenido a la seccion de marcar tarea como completada")
        print("----------------------------------------")
        actualizar_estado()

    elif opcion == "5":
        print("Bienvenido a la seccion de eliminar tareas")
        print("------------------------------------------")
        eliminar_tareas()
    
    elif opcion == "6":
        print("Saliendo del programa...")
        bool = False