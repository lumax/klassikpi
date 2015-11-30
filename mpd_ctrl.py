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
        if 0 == len(self.sender):
            return
        self.position = self.position+1
        if self.position >= len(self.sender):
            self.position = 0;
        if 1 == self.verbose:
            print 'nextSender',self.position
        self.clear()
        self.play()

    def prevSender(self):
        if 0 == len(self.sender):
            return
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
