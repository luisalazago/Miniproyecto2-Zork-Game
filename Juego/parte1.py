"""
Codificación del Misterio de Albus PARTE 1
"""

from distutils.errors import LibError
from os import system
import time

# Variables Globales
comandos_niveles = [
    ["go", "stay"],  ["follow", "return"], 
    ["take", "straight"], ["send", "go"]
]
formato_comandos = {
    "go": [["alderaan", "home"], 1], "stay": [[], 0], 
    "follow": [["guy"], 1], "return": [["home"], 1],
    "send": [["message"], 1], "take": [["atajo"], 1],
    "straight": [[], 0]
}
contador = 0
contador_derecha = 0
contador_izquierda = 0

# Funciones para el final
def imprimirFinal():
    system("cls")
    print("======================================================================================================")
    print("FIN DEL JUEGO.")
    print("Esperamos que te haya gustado, recuerda que hay más de un solo final, puedes volver a iniciar y")
    print("recorrer todos los finales que tiene el juego.")
    print("======================================================================================================")
    time.sleep(7)

def evaluar_comando(comando):
    # Primero se evalua si se envio el formato adecuado del comando por parte del usuario.
    ans = None
    if(not formato_comandos[comando[0]][1]): ans = False
    elif(formato_comandos[comando[0]][1] + 1 != len(comando)):
        ans = True
    else:
        ans = False
        if(not comando[1] in formato_comandos[comando[0]][0]): ans = True
    return ans

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
    print("")
    for linea in archivo:
        contador_derecha += 1
        if(linea[0] == "+"): break
        print(linea)

def cargarTextoIzquierda():
    global contador_izquierda
    archivo = open("../Juego/Historia_to_load/parte1/decision_izquierda.txt", "r", encoding = 'utf-8')
    archivo = archivo.readlines()
    archivo = archivo[contador_izquierda:]
    print("")
    for linea in archivo:
        contador_izquierda += 1
        if(linea[0] == "-"): break
        print(linea)

# Funciones para jugar
def juego(state):
    cargarTexto()
    x = input("/> ")
    x = x.lower().split()
    veracidad = True
    while(veracidad):
        if(x[0] in comandos_niveles[state - 1]):
            for comando in comandos_niveles[state - 1]:
                if(x[0] == comando): veracidad = evaluar_comando(x)
        if(not veracidad): break
        print("Comando no reconocido.")
        x = input("/> ")
        x = x.lower().split()
    return x

# Función principal
def stateMachine():
    global contador, contador_izquierda, contador_derecha
    contador, contador_izquierda, contador_derecha = 0, 0, 0
    state = 1
    end = True
    while(end):
        if(state == 1):
            comando = juego(state)
            if(comando[0] == "go"):
                state = 2
                print("")
                cargarTextoIzquierda()
                time.sleep(6)
            elif(comando[0] == "stay"):
                end = False
                cargarTextoDerecha()
                time.sleep(10)
                imprimirFinal()
        elif(state == 2):
            comando = juego(state)
            if(comando[0] == "follow"):
                state = 3
                print("")
                cargarTextoIzquierda()
                time.sleep(6)
            elif(comando[0] == "return"):
                end = False
                cargarTextoDerecha()
                time.sleep(20)
                imprimirFinal()
        elif(state == 3):
            comando = juego(state)
            if(comando[0] == "take"):
                cargarTextoIzquierda()
                time.sleep(30)
            elif(comando[0] == "straight"):
                cargarTextoDerecha()
                time.sleep(60)
            state = 4
        elif(state == 4):
            comando = juego(state)
            if(comando[0] == "go"):
                cargarTextoDerecha()
            elif(comando[0] == "send"):
                cargarTextoIzquierda()