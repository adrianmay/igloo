#!/usr/bin/python
# Thanks to http://www.raspberrypi-spy.co.uk/2014/08/enabling-the-spi-interface-on-the-raspberry-pi/

import spidev
import time
import os
import sys

spi = spidev.SpiDev()
spi.open(0,0)

def ReadChannel(channel):
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

while True:
    for ch in range(0,8):
        v = ReadChannel(ch)
        sys.stdout.write(str(v))
        sys.stdout.write("\t")
        sys.stdout.flush()
    print
    time.sleep(1)


