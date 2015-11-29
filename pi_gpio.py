import time
import RPi.GPIO as GPIO
import datetime as dt

def gpio_init():

  print GPIO.VERSION
  # RPi.GPIO Layout verwenden (wie Pin-Nummern)
  GPIO.setmode(GPIO.BOARD)

  # Pin 18 (GPIO 24) auf Input setzen
  GPIO.setup(18, GPIO.IN)

  GPIO.add_event_detect(18,GPIO.BOTH) # add rising edge detection on a channel

  # Pin 11 (GPIO 17) auf Output setzen
  GPIO.setup(11, GPIO.OUT)

timeHigh = dt.datetime.now()
timeLow = dt.datetime.now()
def dauer_gpio_pressed(IsHigh):#returns dauer in Sekunden
  global timeHigh
  global timeLow

  if IsHigh:#Messung beendet
    timeHigh = dt.datetime.now()
    #print 'dauer_gpio_pressed IsHigh', timeHigh
    tmpTime = (timeHigh-timeLow)
    print 'tmpTime: ', tmpTime
    #print 'die vergangene Zeit: ', (timeHigh-timeLow), "in Microsekunden", (tmpTime.seconds/1000+tmpTime.microsecond)/1e6
    return (timeHigh.microsecond-timeLow.microsecond)/1e6
  else: #IsLow
    timeLow = dt.datetime.now()
    #print 'dauer_gpio_pressed IsLow', timeLow
    return 0

def gpio_dispatcher():
  if GPIO.input(18) == GPIO.HIGH:
    print 'gpio high'
    print 'dauer_gpio_pressed: ',dauer_gpio_pressed(1)
  elif GPIO.input(18) == GPIO.LOW:
    print 'gpio low'
    dauer_gpio_pressed(0)

gpio_init()

counter = 0
# Dauersschleife
while 1:
  time.sleep(0.1)

#  counter = counter+1
  if counter >= 10:
    break # stops the loop

  # LED immer anmachen
  GPIO.output(11, GPIO.HIGH)

  if GPIO.event_detected(18):
    gpio_dispatcher()
    print('gpio 18 event_detected')
    counter = counter+1

  # GPIO lesen
#  if GPIO.input(18) == GPIO.HIGH:
#    print 'gpio high'

#  elif GPIO.input(18) == GPIO.LOW:
#    print 'gpio low'



#hinter dem while loop

print 'ende aus!'
GPIO.cleanup(18)
GPIO.cleanup(11)

