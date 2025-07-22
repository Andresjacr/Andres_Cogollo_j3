import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from matricula import registro as st
from rutas import skills as rt
from notas_generales import notas as nt
from nota_final import nota_fin as nf
from tabla_de_estudiantes import inf_estudiantes as tb

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('1. matricular  alumno')
    print('2. asignar ruta al estudiante')
    print('3. Registrar notas')
    print('4. Consultar nota final')
    print('5. tabla de estudiantes matriculados')
    print('6. Salir')
    try:
        opcion = int(input('Seleccione una opción: '))
        if opcion < 1 or opcion > 4:
            print('Opción no válida. Intente de nuevo')
            return main_menu()
        return opcion
    except ValueError:
        print('Entrada no válida. Intente de nuevo')
        return main_menu()

if __name__ == '__main__':
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('bienbenido al sistema de gestion de alumnos')
        opcion= main_menu()
        if opcion == 1:
            st.add_student()
        elif opcion ==2:
            rt.add_students.copy()
        elif opcion ==3:
            nt.registrar_notas()
        elif opcion ==4:
            nf.calcular_promedio
        elif opcion ==5:
            tb.inf_estudiantes()
