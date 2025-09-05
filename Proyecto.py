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
