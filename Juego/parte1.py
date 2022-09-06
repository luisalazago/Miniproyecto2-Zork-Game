"""
Codificación del Misterio de Albus PARTE 1
"""

from distutils.errors import LibError
from os import system
import time

comandos_niveles = [["go", "stay"], []]
formato_comandos = {"go": ["name"], "stay": []}
contador = 0

def evaluar_comando(comando, texto):
    # Primero se evalua si se envio el formato adecuado del comando por parte del usuario.
    if(len(formato_comandos[comando[0]]) + 1 != len(comando)): return True
    veracidad = False
    for condiciones in formato_comandos[comando[0]]:
        if(condiciones == "name" and comando[1] != texto): veracidad = True
    return veracidad

def cargarTexto(des):
    global contador
    jugar = 0
    texto = 0
    camino = des
    cam1 = 0
    cam2 = 0
    archivo = open("../Juego/Historia_to_load/parte1.txt", "r")
    archivo = archivo.readlines()
    if(contador):
        archivo = archivo[contador:]
        #print(archivo)
        #x = input()
    for linea in archivo:
        contador += 1
        if(camino == 0):
            if(linea[0] == "="):
                jugar += 1
                if(jugar == 2):
                    print(linea)
                    break
            print(linea)  
        elif(camino == 1):
            if(linea[0] == "+"): cam1 = 1
            elif(cam1):
                if(linea[0] == "-"):
                    texto = 1
                    break
                print(linea)
        else:
            if(linea[0] == "-"): cam2 = 1
            elif(cam2):
                if(linea == "\n"):
                    texto = 1
                    break
                print(linea)
    
    if(texto):
        archivo = archivo[contador:]
        print(archivo)
        for linea in archivo:
            contador += 1
            if(linea == "."): break
    print(contador)

def stateMachine():
    state = 1
    contador = 0
    end = True
    while(end):
        if(state == 1):
            cargarTexto(0)
            x = input("/> ")
            x = x.lower().split()
            while(x[0] not in comandos_niveles[0] or evaluar_comando(x, "alderaan")):
                print("Comando no reconocido.")
                x = input("/> ")
                x = x.lower().split()
            if(x[0] == "go"):
                state = 2
                print("")
                cargarTexto(1)
                time.sleep(6)
            elif(x[0] == "stay"):
                end = False
                cargarTexto(2)
                time.sleep(10)
                system("cls")
                print("======================================================================================================")
                print("FIN DEL JUEGO.")
                print("Esperamos que te haya gustado, recuerda que hay más de un solo final, puedes volver a iniciar y")
                print("recorrer todos los finales que tiene el juego.")
                print("======================================================================================================")
                time.sleep(7)
        elif(state == 2):
            cargarTexto(0)
            x = input("/> ")
            x = x.lower().split()
            while(x[0] not in comandos_niveles[0] or len(x) == 1 or x[1] != "alderaan"):
                print("Comando no reconocido.")
                x = input("/> ")
                x = x.lower().split()
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
        """
        