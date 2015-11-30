#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mpd_ctrl import mpcCtrl

sender = [
    "http://stream.klassikradio.de/live/mp3-128/www.klassikradio.de",
    "http://stream.klassikradio.de/movie/mp3-128/www.klassikradio.de",
    "http://stream.klassikradio.de/newclassics/mp3-128/www.klassikradio.de",
    "http://stream.klassikradio.de/chor/mp3-128/www.klassikradio.de",
    "http://stream.klassikradio.de/lounge/mp3-128/www.klassikradio.de",
    "http://stream.klassikradio.de/lounge-beat/mp3-128/www.klassikradio.de",
    "http://stream.klassikradio.de/smooth/mp3-128/www.klassikradio.de",
    "http://stream.klassikradio.de/rockclassic/mp3-128/www.klassikradio.de",
    "http://stream.klassikradio.de/schiller/mp3-128/www.klassikradio.de",
    "http://stream.klassikradio.de/christmas/mp3-128/www.klassikradio.de",
    "http://stream.klassikradio.de/klassikrock/mp3-128/www.klassikradio.de"]

print 'Du hast',len(sender),'Sender in der Senderliste'

ctrl = mpcCtrl('derName')

print 'SenderAtCurrentPos:',ctrl.getSenderAtCurrentPos()

for s in sender:
    ctrl.addSender(s)
#ctrl.addSender(sender[0])
#ctrl.addSender(sender[1])
#ctrl.addSender(sender[2])
#ctrl.addSender(sender[3])

print 'Die momentane Position ist:',ctrl.getPosition()
#ctrl.printSender()
print 'SenderAtCurrentPos:',ctrl.getSenderAtCurrentPos()
    
help = 'mögliche Eingaben: help, exit, next, prev'

while 1:    # infinite loop
    n = raw_input()
    if n == "exit":
        ctrl.clear()
        break  # stops the loop
    elif n == "next" or n == "n":
        ctrl.nextSender()
    elif n == "prev" or n == "p":
        ctrl.prevSender()
    elif n == "help":
        print help
    else:
       print help

#nach der Dauerschleife

"""
# Dauersschleife
while 1:

  # LED immer ausmachen
  GPIO.output(11, GPIO.HIGH)

  time.sleep(0.1)



  # GPIO lesen
  if GPIO.input(18) == GPIO.HIGH:
    # LED an
    GPIO.output(11, GPIO.HIGH)

    # Warte 100 ms
    time.sleep(0.1)

    # LED aus
    GPIO.output(11, GPIO.LOW)

    # Warte 100 ms
    time.sleep(0.1)
"""
