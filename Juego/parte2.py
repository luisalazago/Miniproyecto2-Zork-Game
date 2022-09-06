"""
Codificación del Misterio de Albus PARTE 2
"""

from distutils.errors import LibError
from os import system
import time

comandos_niveles = [["realize"], ["hire"], ["friend", "police"], ["investigate", "police"], ["guilty"], ["evidence"], ["guilty"], ["read", "not read"], ["realize"], ["town", "die"], ["end"], ["letter"], ["end"], [], ["read"], []]

def cargarTexto(contador, des):
    jugar = 0
    camino = 0
    archivo = open("../Juego/Historia_to_load/parte2.txt", "r")
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

def stateMachine2():
	state = 19
	contador = 0
	end = True
	
	while(end):
		if(state == 19):
			contador = cargarTexto(contador, None)
			x = input("/> ")
            x = x.lower().split()
            while(x[0] not in comandos_niveles[0]):
                print("Comando no reconocido.")
                x = input("/> ")
                x = x.lower().split()
            if(x[0] == "realize"):
                state = 20
                contador = cargarTexto(contador, 1)
                time.sleep(6)
            
		elif(state == 20):
			contador = cargarTexto(contador, None)
			x = input("/> ")
            x = x.lower().split()
            while(x[0] not in comandos_niveles[1]):
                print("Comando no reconocido.")
                x = input("/> ")
                x = x.lower().split()
            if(x[0] == "hire"):
                state = 21
                contador = cargarTexto(contador, 1)
                time.sleep(6)

		elif(state == 21):
			contador = cargarTexto(contador, None)
			x = input("/> ")
            x = x.lower().split()
            while(x[0] not in comandos_niveles[2]):
                print("Comando no reconocido.")
                x = input("/> ")
                x = x.lower().split()
            if(x[0] == "friend"):
                state = 22
                contador = cargarTexto(contador, 1)
                time.sleep(6)
            elif(x[0] == "police"):
                state = 23
                contador = cargarTexto(contador, 1)
                time.sleep(6)

		elif(state == 22):
			contador = cargarTexto(contador, None)
			x = input("/> ")
            x = x.lower().split()
            while(x[0] not in comandos_niveles[3]):
                print("Comando no reconocido.")
                x = input("/> ")
                x = x.lower().split()
            if(x[0] == "investigate"):
                state = 24
                contador = cargarTexto(contador, 1)
                time.sleep(6)
            elif(x[0] == "police"):
                state = 23
                contador = cargarTexto(contador, 1)
                time.sleep(6)

		elif state == 23:
			contador = cargarTexto(contador, None)
			x = input("/> ")
            x = x.lower().split()
            while(x[0] not in comandos_niveles[4]):
                print("Comando no reconocido.")
                x = input("/> ")
                x = x.lower().split()
            if(x[0] == "guilty"):
                state = 26
                contador = cargarTexto(contador, 1)
                time.sleep(6)

		elif state == 24:
			contador = cargarTexto(contador, None)
			x = input("/> ")
            x = x.lower().split()
            while(x[0] not in comandos_niveles[5]):
                print("Comando no reconocido.")
                x = input("/> ")
                x = x.lower().split()
            if(x[0] == "evidence"):
                state = 25
                contador = cargarTexto(contador, 1)
                time.sleep(6)

		elif state == 25:
			contador = cargarTexto(contador, None)
			x = input("/> ")
            x = x.lower().split()
            while(x[0] not in comandos_niveles[6]):
                print("Comando no reconocido.")
                x = input("/> ")
                x = x.lower().split()
            if(x[0] == "guilty"):
                state = 26
                contador = cargarTexto(contador, 1)
                time.sleep(6)

		elif state == 26:
			contador = cargarTexto(contador, None)
			x = input("/> ")
            x = x.lower().split()
            while(x[0] not in comandos_niveles[7]):
                print("Comando no reconocido.")
                x = input("/> ")
                x = x.lower().split()
            if(x[0] == "letter"):
                state = 27
                contador = cargarTexto(contador, 1)
                time.sleep(6)

		elif state == 27:
			contador = cargarTexto(contador, None)
			x = input("/> ")
            x = x.lower().split()
            while(x[0] not in comandos_niveles[8]):
                print("Comando no reconocido.")
                x = input("/> ")
                x = x.lower().split()
            if(x[0] == "read"):
                state = 28
                contador = cargarTexto(contador, 1)
                time.sleep(6)
            if(x[0] == "not read"):
                state = 29
                contador = cargarTexto(contador, 1)
                time.sleep(6)

		elif state == 28:
			contador = cargarTexto(contador, None)
			x = input("/> ")
            x = x.lower().split()
            while(x[0] not in comandos_niveles[9]):
                print("Comando no reconocido.")
                x = input("/> ")
                x = x.lower().split()
            if(x[0] == "realize"):
                state = 30
                contador = cargarTexto(contador, 1)
                time.sleep(6)

		elif state == 29:
			contador = cargarTexto(contador, None)
			x = input("/> ")
            x = x.lower().split()
            while(x[0] not in comandos_niveles[10]):
                print("Comando no reconocido.")
                x = input("/> ")
                x = x.lower().split()
            if(x[0] == "town"):
                state = 31
                contador = cargarTexto(contador, 1)
                time.sleep(6)
            elif(x[0] == "die"):
                state = 32
                contador = cargarTexto(contador, 1)
                time.sleep(6)

		elif state == 30:
			contador = cargarTexto(contador, None)
			x = input("/> ")
            x = x.lower().split()
            while(x[0] not in comandos_niveles[11]):
                print("Comando no reconocido.")
                x = input("/> ")
                x = x.lower().split()
            if(x[0] == "end"):
                state = 33
                contador = cargarTexto(contador, 1)

		elif state == 31:
			contador = cargarTexto(contador, None)
			x = input("/> ")
            x = x.lower().split()
            while(x[0] not in comandos_niveles[12]):
                print("Comando no reconocido.")
                x = input("/> ")
                x = x.lower().split()
            if(x[0] == "letter"):
                state = 34
                contador = cargarTexto(contador, 1)

		elif state == 32:
			contador = cargarTexto(contador, None)
			x = input("/> ")
            x = x.lower().split()
            while(x[0] not in comandos_niveles[13]):
                print("Comando no reconocido.")
                x = input("/> ")
                x = x.lower().split()
            if(x[0] == "end"):
                state = 35
                contador = cargarTexto(contador, 1)

		elif state == 33:
			end == False

		elif state == 34:
			contador = cargarTexto(contador, None)
			x = input("/> ")
            x = x.lower().split()
            while(x[0] not in comandos_niveles[13]):
                print("Comando no reconocido.")
                x = input("/> ")
                x = x.lower().split()
            if(x[0] == "read"):
                state = 28
                contador = cargarTexto(contador, 1)

		elif state == 35:
			end == False


stateMachine2()