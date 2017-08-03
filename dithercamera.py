# coding: utf-8

# Dither Camera for RPi Zero W
# Python source code
# NADA ELECTRONICS, LTD.
# By. Takehiro Yamaguchi

import commands
import time
import picamera
import RPi.GPIO as GPIO

# Button
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(18) == GPIO.LOW:
        with picamera.PiCamera() as camera:
            camera.resolution = (1024, 768)
            camera.rotation = 270
            #camera.start_preview()
            time.sleep(1)
            camera.capture('image.bmp', format = 'bmp', resize=(512, 384))
            check = commands.getoutput("convert foo.bmp -rotate 90 -modulate 170 -colorspace Gray  -ordered-dither o4x4 -colors 2 -depth 1 image1.bmp")
            #print check
            # Image Ptinting
            check = commands.getoutput("sudo python imageprn.py")
            #print check

