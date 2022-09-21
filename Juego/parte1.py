"""
Codificación del Misterio de Albus, funciones para cargar la
historia del juego, jugarlo y ejecutar los sonidos del juego.
"""

from distutils.errors import LibError
from os import system
import time
from OpenAl import *

# Variables Globales
comandos_niveles = [
    ["go", "stay"],  ["follow", "return"], 
    ["take", "straight"], ["send", "go"],
    ["go"], ["read", "throw"], ["go", "stay"]
]
formato_comandos = {
    "go": [["alderaan", "home", "out", "house", "jefatura"], 1], 
    "stay": [[], 0], "follow": [["guy"], 1], "return": [["home"], 1],
    "send": [["message"], 1], "take": [["atajo"], 1],
    "straight": [[], 0], "read": [["letter"], 1],
    "throw": [[], 0]
} # El formato de los comandos tiene los comandos y una pareja de las palabras que se deben colocar y la cantida de palabras que vienen después de comando que es el entero.
contador = 0
contador_derecha = 0
contador_izquierda = 0

def dprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.010)
    
# Funciones para el final
def imprimirFinal():
    """
    Esta función imprime el final en caso de que se llegue a un final del juego.
    """
    system("cls")
    print("======================================================================================================")
    dprint("FIN DEL JUEGO.\n")
    dprint("Esperamos que te haya gustado, recuerda que hay más de un solo final, puedes volver a iniciar y \n")
    dprint("recorrer todos los finales que tiene el juego.\n")
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
            print(linea)
            if(jugar == 2):
                break
        elif(jugar == 0):
            dprint(linea)
        elif(jugar == 1):
            print(linea)
    contador += 1

def cargarTextoDerecha(se_lee):
    """
    Esta función permite cargar las decisiones que se tomen por el
    camino derecho.
    """
    global contador_derecha
    archivo = open("../Juego/Historia_to_load/parte1/decision_derecha.txt", "r", encoding = 'utf-8')
    archivo = archivo.readlines()
    archivo = archivo[contador_derecha:]
    if(se_lee): dprint("")
    for linea in archivo:
        contador_derecha += 1
        if(linea[0] == "+"): break
        if(se_lee): dprint(linea)

def cargarTextoIzquierda(se_lee):
    """
    Esta función permite cargar la historia por el camino izquierdo.
    """
    global contador_izquierda
    archivo = open("../Juego/Historia_to_load/parte1/decision_izquierda.txt", "r", encoding = 'utf-8')
    archivo = archivo.readlines()
    archivo = archivo[contador_izquierda:]
    if(se_lee): dprint("")
    for linea in archivo:
        contador_izquierda += 1
        if(linea[0] == "-"): break
        if(se_lee): dprint(linea)

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
        dprint("Comando no reconocido.\n")
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
                cargarTextoIzquierda(True)
                cargarTextoDerecha(False)
                time.sleep(11)
            elif(comando[0] == "stay"):
                sound(8)
                end = False
                cargarTextoDerecha(True)
                time.sleep(10)
                imprimirFinal()
        elif(state == 2):
            sound(3)
            comando = juego(state)
            print("")  
            if(comando[0] == "follow"):
                sound(4)
                state = 3
                cargarTextoIzquierda(True)
                cargarTextoDerecha(False)
                time.sleep(6)
            elif(comando[0] == "return"):
                sound(8)
                end = False
                cargarTextoDerecha(True)
                imprimirFinal()
        elif(state == 3):
            sound(5)
            comando = juego(state)
            print("")
            if(comando[0] == "take"):
                sound(6)
                cargarTextoIzquierda(True)
                cargarTextoDerecha(False)
            elif(comando[0] == "straight"):
                sound(9)
                cargarTextoDerecha(True)
                cargarTextoIzquierda(False)
            state = 4
        elif(state == 4):
            sound(6)
            comando = juego(state)
            print("")
            if(comando[0] == "go"):
                sound(10)
                cargarTextoDerecha(True)
                cargarTextoIzquierda(False)
            elif(comando[0] == "send"):
                sound(7)
                cargarTextoIzquierda(True)
                cargarTextoDerecha(False)
            state = 5
        elif(state == 5):
            sound(1)
            comando = juego(state)
            print("")
            if(comando[1] == "house"):
                sound(3)
                cargarTextoIzquierda(True)
                cargarTextoDerecha(False)
                time.sleep(5)
            elif(comando[1] == "jefatura"):
                sound(12)
                cargarTextoDerecha(True)
                cargarTextoIzquierda(False)
                time.sleep(10)
            state = 6
        elif(state == 6):
            comando = juego(state)
            print("")
            if(comando[0] == "read"):
                sound(11)
                time.sleep(5)
                sound(8)
                end = False
                cargarTextoIzquierda(True)
                imprimirFinal()
            elif(comando[0] == "throw"):
                sound(13)
                cargarTextoDerecha(True)
                cargarTextoIzquierda(False)
                time.sleep(7)
                state = 7
        elif(state == 7):
            sound(1)
            comando = juego(state)
            print("")
            if(comando[0] == "go"):
                sound(2)
                time.sleep(5)
                sound(8)
                cargarTextoIzquierda(True)
            elif(comando[0] == "stay"):
                sound(8)
                cargarTextoDerecha(True)
            end = False
            time.sleep(10)
            imprimirFinal()

             