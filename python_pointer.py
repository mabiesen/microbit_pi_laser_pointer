# Script to receive data from the microbit and use that data to move our laser pointer

import RPi.GPIO as GPIO
import serial

# Set the variables that concern our serial communication 
PORT = "/dev/ttyACM0"
BAUD = 115200
s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

# Set the variables that control our servos
servo1 = 13 #placeholder
servo2 = 16 #placeholder
pointer_startx = 6
pointer_starty = 6



def get_servo_value(myval):
  # Set variables we will use to convert data to servo movement, create coefficient
  my_buffer = 100
  servo_min = 3.0
  servo_max = 9.0
  tilt_max = 500.0
  full_tilt = tilt_max * 2
  move_val = abs(myval)/full_tilt * (servo_max - servo_min) + servo_min
  return move_val

def move_servo(myservo, mymove):
  # Set top servo position
  GPIO.setmode(GPIO.BOARD) #declare the reference style for GPIO
  GPIO.setup(myservo,GPIO.OUT) #assign pin as an output
  pwm1=GPIO.PWM(myservo,50) #sets PWM for the pin
  pwm1.start(5)
  pwm1.changedutycycle(mymove)
  GPIO.cleanup()


# Set starting position, should move at this point
#move_servo(servo1,pointer_starty)
#move_servo(servo2,pointer_startx)

while True:
  # Get The Data
  data = s.readline().decode('UTF-8')   #check for data.  this code blocks script from moving forward until data is received.
  datalist = data.rstrip().split(',')

  # Convert the data to movement. 
  current_x = get_servo_value(int(datalist[0]))
  current_y = get_servo_value(int(datalist[1]))
  
  # Print current vals to console
  print("x is %d" % current_x)
  print("y is %d" % current_y)

  # Set current servo positions
  #move_servo(servo1, current_y)
  #move_servo(servo2, current_x)
