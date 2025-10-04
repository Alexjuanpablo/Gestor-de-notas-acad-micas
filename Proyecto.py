# menu principal
cursos = []

def menu():
    print("==== Menú Principal ====")
    print("[1] Registrar nuevo curso")
    print("[2] Mostrar cursos y notas")
    print("[3] Calcular promedio general")
    print("[4] Cursos aprobados y reprobados")
    print("[5] Actualizar notas")
    print("[6] Eliminar curso")
    print("[0] Salir")

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
        
# codigo para la opcion 5, actualizacion de notas 
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
    elif option == 5:
        actualizar_notas()
    elif option == 6:
        eliminar_curso()

    else:
        print("Opción inválida. Intente de nuevo.")

    print()
    menu()
    option = int(input("Ingrese su opción: "))

print("Gracias por usar el programa.")
