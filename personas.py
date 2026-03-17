alumnos = []

cantidad = int(input("¿Cuantos alumnos desea cargar?"))

for i in range(cantidad):
    print(f"\nAlumno{i+1}")
    nombre = input("nombre:")
    edad = int(input("edad:"))
    nota = float(input("nota:"))


    alumnos.append({
        "nombre":nombre,
        "edad":edad,
        "nota":nota
    })

print("\nLista en orden de ingreso:")
for alumno in alumnos:
    print(f"{alumno['nombre']} -Edad:{alumno['edad']}-Nota: {alumno['nota']}")

ordenados = sorted(alumnos, key=lambda x:x['nota'],reverse=True)
for alumno in ordenados:
 print(f"{alumno['nombre']}-Nota: {alumno['nota']}")
        

suma = 0
for alumno in alumnos:
   suma += alumno['nota']

promedio = suma / cantidad

print(f"\nPromedio geneneral:{promedio}")


