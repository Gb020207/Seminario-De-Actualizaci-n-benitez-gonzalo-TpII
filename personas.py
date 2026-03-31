alumnos = []


try:
    cantidad = int(input("¿Cuántos alumnos desea cargar? "))
except ValueError:
    print("Error: Debe ingresar un número entero.")
    cantidad = 0

for i in range(cantidad):
    print(f"\n--- Registro Alumno {i+1} ---")
    nombre = input("Nombre: ")
    
   
    while True:
        try:
            edad = int(input("Edad: "))
            if edad < 0:
                print("La edad no puede ser negativa.")
            else:
                break
        except ValueError:
            print("Ingrese una edad válida (número).")


    while True:
        try:
            nota = float(input(f"Ingrese la nota de {nombre}: "))

            if nota > 10:
                print(" No existe nota más allá de 10. Reintente.")
            elif nota < 0:
                print(" No existe nota menor a 0. Reintente.")
            else:
                
                alumnos.append({
                    "nombre": nombre,
                    "edad": edad,
                    "nota": nota
                })
                
        except ValueError:
            print(" Error: Debe ingresar un número (ejemplo: 8.5).")



if alumnos:
    print("\n" + "="*30)
    print(" LISTA EN ORDEN DE INGRESO")
    print("="*30)
    for alumno in alumnos:
        print(f"{alumno['nombre']} - Edad: {alumno['edad']} - Nota: {alumno['nota']}")

    print("\n" + "="*30)
    print(" RANKING (MAYOR A MENOR)")
    print("="*30)
    ordenados = sorted(alumnos, key=lambda x: x['nota'], reverse=True)
    for alumno in ordenados:
        print(f"{alumno['nombre']} -> Nota: {alumno['nota']}")


    suma = sum(a['nota'] for a in alumnos)
    promedio = suma / len(alumnos)
    print(f"\nPROMEDIO GENERAL: {promedio:.2f}")
else:
    print("\nNo se cargaron alumnos.")