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

# Set variables we will use to convert data to servo movement
my_buffer = 100
servo_min = 3
servo_max = 9
  


#discard first reading
startdata = s.readline()
#determine microbit starting position
startdata = s.readline().decode('UTF-8')   #check for data.  this code blocks script from moving forward until data is received.
startdatalist = startdata.rstrip().split(',')

# Set top servo starting position
GPIO.setmode(GPIO.BOARD) #declare the reference style for GPIO
GPIO.setup(servo1,GPIO.OUT) #assign pin as an output
pwm1=GPIO.PWM(servo1,50) #sets PWM for the pin
pwm1.start(5)
pwm1.changedutycycle(pointer_starty)
GPIO.cleanup()

# Set bottom servo starting position
GPIO.setmode(GPIO.BOARD) #declare the reference style for GPIO
GPIO.setup(servo2,GPIO.OUT) #assign pin as an output
pwm2=GPIO.PWM(servo2,50) #sets PWM for the pin
pwm2.start(5)
pwm2.changedutycycle(pointer_startx)
GPIO.clanup()

while True:
  # Get The Data
  data = s.readline().decode('UTF-8')   #check for data.  this code blocks script from moving forward until data is received.
  datalist = data.rstrip().split(',')

  # Convert the data to movement.  First find difference
  xdifference = datalist(0) - startdatalist(0)
  ydifference = datalist(1) - startdatalist(1)

  # Set top servo position
  GPIO.setmode(GPIO.BOARD) #declare the reference style for GPIO
  GPIO.setup(servo1,GPIO.OUT) #assign pin as an output
  pwm1=GPIO.PWM(servo1,50) #sets PWM for the pin
  pwm1.start(5)
  pwm1.changedutycycle(current_x)
  GPIO.cleanup()

  # Set bottom servo position
  GPIO.setmode(GPIO.BOARD) #declare the reference style for GPIO
  GPIO.setup(servo2,GPIO.OUT) #assign pin as an output
  pwm2=GPIO.PWM(servo2,50) #sets PWM for the pin
  pwm2.start(5)
  pwm2.changedutycycle(current_y)
  GPIO.clanup()
    
    
