"""
Codificación del Misterio de Albus PARTE 1
"""

from distutils.errors import LibError
from os import system
import time

comandos_niveles = [["go", "stay"], ["follow", "return"]]
formato_comandos = {"go": ["name"], "stay": [], "follow": ["name"], "return": ["name"]}
contador = 0
contador_derecha = 0
contador_izquierda = 0

def imprimirFinal():
    system("cls")
    print("======================================================================================================")
    print("FIN DEL JUEGO.")
    print("Esperamos que te haya gustado, recuerda que hay más de un solo final, puedes volver a iniciar y")
    print("recorrer todos los finales que tiene el juego.")
    print("======================================================================================================")
    time.sleep(7)

def evaluar_comando(comando, texto):
    # Primero se evalua si se envio el formato adecuado del comando por parte del usuario.
    if(len(formato_comandos[comando[0]]) + 1 != len(comando)): return True
    veracidad = False
    for condiciones in formato_comandos[comando[0]]:
        if(condiciones == "name" and comando[1] != texto): veracidad = True
    return veracidad

# Funciones para cargar el texto de los archivos
def cargarTexto():
    global contador
    jugar = 0
    archivo = open("../Juego/Historia_to_load/parte1/parte1.txt", "r", encoding = 'utf-8')
    archivo = archivo.readlines()
    archivo = archivo[contador:]
    for linea in archivo:
        contador += 1
        if(linea[0] == "="):
            jugar += 1
            if(jugar == 2):
                print(linea)
                break
        print(linea)
    contador += 1

def cargarTextoDerecha():
    global contador_derecha
    archivo = open("../Juego/Historia_to_load/parte1/decision_derecha.txt", "r", encoding = 'utf-8')
    archivo = archivo.readlines()
    archivo = archivo[contador_derecha:]
    for linea in archivo:
        contador_derecha += 1
        if(linea[0] == "+"): break
        print(linea)
    contador_derecha += 1
    
def cargarTextoIzquierda():
    global contador_izquierda
    archivo = open("../Juego/Historia_to_load/parte1/decision_izquierda.txt", "r", encoding = 'utf-8')
    archivo = archivo.readlines()
    archivo = archivo[contador_izquierda:]
    for linea in archivo:
        contador_izquierda += 1
        if(linea[0] == "-"): break
        print(linea)
    contador_izquierda += 1

# Función principal
def stateMachine():
    state = 1
    end = True
    while(end):
        if(state == 1):
            cargarTexto()
            x = input("/> ")
            x = x.lower().split()
            while(x[0] not in comandos_niveles[state - 1] or evaluar_comando(x, "alderaan")):
                print("Comando no reconocido.")
                x = input("/> ")
                x = x.lower().split()
            if(x[0] == "go"):
                state = 2
                print("")
                cargarTextoIzquierda()
                time.sleep(6)
            elif(x[0] == "stay"):
                end = False
                cargarTextoDerecha()
                time.sleep(10)
                imprimirFinal()
        elif(state == 2):
            cargarTexto()
            x = input("/> ")
            x = x.lower().split()
            while(x[0] not in comandos_niveles[state - 1] or evaluar_comando(x, "extraño") or evaluar_comando(x, "home")):
                print("Comando no reconocido.")
                x = input("/> ")
                x = x.lower().split()
            if(x[0] == "follow"):
                state = 3
                print("")
                cargarTextoIzquierda()
                time.sleep(6)
            elif(x[0] == "return"):
                end = False
                cargarTextoDerecha()
                time.sleep(20)
                imprimirFinal()
        elif(state == 3):
            cargarTexto()
            x = input("/> ")
            x = x.lower().split()
            while(x[0] not in comandos_niveles[0] or len(x) == 1 or x[1] != "extraño" or x[1] != "home"):
                print("Comando no reconocido.")
                x = input("/> ")
                x = x.lower().split()
        