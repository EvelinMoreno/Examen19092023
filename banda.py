agrupaciones = []

def registrar_agrupacion():
    id_agrupacion = len(agrupaciones) + 1
    nombre = input("Nombre de la agrupación: ")
    genero = input("Ingrese el género musical: ")
    hora_presentacion = input("Ingrese la hora de la presentación (HH:MM): ")
    pago = input(float("Ingrese el pago acordado: "))
    estado = input(bool("¿Ya se presentó? (True/False): "))
    if estado.lower() == 'true':
        estado = True
    elif estado.lower() == 'false':
        estado = False
    else:
        print("Valor no válido, ingrese True o False")

    agrupacion = {
        "id": id_agrupacion,
        "nombre": nombre,
        "genero": genero,
        "hora_presentacion": hora_presentacion,
        "pago": pago,
        "estado": estado
    }

    agrupaciones.append(agrupacion)
    print(f"Agrupación {nombre} registrada con éxito!")
    
def mostrar_estado_presentacion():
    print("Agrupaciones que no se han presentado:")
    for agrupacion in agrupaciones:
        if not agrupacion["estado"]:
            print(f"{agrupacion['nombre']}: False")
        else:
            print(f"{agrupacion['nombre']}: True")

def cambiar_hora_presentacion():
    id_agrupacion = int(input("Ingrese el ID de la agrupación a la que desea cambiar la hora de presentación: "))
    for agrupacion in agrupaciones:
        if agrupacion["id"] == id_agrupacion and not agrupacion["estado"]:
            nueva_hora = input("Ingrese nueva hora de presentación (HH:MM): ")
            agrupacion["hora_presentacion"] = nueva_hora
            print(f"Hora de presentación de {agrupacion['nombre']} cambiada a {nueva_hora}")
            break
    else:
        print("No se encontró una agrupación con el ID especificado o ya se ha presentado.")

def retirar_agrupacion():
    id_agrupacion = int(input("Ingrese el ID de la agrupación que desea retirar: "))
    for agrupacion in agrupaciones:
        if agrupacion["id"] == id_agrupacion and not agrupacion["estado"]:1
        agrupaciones.remove(agrupacion)
        print(f"{agrupacion['nombre']} ha sido retirada del festival.")
        break
    else:
        print("No se encontró una agrupación con el ID especificado o ya se ha presentado.")

# Menú principal
while True:
    print("\nMenú de opciones:")
    print("1. Registrar una agrupación")
    print("2. Mostrar agrupaciones que no se han presentado")
    print("3. Cambiar hora de presentación")
    print("4. Retirar una agrupación")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_agrupacion()
    elif opcion == "2":
        mostrar_estado_presentacion()
    elif opcion == "3":
        cambiar_hora_presentacion()
    elif opcion == "4":
        retirar_agrupacion()
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
