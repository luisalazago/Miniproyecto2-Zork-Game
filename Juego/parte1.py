"""
Codificación del Misterio de Albus PARTE 1
"""

from distutils.errors import LibError
from os import system
import time
from OpenAl import *

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
} # El formato de los comandos tiene los comandos y una pareja de las palabras que se deben colocar y la cantida de palabras que vienen después de comando que es el entero.
contador = 0
contador_derecha = 0
contador_izquierda = 0

def dprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.035)
    

# Funciones para el final
def imprimirFinal():
    """
    Esta función imprime el final en caso de que se llegue a un final del juego.
    """
    system("cls")
    print("======================================================================================================")
    dprint("FIN DEL JUEGO.")
    dprint("Esperamos que te haya gustado, recuerda que hay más de un solo final, puedes volver a iniciar y")
    dprint("recorrer todos los finales que tiene el juego.")
    print("======================================================================================================")
    time.sleep(7)

def evaluar_comando(comando):
    """
    Esta función permite verificar que el comando ingresado sea correcto tanto
    sintácticamente como semánticamente. Se verifica si el comando no debe tener
    más palabras después de la principal, se verifica si se envian la cantidad
    de palabras correctas y por último se verifica si las palabras después
    son las correctas.

    Retorna verdadero si hay un error y retorna falso cuando no.
    """
    ans = None
    if(not formato_comandos[comando[0]][1]): ans = False
    elif(formato_comandos[comando[0]][1] + 1 != len(comando)): ans = True
    else:
        ans = False
        if(not comando[1] in formato_comandos[comando[0]][0]): ans = True
    return ans

# Funciones para cargar el texto de los archivos
def cargarTexto():
    """
    Esta función permite cargar el texto de la historia principal, sin
    los caminos que se tomen.
    """
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
        dprint(linea)
    contador += 1

def cargarTextoDerecha():
    """
    Esta función permite cargar las decisiones que se tomen por el
    camino derecho.
    """
    global contador_derecha
    archivo = open("../Juego/Historia_to_load/parte1/decision_derecha.txt", "r", encoding = 'utf-8')
    archivo = archivo.readlines()
    archivo = archivo[contador_derecha:]
    dprint("")
    for linea in archivo:
        contador_derecha += 1
        if(linea[0] == "+"): break
        dprint(linea)

def cargarTextoIzquierda():
    """
    Esta función permite cargar la historia por el camino izquierdo.
    """
    global contador_izquierda
    archivo = open("../Juego/Historia_to_load/parte1/decision_izquierda.txt", "r", encoding = 'utf-8')
    archivo = archivo.readlines()
    archivo = archivo[contador_izquierda:]
    dprint("")
    for linea in archivo:
        contador_izquierda += 1
        if(linea[0] == "-"): break
        dprint(linea)

# Funciones para jugar
def juego(state):
    """
    Esta función es la que recive los comandos y los verifica en caso que
    estén malos, sino retorna el comando y se pasa a verificar en la
    máquina de estados.
    """
    cargarTexto()
    x = input("/> ")
    x = x.lower().split()
    veracidad = True
    while(veracidad):
        if(x[0] in comandos_niveles[state - 1]):
            for comando in comandos_niveles[state - 1]:
                if(x[0] == comando): veracidad = evaluar_comando(x)
        if(not veracidad): break
        dprint("Comando no reconocido.")
        x = input("/> ")
        x = x.lower().split()
    return x

# Función principal
def stateMachine():
    """
    Esta función permite simular la máquina de estados de todo el
    juego, los states no son los nodos, solo son estados que fueron
    determinados por el programador según los nodos que se avanzaban
    en la historia, es decir, cada estado necesariamente no debe
    representar un solo nodo, puede representar varios según como
    se vaya a procesar la historia, esto puede variar.
    """
    global contador, contador_izquierda, contador_derecha
    contador, contador_izquierda, contador_derecha = 0, 0, 0
    state = 1
    end = True
    while(end):
        if(state == 1):
            sound(1)
            comando = juego(state)
            print("")
            if(comando[0] == "go"):
                sound(2)
                state = 2
                cargarTextoIzquierda()
                time.sleep(16)
            elif(comando[0] == "stay"):
                end = False
                cargarTextoDerecha()
                time.sleep(10)
                imprimirFinal()
        elif(state == 2):
            sound(3)
            comando = juego(state)
            print("")
            if(comando[0] == "follow"):
                state = 3
                cargarTextoIzquierda()
                time.sleep(6)
            elif(comando[0] == "return"):
                end = False
                cargarTextoDerecha()
                time.sleep(20)
                imprimirFinal()
        elif(state == 3):
            comando = juego(state)
            print("")
            if(comando[0] == "take"):
                cargarTextoIzquierda()
                time.sleep(30)
            elif(comando[0] == "straight"):
                cargarTextoDerecha()
                time.sleep(60)
            state = 4
        elif(state == 4):
            comando = juego(state)
            print("")
            if(comando[0] == "go"):
                cargarTextoDerecha()
            elif(comando[0] == "send"):
                state = 5
                cargarTextoIzquierda()
                time.sleep(20)
        elif(state == 5):
            comando = juego(state)
            print("")
             