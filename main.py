from adafruit_motorkit import MotorKit

import time

kit = MotorKit(0x40)



def FWD(t): #where t is time
  
  kit.motor1.throttle = 0.76
  kit.motor2.throttle = 0.75

  time.sleep(t)

def STOP():
  kit.motor1.throttle = 0.0
  kit.motor2.throttle = 0.0
  time.sleep(2.0)

def LEFT(t):
  kit.motor1.throttle = 0.76
  kit.motor2.throttle = -0.75 

  time.sleep(t)

def BWD(t):
  kit.motor1.throttle = -0.78
  kit.motor2.throttle = -0.75
  time.sleep(t)


def RIGHT(t):
  kit.motor1.throttle = -0.78
  kit.motor2.throttle = 0.75
  time.sleep(t)


FWD(4.1)
STOP()
LEFT(0.9) #change to right turn on second run
#RIGHT(0.9)
STOP()
FWD(2.4) 
STOP()
BWD(4.6)
STOP()
