"""Ejercicio 19: Registro de tareas pendientes.

Escribe un programa que pregunte cuántas tareas se quieren registrar y, para
cada una, pida su nombre y si está completada. Para las tareas completadas,
muestra un mensaje de confirmación. Para las pendientes, no hagas nada todavía:
usa pass como marcador de posición, dejando ese caso preparado para
implementarlo más adelante, y usa continue para saltar el aviso de "tarea
procesada" y contarla como pendiente. Al final, muestra cuántas tareas han
quedado pendientes.
"""


while True:
    try:
        total_tareas = int(input("¿Cuántas tareas deseas registrar?: "))
        if total_tareas > 0:
            break
        print("Introduce un número mayor que 0.")
    except ValueError:
        print("Introduce un número válido.")

pendientes = 0

for i in range(total_tareas):
    print(f"---Tarea {i+1} ---")
    nombre = input("Nombre de la tarea: ")
    completada = input("¿Está completada? (s/n): ").strip().lower() == "s"

    if completada:
        print(f"Confirmación: La tarea '{nombre}' está completada.")
    else:
        pass
        pendientes += 1
        continue
    print(f"Tarea '{nombre}' procesada con éxito")
print(f"\nTotal de tareas que han quedado pendientes: {pendientes}")
