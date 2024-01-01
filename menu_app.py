def agregar_compra(compras, monto):
    compras.append(monto)
    print(f"Compra de ${monto} agregada correctamente.")


def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        for i, compra in enumerate(compras, start=1):
            print(f"Compra {i}: ${compra}")


def mostrar_total(compras):
    total = sum(compras)
    print(f"Total gastado: ${total}")


def main():
    compras = []

    while True:
        print("\nMenú:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            monto = float(input("Ingrese el monto de la compra: "))
            agregar_compra(compras, monto)
        elif opcion == "2":
            mostrar_compras(compras)
        elif opcion == "3":
            mostrar_total(compras)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
