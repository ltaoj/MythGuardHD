#!/usr/bin/python
# -*- coding: UTF-8 -*-

# provide web service to control the hardware(gpio)
# date: 2018-04-02 01:26:45
# author: ltaoj

import sys
import RPi.GPIO as GPIO

from flask import Flask, request

app = Flask(__name__)

# param:level value:{1, 0}
@app.route('/guard/control/door', methods=['POST', 'GET'])
def door():
    error = None
    level = request.form['level']
    if level == 0:
        closeDoor()
    elif level == 1:
        openDoor()
    else:
        pass

# open the door
# output high
def openDoor():
    GPIO.setwarnings(False)
    # 设置BCM编码
    GPIO.setmode(GPIO.BCM)
    pin = 17
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    print('door opend')

# close the door
# output low
def closeDoor():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    pin = 17
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    print('door closed')


if __name__ == '__main__':
    app.run()
