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