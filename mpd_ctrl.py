#!/usr/bin/env python
# -*- coding: utf-8 -*-
### -*- coding: iso-8859-1 -*-

import subprocess

#mpd_ctrl.py control mpd over mpc

class mpcCtrl:
    
    info = 'this is a mpcCtrl Class' # class variable shared by all instances

    def __init__(self, name):
        self.position = 0   # instance variable unique to each instance
        self.verbose = 1
        self.sender = []    # creates a new empty list
        self.clear()

    def addSender(self, sender):
        self.sender.append(sender)
        self.position = len(self.sender)-1

    def getPosition(self):
        return self.position

    def getSenderAtCurrentPos(self):
        if len(self.sender)-1 >= self.position:
            return self.sender[self.position]
        else:
            return 0

    def play(self):
        s = self.getSenderAtCurrentPos()
        if s:
            subprocess.call(["mpc","add",s])
            #subprocess.call(["mpc","playlist"])
            subprocess.call(["mpc","play"])

    def nextSender(self):
        self.position = self.position+1
        if self.position >= len(self.sender):
            self.position = 0;
        if 1 == self.verbose:
            print 'nextSender',self.position
        self.clear()
        self.play()

    def prevSender(self):
        self.position = self.position-1
        if self.position < 0:
            self.position = len(self.sender)-1;
        if 1 == self.verbose:
            print 'prevSender',self.position
        self.clear()
        self.play()
        
    def printSender(self):
        for string in self.sender:
            print 'Sender',string

    def clear(self):
        subprocess.call(["mpc","clear"])

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
