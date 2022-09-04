"""
Nombre: El Misterio de Albus.
Por: Luis Alberto Salazar y Juan David Aycardi.
"""

from os import system
import time

def main():
    flag = True
    while(flag):
        system("cls")
        print("==================================================================")
        print("EL MISTERIO")
        print("DE")
        print("ALBUS")
        print("==================================================================")
        print("Menu de opciones")
        print("__________________________________________________________________")
        print("1) Iniciar nueva partida")
        print("2) Continuar partida")
        print("3) Salir del juego")
        print("__________________________________________________________________")
        x = int(input("¿Que opcion desea seleccionar?: "))
        while(x < 1 or x > 3):
            print("")
            print("Error, por favor seleccion una opcion valida")
            x = int(input("¿Que opcion desea seleccionar?: "))
        
        print("")
        if(x == 1):
            print("Iniciando una nueva partida porque aun no hay funciones")
            time.sleep(5)
        elif(x == 2):
            print("Continuando partida guardada")
            time.sleep(5)
        else:
            print("==================================================================")
            print("Gracias por jugar, esperamos que su experiencia haya sido grata")
            flag = False

main()