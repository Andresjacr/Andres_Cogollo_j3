import matricula.registro as st
import os

def add_student():
    os.system('cls' if os.name == 'nt' else 'clear')
    student = st.students.copy()
    id = input("Ingrese el ID del Estudiante: ")
    student['nombre'] = input("Ingrese el Nombre del Estudiante: ")
    student['edad'] = int(input("Ingrese la Edad del Estudiante: "))
    student['email'] = input("Ingrese el Email del Estudiante: ")
    student['telefono'] = input("Ingrese el Telefono del Estudiante: ")
    st.campus.update({id: student})
