# code to be placed on the battery powered microbit controller
from microbit import *
import radio

radio.on()

display.scroll("place on flat surface, press a")

if button_a.was_pressed():
  while True:
    my_data = accelerometer.get_values()
    mysend = str(my_data[0]) + "," + str(my_data[1]) 
    radio.send(my_send)
  
