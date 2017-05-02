# This script merely acts to receive messages and relay them to the raspberry pi
from microbit import *
import radio


while True:
  incoming = radio.receive()
  if len(incoming) > 1:
    uart.write(incoming + "\n")
  sleep(300)
