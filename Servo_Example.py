#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import xbox
import sys

# Initialise the PWM device using the default address
pwm = PWM(0x40, debug=True)
joy = xbox.Joystick()


servoClockwise = 1.6
servoCounterCW = 1.4
servoStop      = 1.5
freq           = 60

def setServoPulse(channel, pulse):
  pulseLength = 1000000
  pulseLength //= freq
  pulseLength //=4096
  pulse *=1000
  print "pulseLength is %d" % pulseLength
  pulse //= pulseLength
  pulse = int(pulse)
  print "Pulse was %d bits" % pulse
  pwm.setPWM(channel, 0, pulse)


pwm.setPWMFreq(freq)                        # Set frequency to 60 Hz


while (True):
  # Change speed of continuous servo on channel O
  if joy.A():
    try:
      setServoPulse(0,servoClockwise)
    except:
      print("Unhandled error:", sys.exc_info()[0])
      joy.close()
      raise
  elif joy.B():
    try:
      setServoPulse(0,servoCounterCW)
    except:
      print("Unhandled error:", sys.exc_info()[0])
      joy.close()
      raise
  elif joy.X():
    try:
      setServoPulse(0,servoStop)
      joy.close()
    except:
      print("Unhandled error:", sys.exc_info()[0])
      joy.close()
      raise
    break
  else:
    setServoPulse(0,servoStop)    
  


