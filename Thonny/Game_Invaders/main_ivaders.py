## Fork: https://github.com/printnplay/Pico-MicroPython/blob/main/picoinvaders.py
#Pico Invaders!
#
# TODO : Implement alien shots, Shields, Sound
from machine import Pin, ADC, PWM, SoftI2C, Signal
from SSD1306 import SSD1306_I2C
from time import sleep_ms
import framebuf
import random

# Resilution 8192px 
WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height


rst = Pin(16, Pin.OUT)
rst.value(1)
i2c = SoftI2C(scl=Pin(15), sda=Pin(4))
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display

sWidth =1
select1 = Signal(Pin(38, Pin.IN), invert=True) 
# select1 = Pin(38, Pin.IN) 
roteA = Pin(37, Pin.IN)
roteB = Pin(36, Pin.IN)



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
    'home' : 5
    }

y = {
    'ship' : pattern[5],
    # 'shift' : (len(pattern[5])- 2) // 3,
    'shift' : 4555,
    'home' : 15
    }

shipsX = [x, y]

# # Clear the oled display in case it has junk on it.
# def renderX(matrixString):
#     for runX in range(11):
#         oled.fill(0)
#         for x in matrixString:
#             # print(y)
#             # print(x)
#             oled.blit(compileMatrix(x['ship'], x['shift']), x['home'], runX)
#             # oled.blit(compileMatrix(x[1]['ship'], x[1]['shift']), 15, runX)
#             # oled.blit(compileMatrix(matrixString), 5, x)
#         # Finally update the oled display so the image & text is displayed
#         sleep(.01)
#         # print(x)
#         oled.show()

# Clear the oled display in case it has junk on it.
def renderX(matrixString):
    runX = 0
    for sysTic in range(500):
        runX += select1.value()
#         print('select1: {}'.format(runX))
#         print('roteA: {}'.format(roteA.value()))
#         print('roteB: {}'.format(roteB.value()))
        oled.fill(0)
        for x in matrixString:
            oled.blit(compileMatrix(x['ship'], x['shift']), x['home'], runX)
        sleep_ms(16)
        oled.show()

renderX(shipsX)
print("RUN COMPLETE")        


