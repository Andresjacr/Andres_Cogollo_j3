import matricula.registro as st 
import datamodels.modelsdata as models
import os

st.add_student()
os.system('cls' if os.name == 'nt' else 'clear')
id = input("Ingrese el ID del Estudiante a mostrar: ")
student = models.campus.get(id, {})
print("Rutas Disponibles:")
print("Seleccione una ruta a matricular")
opciones = list(models.rutas.keys())
for i, opcion in enumerate(opciones, start=1):
    print(f"{i}. {opcion}")
opcion = int(input("Ingrese el número de la ruta: ")) - 1

if 0 <= opcion <len(opciones):
    ruta = {
        'nombre_ruta': opciones[opcion],
        'skills':[]
    }
    student.update({'ruta':ruta})
    print('ruta asignada correctamente')
else:
    print('opcionn no valida')
print(models.campus )