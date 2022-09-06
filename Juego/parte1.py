"""
Codificación del Misterio de Albus PARTE 1
"""

from distutils.errors import LibError
from os import system
import time

comandos_niveles = [["go", "stay"], []]

def cargarTexto(contador, des):
    jugar = 0
    camino = 0
    archivo = open("../Juego/Historia_to_load/parte1.txt", "r")
    for linea in archivo:
        contador += 1
        if(linea[0] == "=" and des == None):
            jugar += 1
            if(jugar == 2):
                print(linea)
                break
        elif(linea[0] == "+" and des == 1): camino = 1
        elif(linea[0] == "-" and des == 2): camino = 2 
        else:
            print(linea)
            
        if(camino == 1):
            if(linea[0] == "-" and des == 1): break
            elif(linea[0] == "+" and des == 2): break
            print(linea)
            camino = 0
    return contador

def stateMachine():
    state = 1
    contador = 0
    end = True
    while(end):
        if(state == 1):
            contador = cargarTexto(contador, None)
            x = input("/> ")
            x = x.lower().split()
            while(x[0] not in comandos_niveles[0]):
                print("Comando no reconocido.")
                x = input("/> ")
                x = x.lower().split()
            if(x[0] == "go"):
                state = 2
                contador = cargarTexto(contador, 1)
                time.sleep(6)
            elif(x[0] == "stay"):
                end = False
                contador = cargarTexto(contador, 2)
                time.sleep(10)
            end = False
        """
        elif(state == 2):
        elif(state == 2):
        elif(state == 2):
        elif(state == 2):
        elif(state == 2):
        elif(state == 2):
        elif(state == 2):
        elif(state == 2):
        elif(state == 2):
        elif(state == 2):
        elif(state == 2):
        elif(state == 2):
        elif(state == 2):
        elif(state == 2):
        elif(state == 2):
        elif(state == 2):
        elif(state == 2):
        elif(state == 2):
        """
        