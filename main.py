from datetime import date

from datetime import datetime

import os

from clasePersona import Persona

from claseTallerCapacitacion import tallerCapacitacion

from claseInscripcion import Inscripcion

from manejadorTalleres import manejadorTalleres

from claseMenu import Menu

def testClaseAsociacion():
    unaPersona = Persona('Manuel Rossi', 'San Juan 785 - Jachal', '38409657')
    unTaller = tallerCapacitacion(1, 'Maneja Office como un experto', 45, 7500)
    inscripcion = Inscripcion(unaPersona, unTaller, datetime.date(2020, 5, 20) , True)

    print(inscripcion)

    talleres = manejadorTalleres(5)
    #talleres.mostrarDatos()

if __name__ == '__main__':
    #testClaseAsociacion()
    #hoy = date.today()
    #print(hoy)
    #print(type(hoy))

    menu = Menu()
    salir = False
    while not salir:
        print("\n------------Menu------------\n0. Salir 1\n1. Cargar datos de los talleres.\n2. Inscribir una persona a un taller. \n3. Consultar inscripcion. \n4. Consultar inscriptos. \n5. Registrar pago. \n6. Guardar inscripciones.")
        op = int(input('Ingrese una opcion: '))
        os.system('cls')
        talleres = menu.opcion(op)
        salir = op == 0

