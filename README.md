# microbit_pi_laser_pointer
Project using the microbit to send messages to raspberry pi, which will in turn move a laser pointer

## Hardware Requirements

1 raspberry pi
2 microbits
Turret containing two servos (build directions and pictures forthcoming)

## Languages Used

Everything is written in Python.

## How it works
1 microbit will be connected directly to the raspberry pi and act in the capacity of a hub.  The other microbit will be powered by battery and will be used to control motion of the laser pointer using the onboard accelerometer and compass.

So flow is as follows:
1. each of the devices are turned on. Plug the "hub" microbit into the Raspberry Pi USB port.  Plug in servos before turning on the Raspberry Pi.
2. The controller waits for the user to press "a" or "b".  If the user presses "a", a single set of coordinates will be sent to the hub microbit using radio; if "b" is pressed, the microbit will stream data until "b" is pressed again.  Anytime the controller microbit sends, the letters "se" appear on the screen.
3.  The hub microbit receives incoming data from the controller microbit.  This data is then sent directly to the Raspberry Pi through a USB connection.
4.  The Raspberry Pi will parse the incoming 

The raspberry pi in turn is connected to two servo motors(180 degree capability) which will control the x and y movements of the laser pointer
