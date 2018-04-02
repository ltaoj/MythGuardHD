#!/usr/bin/python 
# -*- coding: UTF-8 -*- 
 
# control gpio 
# date: 2018年03月30日18:13:25 
# author: ltaoj 
 
import sys 
import RPi.GPIO as GPIO 
 
GPIO.setwarnings(False) 
# 设置BCM编码 
GPIO.setmode(GPIO.BCM) 
args = sys.argv 
# BCM编码为17的引脚 
pin = 17

ctl = args[1]

if (int(ctl) == 1):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

if (int(ctl) == 0):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
