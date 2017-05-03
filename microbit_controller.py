# code to be placed on the battery powered microbit controller
from microbit import *
import radio

radio.on()

while True:
    my_send = accelerometer.get_values()                # Get acc data
    radio.send(str(my_send[0])+"," + str(my_send[1]))   # Send only x and y data as comma separated string
    sleep(800)                                          # Slow down input process
  
