#! /usr/bin/env python
"""\
Scan ports

"""

import serial

def scan():
    available = []
    for i in range(256):
        try:
            s = serial.Serial(i)
            available.append( (i, s.portstr))
            s.close()
        except serial.SerialException:
            pass
    return available

def run():
    print "Ports:"
    for n,s in scan():
        print "(%d) %s" % (n,s)
