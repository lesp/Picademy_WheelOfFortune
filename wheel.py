import pibrella
from time import sleep
from random import randint

def spinwheel(pin):
	#pibrella.light.blink(0.5,0.5)
	duration = randint(1,10)
    print(duration)
    pibrella.output.e.on()
    sleep(duration)
    pibrella.output.e.off()
    #pibrella.light.off()


pibrella.button.pressed(spinwheel)
    
