"""
Codificación del Misterio de Albus PARTE 1
"""

from os import system
from final import final1

comandos_niveles = [["go", "stay"], []]

def cargarTexto(contador, des):
    jugar = 0
    archivo = open("../Juego/Historia_to_load/parte1.txt", "r")
    for linea in archivo:
        contador += 1
        if(linea[0] == "=" and des == None):
            jugar += 1
            if(jugar == 2):
                print(linea)
                break
        elif(linea[0] == "+" and des == 1):
            pass
        print(linea)
    return contador

def stateMachine():
    state = 1
    contador = 0
    end = True
    while(end):
        system("cls")
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
                
            elif(x[0] == "stay"):
                end = False
                final1()
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
        