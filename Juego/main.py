"""
Nombre: El Misterio de Albus.
Por: Luis Alberto Salazar y Juan David Aycardi.
"""
from parte1 import stateMachine
from os import system
import time
import sys
from OpenAl import *

def dprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.17)
    print()

def main():
    flag = True
    while(flag):
        sound(0)
        system("cls")
        print("==================================================================")
        dprint("EL MISTERIO")
        dprint("DE")
        dprint("ALBUS")
        print("==================================================================")
        print("Menú de opciones")
        print("__________________________________________________________________")
        print("1) Iniciar nueva partida")
        print("2) Salir del juego")
        print("__________________________________________________________________")
        x = int(input("¿Qué opción desea seleccionar?: "))
        while(x < 1 or x > 2):
            print("")
            print("Error, por favor seleccione una opción válida")
            x = int(input("¿Qué opción desea seleccionar?: "))
        
        print("")
        if(x == 1):
            print("Iniciando una nueva partida...")
            print("")
            time.sleep(5)
            stateMachine()
        else:
            print("==================================================================")
            print("Gracias por jugar, esperamos que su experiencia haya sido grata")
            flag = False

main()