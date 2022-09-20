import time
from openal import * 


def sound(s):
	oalQuit()
	x_pos = 0
	y_pos = 0
	z_pos = 0
	sleepTime = 0
	if s == 0:
		source = oalOpen("../Juego/Sonidos/menu.wav")
		sleepTime = 2
	elif s == 1:
		source = oalOpen("../Juego/Sonidos/intro.wav")
		sleepTime = 1
	elif s == 2:
		source = oalOpen("../Juego/Sonidos/bus.wav")
		sleepTime = 1
	elif s == 3:
		source = oalOpen("../Juego/Sonidos/bus.wav")
		sleepTime = 1
	# elif s == 4:


	source.set_position([x_pos, 0, 0])
	source.set_looping(True)
	source.play()
	listener = Listener()
	listener.set_position([0, 0, 0])
	time.sleep(sleepTime)
	# while True:
	#     source.set_position([x_pos, y_pos, z_pos])
	#     print("Playing at: {0}".format(source.position))
	#     time.sleep(sleep_time)
	#     x_pos += 0.1

	
    