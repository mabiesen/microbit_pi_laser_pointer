# code to be placed on the battery powered microbit controller
from microbit import *
import radio

my_switch = True

radio.on()

def send_acc_data():
    my_send = accelerometer.get_values()                # Get acc data
    radio.send(str(my_send[0])+"," + str(my_send[1]))   # Send only x and y data as comma separated string
    sleep(800)    

while True:
    if button_a.was_pressed():
        send_acc_data()
    if button_b.was_pressed():
        my_switch = True
        while myswitch:
            send_acc_data():
            if button_b.was_pressed():
                my_switch = False
  
