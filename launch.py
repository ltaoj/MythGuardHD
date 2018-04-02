#!/usr/bin/python
# -*- coding: UTF-8 -*-

# provide web service to control the hardware(gpio)
# date: 2018-04-02 01:26:45
# author: ltaoj

import sys
import RPi.GPIO as GPIO

from flask import Flask, request, jsonify

app = Flask(__name__)

# param:level value:{1, 0}
@app.route('/guard/control/door', methods=['POST', 'GET'])
def door():
    error = None
    level = request.args.get('level')
    try:
        if int(level) == 0:
            close_door()
        elif int(level) == 1:
            open_door()
        else:
            raise Exception("only 0 and 1 support")
    except Exception:
        response_failed = {"code": 0, "type": get_type(level), "msg": "failed"}
        return jsonify({"json": response_failed})
    response_ok = {"code": 1, "type": get_type(level), "msg": "success"}
    return jsonify({"json": response_ok})

# open the door
# output high
def open_door():
    GPIO.setwarnings(False)
    # 设置BCM编码
    GPIO.setmode(GPIO.BCM)
    pin = 17
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    print('door opend')

# close the door
# output low
def close_door():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    pin = 17
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    print('door closed')

def get_type(level):
    return "open" if int(level) == 1 else "close" if int(level) == 0 else None

if __name__ == '__main__':
    app.run(host='0.0.0.0')
