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
		source = oalOpen("../Juego/Sonidos/crowd.wav")
		sleepTime = 0
		config(x_pos,y_pos,z_pos,sleepTime,source)
	elif s == 4:
		source = oalOpen("../Juego/Sonidos/park.wav")
		sleepTime = 1
		config(x_pos,y_pos,z_pos,sleepTime,source)

	
	# while True:
	#     source.set_position([x_pos, y_pos, z_pos])
	#     print("Playing at: {0}".format(source.position))
	#     time.sleep(sleep_time)
	#     x_pos += 0.1

	
    