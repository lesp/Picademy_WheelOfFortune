import pibrella
from time import sleep
from random import randint
import signal

global duration
duration = randint(1,10)

def spinwheel(pin):
    global duration
    pibrella.output.e.on()
    sleep(duration)
    pibrella.output.e.off()


pibrella.button.changed(spinwheel)
    
