# This script merely acts to receive messages and relay them to the raspberry pi
from microbit import *
import radio

radio.on()

while True:
  display.scroll("d")
  incoming = radio.receive()
  if incoming:
    display.scroll(incoming)
    uart.write(incoming + "\n")
