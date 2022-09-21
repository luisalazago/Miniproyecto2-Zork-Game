"""
Archivo de OpenAL para cargar los sonidos dentro del juego
con distintos tiempos y manejo de espacios.
"""

import time
from openal import * 

def config(x,y,z,sleep,source):
	source.set_position([x, 0, 0])
	source.set_looping(True)
	source.play()
	listener = Listener()
	listener.set_position([0, 0, 0])
	time.sleep(sleep)

def sound(s):
	oalQuit()
	x_pos = 0
	y_pos = 0
	z_pos = 0
	sleepTime = 0
	if s == 0:
		source = oalOpen("../Juego/Sonidos/menu.wav")
		sleepTime = 2
		config(x_pos,y_pos,z_pos,sleepTime,source)
	elif s == 1:
		source = oalOpen("../Juego/Sonidos/intro.wav")
		sleepTime = 1
		config(x_pos,y_pos,z_pos,sleepTime,source)
	elif s == 2:
		source = oalOpen("../Juego/Sonidos/bus.wav")
		sleepTime = 1
		config(x_pos,y_pos,z_pos,sleepTime,source)
	elif s == 3:
		source = oalOpen("../Juego/Sonidos/crowd_park.wav")
		sleepTime = 0
		config(x_pos,y_pos,z_pos,sleepTime,source)
	elif s == 4:
		source = oalOpen("../Juego/Sonidos/running.wav")
		sleepTime = 1
		config(x_pos,y_pos,z_pos,sleepTime,source)
	elif s == 5:
		source = oalOpen("../Juego/Sonidos/breath.wav")
		sleepTime = 1
		config(x_pos,y_pos,z_pos,sleepTime,source)
	elif s == 6:
		source = oalOpen("../Juego/Sonidos/crowd.wav")
		sleepTime = 0
		config(x_pos,y_pos,z_pos,sleepTime,source)
	elif s == 7:
		source = oalOpen("../Juego/Sonidos/writing_police.wav")
		sleepTime = 0
		config(x_pos,y_pos,z_pos,sleepTime,source)
	elif s == 8:
		source = oalOpen("../Juego/Sonidos/end.wav")
		sleepTime = 0
		config(x_pos,y_pos,z_pos,sleepTime,source)
	elif s == 9:
		source = oalOpen("../Juego/Sonidos/steps.wav")
		sleepTime = 0
		config(x_pos,y_pos,z_pos,sleepTime,source)
	elif s == 10:
		source = oalOpen("../Juego/Sonidos/reporter.wav")
		sleepTime = 0
		config(x_pos,y_pos,z_pos,sleepTime,source)
	elif s == 11:
		source = oalOpen("../Juego/Sonidos/paper.wav")
		sleepTime = 0
		config(x_pos,y_pos,z_pos,sleepTime,source)
	elif s == 12:
		source = oalOpen("../Juego/Sonidos/police.wav")
		sleepTime = 0
		config(x_pos,y_pos,z_pos,sleepTime,source)
	elif s == 13:
		source = oalOpen("../Juego/Sonidos/throwing.wav")
		sleepTime = 0
		config(x_pos,y_pos,z_pos,sleepTime,source)
	
	
    