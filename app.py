from funciones_basicas import crear_tarea
bool = True

while bool == True:
    print("--menu tareas--")
    print("1. crear tarea")
    print("2. Editar")
    print("3. listar tarea")
    print("4. marcar tarea")
    print("5. eliminar tarea")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("Bienvenido a la seccion de creacion de una nueva tarea")
        print("------------------------------------------------------")
        crear_tarea()

    elif opcion == "2":
        print("")

    elif opcion == "3":
        print("")

    elif opcion == "3":
        print("")

    elif opcion == "4":
        print ("")
    
    elif opcion == "5":
        print("Saliendo del programa...")
        bool = False