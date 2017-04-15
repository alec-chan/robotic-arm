#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import xbox


# Initialise the PWM device using the default address
pwm = PWM(0x40, debug=True)
joy = xbox.Joystick()


servoClockwise = 0.0020
servoCounterCW = 0.0010
servoStop      = 0.0015


def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)


pwm.setPWMFreq(60)                        # Set frequency to 60 Hz


while (True):
  # Change speed of continuous servo on channel O
  if joy.A():
    setServoPulse(0,servoClockwise)
  elif joy.B():
    serServoPulse(0,servoCounterCW)
  elif joy.X():
    setServoPulse(0,servoStop)
    break    
  


