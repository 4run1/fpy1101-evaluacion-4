biblioteca = []

#funciones

#validaciones
def validar_titulo(titulo):
    return titulo != ""
def validar_copias(copias):
    try:
        copias = int(copias)
        return copias >= 0
    except ValueError:
        return False

def validar_prestamo(prestamos):
    try:
        prestamos = int(prestamos)
        return prestamos > 0
    except ValueError:
        return False
#fin validaciones

def agregar_libro(biblioteca):
    titulo = input("Ingrese el título del libro: ").strip()
    copias = input("Ingrese la cantidad de copias: ").strip()
    prestamos = input("Ingrese la cantidad de días de préstamos: ").strip()

    if validar_titulo(titulo):
    
        if validar_copias(copias):
        
            if validar_prestamo(prestamos):
                copias = int(copias)
                prestamos = int(prestamos)

                if copias > 0:
                    disponibilidad = True
                else:
                    disponibilidad = False
            
                
                libros = {
                    "titulo": titulo,
                    "copias": copias,
                    "prestamos": prestamos,
                    "disponibilidad": disponibilidad
                }
                biblioteca.append(libros)
                print("Libro agregado correctamente.")
                

            else:
                print("Error: el numero de prestamos debe ser mayor a 0")
        else:
            print("Error: el numero de copias NO deben ser negativas.")
    else:
        print("Error: el titulo no puede estar vacio.")           

def buscar_libro(biblioteca, titulo):
    for posicion, libro in enumerate(biblioteca):

        if libro["titulo"].lower() == titulo.lower():
            return posicion

    return -1 

def eliminar_libro(biblioteca):
    titulo = input("Ingrese el título del libro a eliminar: ").strip()

    posicion = buscar_libro(biblioteca, titulo)

    if posicion != -1:

        while True:

            print("Esta acción es irreversible.")
            seguro = input(f"¿Desea eliminar '{titulo}'? (S/N): ").strip().upper()

            if seguro == "S":
                biblioteca.pop(posicion)
                print("\nEliminación exitosa.\n")
                break

            elif seguro == "N":
                print("\nCancelación exitosa.\n")
                break

            else:
                print("Error: ingrese una opción válida (S/N).")

    else:
        print(f"El libro '{titulo}' no se encuentra registrado.")

def actualizar_disponibilidad(biblioteca):
    for i in biblioteca:
        if i["copias"] > 0:
            i["disponibilidad"] = True
        else:
            i["disponibilidad"] = False

def mostrar_libros(biblioteca):
    print("=== LISTA DE LIBROS ===")
    actualizar_disponibilidad(biblioteca)
    for i in biblioteca:
        if i["disponibilidad"]:
            estado = "DISPONIBLE"
        else:
            estado = "SIN COPIAS"

        print(f"""
              Titulo = {i['titulo']}
              Copias = {i['copias']}
              Prestamos = {i['prestamos']}
              Estado = {estado}
              *********************************""")
                    


def mostrar_menu():
        print("    ========== MENÚ PRINCIPAL ========== ")
        print("1. Agregar libro")
        print("2. Buscar libro")
        print("3. Eliminar libro")
        print("4. Actualizar disponibilidad")
        print("5. Mostrar libros")
        print("6. Salir")
        print("=====================================")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))

            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Error: ingrese una opción entre 1 y 6.")

        except ValueError:
            print("Error: debe ingresar un número.")

#fin funciones


#codigo principal
while True:

    mostrar_menu()
    opcion = leer_opcion()
#opcion1
    if opcion == 1:
        agregar_libro(biblioteca)

#opcion 2
    elif opcion == 2:
        titulo = input("ingrese el titulo del libro a buscar: ")
        posicion = buscar_libro(biblioteca, titulo)
    
        if posicion != -1:
            
            libro = biblioteca[posicion]
            if libro["disponibilidad"]:
                estado = "DISPONIBLE"
            else:
                estado = "SIN COPIAS"

            print(f"""\nLibro encontrado:
            Posición: {posicion}
            Título: {libro['titulo']}
            Copias: {libro['copias']}
            Préstamos: {libro['prestamos']}
            Estado: {estado}
            """)

        else:
            print("\n Libro no encontrado.\n")

#opcion 3
    elif opcion == 3:
        eliminar_libro(biblioteca)

    elif opcion == 4:
        actualizar_disponibilidad(biblioteca)
        print("Actualizacion exitosa.\n")

    elif opcion == 5:
        mostrar_libros(biblioteca)

    elif opcion == 6:
        print("\n Gracias por usar el sistema. Vuelva pronto")
        break