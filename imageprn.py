# coding: utf-8

# BMP(384px 512px 1bpp) to AS-289R2
# Model:AS-289R2
# Python source code
# NADA ELECTRONICS, LTD.
# By. Takehiro Yamaguchi

import serial

# AS-289R2 Initialize
ser = serial.Serial("/dev/ttyAMA0", baudrate = 38400, timeout = 2)

# CMD DC2 F
ser.write(chr(0x12))
ser.write(chr(0x46))
ser.write(chr(0x36))

# Get BMP(384px 512px 1bpp)
file = open('image1.bmp','r')
file.seek(10)
offset = ord(file.read(1))
file.seek(22)
height = ord(file.read(1))
height += ord(file.read(1) ) * 256

# Output CMD
ser.write(chr(0x1C))
ser.write(chr(0x2A))
ser.write(chr(0x65))
n1 = height / 256
ser.write(chr(n1))
n2 = height % 256
ser.write(chr(n2))

for num in range(height):
    line = height * 48 + offset - ((num+1) * 48)
    file.seek(line)
    for  subnum in range(48):
        x = ord(file.read(1)) ^ 0xFF
        ser.write(chr(x))

for feed in range(6):
    ser.write(chr(0x0D))

file.close()
