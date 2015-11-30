#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import time
import RPi.GPIO as GPIO

def gpio_init():

  #print GPIO.VERSION
  # RPi.GPIO Layout verwenden (wie Pin-Nummern)
  GPIO.setmode(GPIO.BOARD)

  # Pin 18 (GPIO 24) auf Input setzen
  GPIO.setup(18, GPIO.IN)

  #GPIO.add_event_detect(18,GPIO.BOTH) # add rising edge detection on a channel

  # Pin 11 (GPIO 17) auf Output setzen
  GPIO.setup(11, GPIO.OUT)

  # LED anmachen
  GPIO.output(11, GPIO.HIGH)

BtnHigh = True
BtnLowCnt = 0
BtnLowCntExit = 0

def gpio_dispatcher():#alle 100 ms
  global BtnHigh
  global BtnLowCnt
  global BtnLowCntExit

  if GPIO.input(18) == GPIO.HIGH:
    if not BtnHigh:
      BtnHigh = True
      print 'gpio changed to High, time in Seconds = ',(BtnLowCnt*0.1) 
      BtnLowCntExit = 0
      if BtnLowCnt >= 5:
        BtnLowCnt = 0
        return 'LONG RELEASE'
      else:
        BtnLowCnt = 0
        return 'RELEASE'
  elif GPIO.input(18) == GPIO.LOW:
    if BtnHigh:
      BtnHigh = False      
    BtnLowCnt = BtnLowCnt + 1
    BtnLowCntExit = BtnLowCntExit + 1
  if BtnLowCntExit >= 30:
    BtnLowCntExit = 1
    return 'EXIT'

  return 0

gpio_init()

counter = 0
# Dauersschleife
while 1:
  time.sleep(0.1)

  n = gpio_dispatcher()

  if n == 'EXIT':
    print 'EXIT received from gpio_dispatcher'
    break
  elif n == 'RELEASE':
    print 'RELEASE received from gpio_dispatcher'
  elif n == 'LONG RELEASE':
    print 'LONG RELEASE received from gpio_dispatcher'

#  counter = counter+1
  if counter >= 100:
    break # stops the loop

  #print('gpio 18 event_detected')
  counter = counter+1

  # GPIO lesen
#  if GPIO.input(18) == GPIO.HIGH:
#    print 'gpio high'

#  elif GPIO.input(18) == GPIO.LOW:
#    print 'gpio low'



#hinter dem while loop
GPIO.cleanup(18)
GPIO.cleanup(11)



"""
import datetime as dt

timeHigh = dt.datetime.now()
timeLow = dt.datetime.now()
def dauer_gpio_pressed(IsHigh):#returns dauer in Sekunden
  global timeHigh
  global timeLow

  if IsHigh:#Messung beendet
    timeHigh = dt.datetime.now()
    #print 'dauer_gpio_pressed IsHigh', timeHigh
    tmpTime = (timeHigh-timeLow)
    print 'tmpTime in Sekunden: ', (tmpTime.seconds + tmpTime.microseconds/1e6)
    return (tmpTime.seconds + tmpTime.microseconds/1e6)
  else: #IsLow
    timeLow = dt.datetime.now()
    #print 'dauer_gpio_pressed IsLow', timeLow
    return 0
"""
