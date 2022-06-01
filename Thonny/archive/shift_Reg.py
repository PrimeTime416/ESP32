import esp32, machine, ubinascii 
print(help('modules'))
print(dir(machine.I2C))
print(dir(esp32))
from machine import Pin, I2C

i2c = I2C(0, scl=Pin(22), sda=Pin(23), freq=100000)
for i in i2c.scan():
    print(hex(i), i)           # scan for slave devices

i2c.writeto(56, b'\xf0')
readX = i2c.readfrom(57, 1)
print(readX)
print(int.from_bytes(readX, "little") )
print(bin(int.from_bytes(readX, "little") ))
# print(bin(77))
# up:  xfc:
# RT: Push: xbc:
# DW:
# LT:
# PUSH:
# CTR:
# i2c.writeto(56, b'\x0F')