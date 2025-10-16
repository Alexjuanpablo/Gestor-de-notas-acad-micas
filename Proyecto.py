# menu principal
cursos = []

def menu():
    print("==== Menú Principal ====")
    print("[1] Registrar nuevo curso")
    print("[2] Mostrar cursos y notas")
    print("[3] Calcular promedio general")
    print("[4] Cursos aprobados y reprobados")
    print("[5] buscar curso por nombre ") # busquda lineal
    print("[6] Actualizar nota de un curso")
    print("[7] Eliminar curso")
    print("[8] oredenar cursos por notas") #ordenamiento por burbuja
    print("[9] ordenar cursos por nombres ") #ordenamiento por inserción
    print("[10] buscar curso por nombre")  #busqueda binaria
    print("[11] simular cola de solicitudes")
    print("[12] mostrar historial de cambios") #pila
    print("[0] Salir")
    print ("Seleccione una opcción")



# codigo de la opcion 1
def registrar_curso():
    while True:
        nombre = input("Ingrese el nombre del curso (o 'salir' para volver al menú): ").strip()
        if nombre.lower() == 'salir':
            break
        try:
            nota = float(input(f"Ingrese la nota para {nombre}: "))
            cursos.append({"nombre": nombre, "nota": nota})
            print(f"Curso '{nombre}' con nota {nota} agregado correctamente.\n")
        except ValueError:
            print("La nota debe ser un número. Intente de nuevo.\n")
#codigo de la opcion 2 

def mostrar_cursos():
    if not cursos:
        print("No hay cursos registrados aún.")
    else:
        print("Cursos registrados:")
        for idx, curso in enumerate(cursos, 1):
            print(f"{idx}. {curso['nombre']} - Nota: {curso['nota']}")

#codigo de la opcion 3 para el calculo del promdio
def calcular_promedio():
    if not cursos:
        print("No hay cursos registrados para calcular el promedio.")
        return
    total = sum(curso['nota'] for curso in cursos)
    promedio = total / len(cursos)
    print(f"El promedio general es: {promedio:.2f}")

#codigo para la opcion 4, verificacion de cursos aprobados y reprobados 
def cursos_aprobados_reprobados():
    if not cursos:
        print("No hay cursos registrados para analizar.")
        return
    aprobados = [c for c in cursos if c['nota'] >= 60]
    reprobados = [c for c in cursos if c['nota'] < 60]

    print(f"\nCursos aprobados ({len(aprobados)}):")
    for c in aprobados:
        print(f"- {c['nombre']} (Nota: {c['nota']})")

    print(f"\nCursos reprobados ({len(reprobados)}):")
    for c in reprobados:
        print(f"- {c['nombre']} (Nota: {c['nota']})")



# opción 5: buscar curso por nombre (busqueda lienal)
def buscar_curso_por_nombre():
    if not cursos:
        print("No hay cursos registrados para buscar.")
        return

    nombre_busqueda = input("Ingrese el nombre del curso que desea buscar: ").strip().lower()
    encontrados = [c for c in cursos if c['nombre'].lower() == nombre_busqueda]

    if encontrados:
        for curso in encontrados:
            print(f"Curso encontrado: {curso['nombre']} - Nota: {curso['nota']}")
    else:
        print(f"No se encontró ningún curso con el nombre '{nombre_busqueda}'.")



# codigo para la opcion 6, actualizacion de notas 
def actualizar_notas():
    if not cursos:
        print("No hay cursos registrados para actualizar.")
        return
    mostrar_cursos()
    nombre_curso = input("Ingrese el nombre del curso al que desea actualizar la nota: ").strip()
    
    for curso in cursos:
        if curso['nombre'].lower() == nombre_curso.lower():
            try:
                nueva_nota = float(input(f"Ingrese la nueva nota para {curso['nombre']}: "))
                curso['nota'] = nueva_nota
                print(f"Nota actualizada correctamente para el curso '{curso['nombre']}'.\n")
                return
            except ValueError:
                print("La nota debe ser un número.")
                return
    print(f"No se encontró el curso '{nombre_curso}'. Intente nuevamente.")

#codigo para la opccion 7, eliminar curso
def eliminar_curso():
    if not cursos:
        print("No hay cursos registrados para eliminar.")
        return

    mostrar_cursos()
    nombre_curso = input("Ingrese el nombre del curso que desea eliminar: ").strip()

    for curso in cursos:
        if curso['nombre'].lower() == nombre_curso.lower():
            cursos.remove(curso)
            print(f"El curso '{curso['nombre']}' ha sido eliminado correctamente.")
            return

    print(f"No se encontró el curso '{nombre_curso}'. Verifique el nombre e intente de nuevo.")

# codigo para ala opcion 8 ordenar cursos por notas (es por ordenamiento de burbuja)
def ordenar_cursos_por_notas():
    if not cursos:
        print("No hay cursos registrados para ordenar.")
        return

    n = len(cursos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if cursos[j]['nota'] > cursos[j + 1]['nota']:
                cursos[j], cursos[j + 1] = cursos[j + 1], cursos[j]

    print("Cursos ordenados por notas (de menor a mayor):")
    for idx, curso in enumerate(cursos, 1):
        print(f"{idx}. {curso['nombre']} - Nota: {curso['nota']}")

# codigo de la opcion 9 ordenar cursos por nombres (ordenamiento por insercion)

def ordenar_cursos_por_nombres():
    if not cursos:
        print("No hay cursos registrados para ordenar.")
        return

    for i in range(1, len(cursos)):
        key = cursos[i]
        j = i - 1
        while j >= 0 and cursos[j]['nombre'].lower() > key['nombre'].lower():
            cursos[j + 1] = cursos[j]
            j -= 1
        cursos[j + 1] = key

    print("Cursos ordenados por nombre (alfabéticamente):")
    for idx, curso in enumerate(cursos, 1):
        print(f"{idx}. {curso['nombre']} - Nota: {curso['nota']}")

# opcion 10  buscar curso por nombre (busqueda binaria)
def buscar_curso_por_nombre_binaria():
    if not cursos:
        print("No hay cursos registrados para buscar.")
        return

    
    cursos.sort(key=lambda c: c['nombre'].lower())

    nombre_busqueda = input("Ingrese el nombre del curso que desea buscar: ").strip().lower()

    izquierda = 0
    derecha = len(cursos) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        nombre_medio = cursos[medio]['nombre'].lower()

        if nombre_medio == nombre_busqueda:
            print(f"Curso encontrado: {cursos[medio]['nombre']} - Nota: {cursos[medio]['nota']}")
            return
        elif nombre_medio < nombre_busqueda:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    print(f"No se encontró ningún curso con el nombre '{nombre_busqueda}'.")

#opcion 11 simular cola de solicitudes de revisión

from collections import deque

# Cola para solicitudes de revisión
cola_solicitudes = deque()

def simular_cola_solicitudes():
    while True:
        print("\n=== Cola de solicitudes de revisión ===")
        print("[1] Agregar solicitud")
        print("[2] Procesar siguiente solicitud")
        print("[3] Mostrar solicitudes pendientes")
        print("[0] Volver al menú principal")
        
        opcion_cola = input("Seleccione una opción: ").strip()
        
        if opcion_cola == '1':
            solicitud = input("Ingrese el nombre del curso o estudiante para revisión: ").strip()
            cola_solicitudes.append(solicitud)
            print(f"Solicitud '{solicitud}' agregada a la cola.")
        
        elif opcion_cola == '2':
            if cola_solicitudes:
                atendida = cola_solicitudes.popleft()
                print(f"Solicitud '{atendida}' procesada y eliminada de la cola.")
            else:
                print("No hay solicitudes para procesar.")
        
        elif opcion_cola == '3':
            if cola_solicitudes:
                print("Solicitudes pendientes en la cola:")
                for idx, sol in enumerate(cola_solicitudes, 1):
                    print(f"{idx}. {sol}")
            else:
                print("La cola de solicitudes está vacía.")
        
        elif opcion_cola == '0':
            print("Volviendo al menú principal.")
            break
        
        else:
            print("Opción inválida. Intente de nuevo.")

# opcion 12 mostrar historial de cambios (pilas)
# Pila para historial de cambios

historial_cambios = []

# Modificación en actualizar_notas (opción 6)
def actualizar_notas():
    if not cursos:
        print("No hay cursos registrados para actualizar.")
        return
    mostrar_cursos()
    nombre_curso = input("Ingrese el nombre del curso al que desea actualizar la nota: ").strip()
    
    for curso in cursos:
        if curso['nombre'].lower() == nombre_curso.lower():
            try:
                nueva_nota = float(input(f"Ingrese la nueva nota para {curso['nombre']}: "))
                nota_anterior = curso['nota']
                curso['nota'] = nueva_nota
                # Guardar en historial
                cambio = f"Cambio en '{curso['nombre']}': {nota_anterior} -> {nueva_nota}"
                historial_cambios.append(cambio)
                print(f"Nota actualizada correctamente para el curso '{curso['nombre']}'.\n")
                return
            except ValueError:
                print("La nota debe ser un número.")
                return
    print(f"No se encontró el curso '{nombre_curso}'. Intente nuevamente.")

# Función opción 12: mostrar historial de cambios (pila)
def mostrar_historial_cambios():
    if not historial_cambios:
        print("No hay historial de cambios para mostrar.")
        return

    print("Historial de cambios (últimos primero):")
    for idx, cambio in enumerate(reversed(historial_cambios), 1):
        print(f"{idx}. {cambio}")



# Programa principal
menu()
option = int(input("Ingrese su opción: "))

while option != 0:
    if option == 1:
        registrar_curso()
    elif option == 2:
        mostrar_cursos()
    elif option == 3:
        calcular_promedio()
    elif option == 4:
        cursos_aprobados_reprobados()
    elif option ==5:
        buscar_curso_por_nombre ()
    elif option == 6:
        actualizar_notas()
    elif option == 7:
        eliminar_curso()
    elif option == 8:
        ordenar_cursos_por_notas()
    elif option == 9:
        ordenar_cursos_por_nombres()
    elif option == 10:
        buscar_curso_por_nombre_binaria()
    elif option == 11:
        simular_cola_solicitudes()
    elif option == 12:
        mostrar_historial_cambios()


    else:
        print("Opción inválida. Intente de nuevo.")

    print()
    menu()
    option = int(input("Ingrese su opción: "))

print("Gracias por usar el programa gestor de notas Academicas. ¡Hasta pronto! ")

    option = int(input("Ingrese su opción: "))

print("Gracias por usar el programa.")
