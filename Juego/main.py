"""
Nombre: El Misterio de Albus.
Por: Luis Alberto Salazar y Juan David Aycardi.
"""

import time
import sys

def dprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.15)
    print()

def main():
    flag = True
    while(flag):
        print("==================================================================")
        dprint("EL MISTERIO")
        dprint("DE")
        dprint("ALBUS")
        print("==================================================================")
        print("Menú de opciones")
        print("__________________________________________________________________")
        print("1) Iniciar nueva partida")
        print("2) Continuar partida")
        print("3) Salir del juego")
        print("__________________________________________________________________")
        x = int(input("¿Qué opción desea seleccionar?: "))
        while(x < 1 or x > 3):
            print("")
            print("Error, por favor seleccione una opción válida")
            x = int(input("¿Qué opción desea seleccionar?: "))
        
        print("")
        if(x == 1): print("Iniciando una nueva partida porque aun no hay funciones")
        elif(x == 2): print("Continuando partida guardada")
        else:
            print("==================================================================")
            print("Gracias por jugar, esperamos que su experiencia haya sido grata")
            flag = False

main()