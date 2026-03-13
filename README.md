# Proyecto SCRUM con TaskFlow CLI

### Integrantes del equipo:
### Juan David Arias Patiño - Scrum Master
### Natalia Rolón Leal - Product Owner
### Ruben Santiago Carreño Torres - Developer
### Keyner Andres Sepulveda Torres - Developer

## Descripción del proyecto:
TaskFlow CLI es una aplicación sencilla desarrollada en Python que funciona desde la terminal y permite gestionar tareas de forma rápida mediante comandos para crear, listar, completar y eliminar tareas, guardando la información en un archivo JSON.

Este proyecto se desarrolla como un Producto Mínimo Viable (MVP) y tiene como objetivo aplicar el marco de trabajo SCRUM, organizando el desarrollo mediante roles, historias de usuario, sprints y un tablero Kanban. De esta manera, se busca tanto crear una herramienta funcional como evidenciar el uso de metodologías ágiles durante el proceso de desarrollo.


## Planteamiento del problema:
Actualmente, muchas personas tienen dificultades para organizar sus tareas académicas y personales, ya que suelen usar métodos poco estructurados como notas sueltas o recordatorios informales. Esto puede provocar desorden, baja productividad y dificultades para priorizar actividades importantes.

Aunque existen aplicaciones de gestión de tareas, muchas son demasiado complejas o requieren conexión a internet, lo que las hace poco prácticas para usuarios que prefieren herramientas simples desde la terminal.

Además, en los proyectos de desarrollo de software es común que los estudiantes trabajen sin una metodología clara, lo que puede generar desorganización y poca claridad en el progreso del proyecto.

Por esta razón, surge la necesidad de desarrollar TaskFlow CLI, una aplicación sencilla en Python para gestionar tareas desde la consola, que al mismo tiempo permita aplicar el marco de trabajo SCRUM para organizar el desarrollo del proyecto de manera colaborativa, planificada y con mejora continua.

## Objetivo del sistema:
Desarrollar una aplicación de consola en Python llamada TaskFlow CLI que permita gestionar tareas de manera sencilla y organizada, brindando funciones básicas como crear, listar, completar y eliminar tareas, además de guardar la información en un archivo JSON para mantener su persistencia. Al mismo tiempo, el proyecto busca aplicar el marco de trabajo SCRUM para planificar, organizar y desarrollar el sistema de forma colaborativa, evidenciando el uso de metodologías ágiles durante el proceso de desarrollo del producto mínimo viable (MVP).

## Solución Propuesta
TaskFlow CLI surge como una herramienta sencilla y eficiente que evita las dificultades de las interfaces gráficas pesadas. La solución consiste en una interfaz de línea de comandos (CLI) que permite al usuario interactuar con su lista de tareas mediante verbos directos. Al utilizar un archivo JSON para la persistencia, garantizamos que los datos sobrevivan a cada sesión sin necesidad de configurar bases de datos complejas, ofreciendo una experiencia de "instalar y usar" inmediata.

## Funcionalidades Implementadas
- Creación de Tareas: Registro rápido de nuevas actividades con una descripción clara.

- Visualización Dinámica: Listado organizado de todas las tareas pendientes y completadas.

- Edición de tareas: Se realizó una función para editar cualquier tipo de dato y/o información de cada tarea.

- Eliminación Selectiva: Limpieza del historial eliminando tareas obsoletas o erróneas.

- Persistencia Automática: Guardado y carga de datos en tiempo real mediante formato JSON.

## Tecnologías Implementadas
- Python: Lenguaje principal para la lógica del proyecto.

- JSON: Formato estándar para el almacenamiento de datos local.

- VS Code Terminal y Github: Para la interacción fluida con el sistema operativo y la terminal.

## Instrucciones de Instalación y Ejecución
1. Clonar el repositorio:
git clone https://github.com/nataliarolonleal29/Proyecto_SCRUM_TaskFlow_CLI.git

2. Ejecutar la aplicación:
No requiere dependencias externas. Ejecuta directamente con Python:
python app.py

## Metodología SCRUM
Para el desarrollo de este proyecto, se aplicó el marco de trabajo SCRUM de la siguiente manera:

- Roles: Se definieron responsabilidades claras (Product Owner, Scrum Master y Developers) para asegurar la visión del producto y la agilidad del proceso.

- Product Backlog: Se transformaron las necesidades del usuario en historias de usuario técnicas, priorizadas por valor de negocio.

- Sprints: El desarrollo se dividió en iteraciones cortas, enfocándose en entregar un incremento funcional al finalizar cada una.

- Tablero Kanban: Se utilizó una herramienta visual (To Do, In Progress, Done) con GitHub Projects, para monitorear el flujo de trabajo en tiempo real y detectar posibles problemas.

## Reflexión Final
El desarrollo de TaskFlow CLI permitió validar que la simplicidad técnica, apoyada en una metodología ágil como SCRUM, reduce significativamente el desorden y la baja productividad. El aprendizaje principal fue la importancia de la planificación iterativa: empezar con un MVP funcional permitió identificar mejoras necesarias (como la validación de entradas) antes de añadir complejidad innecesaria. Este proyecto reafirma que el orden en el proceso de desarrollo es tan crucial como la calidad del código para alcanzar el éxito y la mejora continua.

## Comados del programa

### Iniciar el programa
1. Ejecuta el archivo principal del programa en Python.
2. Al iniciarlo aparecerá un menú con las diferentes funciones del sistema.

```
--menu tareas--
1. Crear tarea
2. Editar
3. Listar tarea
4. Marcar tarea como completada
5. Eliminar tarea
6. Salir
```

3. El usuario debe ingresar el número de la opción que desea utilizar.

---

## Funciones del Programa

### Crear una tarea
1. En el menú principal selecciona la opción **1**.
2. El programa mostrará el mensaje de bienvenida a la sección de creación de tareas.
3. Ingresa el **título de la tarea**.
4. Ingresa una **descripción de la tarea**.
5. Escribe la **fecha de la tarea** en formato `DIA/MES/AÑO`.
6. Ingresa la **hora de inicio de la tarea**.
7. Ingresa la **hora de finalización de la tarea**.
8. La tarea se guardará con el estado **Programada**.
9. El sistema mostrará el mensaje **"Tarea programada correctamente"**.

---

### Editar una tarea
1. En el menú principal selecciona la opción **2**.
2. El sistema mostrará los títulos de todas las tareas registradas.
3. Escribe el nombre de la tarea que deseas editar.
4. Luego aparecerá un menú con las opciones de edición:

```
1. Titulo
2. Descripcion
3. Fecha
4. Hora de inicio
5. Hora de fin
```

5. Selecciona el número correspondiente al campo que deseas modificar.
6. Ingresa el nuevo valor del campo seleccionado.
7. El programa guardará los cambios.
8. Se mostrará el mensaje **"Datos actualizados correctamente"**.

---

### Listar tareas
1. En el menú principal selecciona la opción **3**.
2. El sistema verificará si existen tareas registradas.
3. Si no hay tareas, mostrará el mensaje:

```
No hay tareas registradas.
```

4. Si existen tareas, el sistema mostrará todas las tareas guardadas con su información.

---

### Marcar una tarea como completada
1. En el menú principal selecciona la opción **4**.
2. El sistema mostrará las tareas que tienen estado **Programada**.
3. Escribe el nombre de la tarea que deseas actualizar.
4. El sistema cambiará el estado de la tarea a **Completada**.
5. Se mostrará el mensaje **"Estado de la tarea actualizada satisfactoriamente"**.

---

### Eliminar una tarea
1. En el menú principal selecciona la opción **5**.
2. El sistema mostrará la lista de tareas registradas.
3. Escribe el nombre de la tarea que deseas eliminar.
4. El sistema eliminará la tarea del sistema.
5. Se mostrará el mensaje **"Tarea eliminada"**.

---

### Salir del programa
1. En el menú principal selecciona la opción **6**.
2. Antes de salir, el sistema preguntará si deseas dejar una opinión.

```
1. Sí
2. No
```

3. Si seleccionas **1**, el sistema solicitará:
   - Nombre de usuario
   - Error o sugerencia
   - Por qué es importante arreglar o añadir esa mejora

4. Esta información se guardará como **historia de usuario**.
5. Finalmente el sistema mostrará el mensaje **"Saliendo del programa..."** y el programa terminará.