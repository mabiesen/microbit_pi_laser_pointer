# code to be placed on the battery powered microbit controller
from microbit import *
import radio

radio.on()

while True:
  my_send = accelerometer.get_values()
  display.scroll(my_send[0])
  radio.send(my_send)
  
