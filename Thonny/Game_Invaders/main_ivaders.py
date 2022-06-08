## Fork: https://github.com/printnplay/Pico-MicroPython/blob/main/picoinvaders.py
#Pico Invaders!
#
# TODO : Implement alien shots, Shields, Sound
from machine import Pin, ADC, PWM, SoftI2C, Signal
from SSD1306 import SSD1306_I2C
from time import sleep_ms
import framebuf
import random

# The MIT License (MIT)
# Copyright (c) 2021 Mike Teachman
# https://opensource.org/licenses/MIT

# example for MicroPython rotary encoder

import sys
if sys.platform == 'esp8266' or sys.platform == 'esp32':
    from rotary_irq_esp import RotaryIRQ
elif sys.platform == 'pyboard':
    from rotary_irq_pyb import RotaryIRQ
elif sys.platform == 'rp2':
    from rotary_irq_rp2 import RotaryIRQ
else:
    print('Warning:  The Rotary module has not been tested on this platform')

import time


r = RotaryIRQ(pin_num_clk=37,
              pin_num_dt=36,
              min_val=-64,
              max_val=64,
              reverse=False,
              range_mode=RotaryIRQ.RANGE_WRAP)



# Resilution 8192px 
WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height


rst = Pin(16, Pin.OUT)
rst.value(1)
i2c = SoftI2C(scl=Pin(15), sda=Pin(4))
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display

sWidth =1
select1 = Signal(Pin(38, Pin.IN), invert=True)
val_old = 0
r.set(value= -124)

pattern = [
    '0b110000001100000011111111111111111100000011000000', 
    '0b000000110000001111111111111111110000001100000011', #T
    '0b001111000100001010000001100000010100001000111100', #O
    '0b111111110000010000001000000100000010000011111111', #N
    '0b000001110000110011111000111110000000110000000111', #Y
    "0b000110000001100000111100111111111111111101011010", #ship1
    '0b111111111111111010110100001100000011000001111001',
    # '0b010110101111111111111111001111000001100000011000', #ship1 reversed
    '0b11111111111111111111111111111111111111111111111100000111111111111111111111111111111111111111111111111111111111111111111111111111',
    '0b1111_1111_1111_1111_1111_1111_111101',
    '0b111111111111111111111111111111111111111111111111111111111111',
    '0b1111_1111_1111_1111_1111_1111_111101',
    '0b100000000111111111000000111111110100000010000000010000001000000011000000111111111000000001111111'
    ]

patternX = pattern[5]

test = 'hello world'

# https://stackoverflow.com/questions/2150108/efficient-way-to-rotate-a-list-in-python
def list_append2(data, shift):
    tmp = data[shift:]
    tmp += data[:shift]
    # print('shift = {}'.format(shift))
    return tmp

# for x in range(len(patternY)):
def matrixShift(matrixString, shift):
    patternY = list(matrixString[2:])
    # patternY.reverse()
    patternY = list_append2(patternY, shift)
    patternY.insert(0, '0b')
    patternRevs = ''
    for x in patternY:
        # print(x)
        patternRevs += str(x)
    return patternRevs

def matrixReverse(matrixString):
    patternY = list(matrixString[2:])
    patternY.reverse()
    patternY.insert(0, '0b')
    patternRevs = ''
    for x in patternY:
        # print(x)
        patternRevs += str(x)
    return patternRevs

def makeMatrix(matrixString):
    num0x0Base = int(matrixString).to_bytes(6,'little')
    num0x0 = bytearray(num0x0Base)
    return  num0x0

def compileMatrix(matrixString, shift):
    # print('shift = {}'.format(shift))
    x = matrixShift(matrixString, shift)
    return framebuf.FrameBuffer(makeMatrix(x), 8, 6, framebuf.MONO_HLSB, sWidth)

x = {
    'ship' : pattern[5],
    'shift' : 0,
    'home' : 60
    }

y = {
    'ship' : pattern[5],
    # 'shift' : (len(pattern[5])- 2) // 3,
    'shift' : 4555,
    'home' : 15
    }

shipsX = [x, y]




def controls(objects = []):
    print('IN: controls: {}'.format(objects[0]))
    global val_old
    val_new = r.value()
    if val_old != val_new:
        deltaX = val_old - val_new
        print('delta: {2} - {3} = {1} home: {0}'.format(deltaX, objects[0]['home'], val_old, val_new))
        val_old = val_new
        objects[0]['home'] += deltaX
#         print('delta: {2} - {3} = {1} home: {0}'.format(deltaX, objects[0]['home'], val_old, val_new))
        print('home: {0}'.format(objects[0]['home']))     

# Clear the oled display in case it has junk on it.
def renderX(matrixString):
#     print('IN: renderX')
    global val_old
    for sysTic in range(5000):
        controls(matrixString)
        oled.fill(0)
        oled.blit(compileMatrix(matrixString[0]['ship'], matrixString[0]['shift']), matrixString[0]['home'], 0)
        sleep_ms(16)
        oled.show()

renderX(shipsX)
# def test(c = 0):
#     print('TEST START')
#     for x in range(c):
#         val_old = r.value()
#         controls()
#         sleep_ms(16)
#     print('TEST END')    
# 
# test(5000)
print("RUN COMPLETE")        