#Gestor de tareas: Una aplicación simple para agregar, eliminar y marcar tareas como completadas.(opcional: añadir un filtro, modificar tareas)
from Funciones import Funciones

Lista_tareas = Funciones() 


print('====================== Bienvenido al gestor de tareas ======================')

opcion = ''

while opcion != '5':
    print('1. Añadir tarea.')
    print('2. Completar tarea.')
    print('3. Eliminar tarea.')
    print('4. Mostrar tareas.')
    print('5. Salir del gestor de tareas.')
    opcion = input('Seleccione una opción del menú:')
    
    if opcion == '1':
        Lista_tareas.añadir_tarea()
    elif opcion == '2':
        Lista_tareas.completar_tarea()
    elif opcion == '3':
        Lista_tareas.eliminar_tarea()
    elif opcion == '4':
        print(Lista_tareas)
    elif opcion == '5':
        print('Saliendo del gestor de tareas.')
    else:
        print('Introduzca una opción válida.')




