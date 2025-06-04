#Gestor de tareas: Una aplicación simple para agregar, eliminar y marcar tareas como completadas. (opcional: añadir un filtro, modificar tareas)

class Funciones: 
    
    def __init__(self): 
        self.lista = []

        
    def __str__(self): 
        contador = ""
        for i in self.lista:
            contador += f'{i}\n'
        return contador
    

    def añadir_tarea(self, estado = "Pendiente"):
        evento = input("Introduzca evento: ")
        dia = input("Seleccione la fecha: ")
        hora = input("Seleccione la hora del evento: ")
        lugar = input("Introduzca lugar del evento: ")
        
        self.lista.append({
            "Evento": evento,
            "Día": dia,
            "Hora": hora,
            "Lugar": lugar,
            "Estado": estado
        })
        
        return 
    
    
    def modificar_tarea(self): 
        tarea_modificada = input("Introduzca la tarea que se desea modificar: ")
        for i in self.lista:
            if i["Evento"] == tarea_modificada:
                return
            else:
                return f'No se han encontrado tareas por {tarea_modificada}'
            return    
    
    
    
    
    def eliminar_tarea(self):
        tarea_eliminada = input('Introduzca el evento que desea eliminar. Si no desea eliminar ninguna tarea escriba "Salir": ')
        for i in self.lista:
            if i["Evento"] == tarea_eliminada:
                self.lista.remove(i)
            elif tarea_eliminada == "Salir":
                print("Saliendo del programa...")
                break
            else:
                return f"No se han encontrados tareas por: {tarea_eliminada}"
            return    
        
    
    def completar_tarea(self):
        tarea_completa = input('Indique la tarea que se ha completado. Si no desea completar una tarea escriba "Salir": ')
        nuevo_estado = "Completada"
        for clave, valor in enumerate(self.lista): 
            if valor["Evento"] == tarea_completa:
                self.lista[clave]["Estado"] = nuevo_estado
            elif tarea_completa == "Salir":
                print("Saliendo del programa...")
                break
            else:
                tarea_completa = input("Tarea inexistente, por favor, introduzca la tarea correcta: ")
            return 