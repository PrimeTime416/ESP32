# Fork: https://github.com/printnplay/Pico-MicroPython/blob/main/picoinvaders.py
#Pico Invaders!
#
# TODO : Implement alien shots, Shields, Sound
from machine import Pin, ADC, PWM, SoftI2C
from SSD1306 import SSD1306_I2C
from time import sleep
import framebuf
import random

# Resilution 8192px 
WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height


rst = Pin(16, Pin.OUT)
rst.value(1)

i2c = SoftI2C(scl=Pin(15), sda=Pin(4))

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display
pattern = [
    '0b110000001100000011111111111111111100000011000000', 
    '0b000000110000001111111111111111110000001100000011', #T
    '0b001111000100001010000001100000010100001000111100', #O
    '0b111111110000010000001000000100000010000011111111', #N
    '0b000001110000110011111000111110000000110000000111', #Y
    "0b000110000001100000111100111111111111111101011010",
    '0b11111111111111111111111111111111111111111111111100000111111111111111111111111111111111111111111111111111111111111111111111111111',
    '0b1111_1111_1111_1111_1111_1111_111101',
    '0b111111111111111111111111111111111111111111111111111111111111',
    '0b1111_1111_1111_1111_1111_1111_111101',
    '0b100000000111111111000000111111110100000010000000010000001000000011000000111111111000000001111111'
    ]

patternX = pattern[5]
bitLength = len(patternX) - 2
num0x0Base = int(patternX).to_bytes(6,'little')
num0x0 = bytearray(num0x0Base)
sWidth =1


numbers = {
#     '0x0': framebuf.FrameBuffer(num0x0, 128, 1, framebuf.MONO_HLSB, sWidth),
#     '0x1': framebuf.FrameBuffer(num0x0, 15, 1, framebuf.MONO_HLSB, sWidth),
#     '0x1': framebuf.FrameBuffer(num0x0, bitLength , 1, framebuf.MONO_HLSB, sWidth),
    '0x1': framebuf.FrameBuffer(num0x0, 8, 6, framebuf.MONO_HLSB, sWidth),
    }

# Clear the oled display in case it has junk on it.
for x in range(11):
    oled.fill(0)
    oled.blit(numbers['0x1'], 0, x)
    # Finally update the oled display so the image & text is displayed
    sleep(1)
    print(x)
    oled.show()

print(patternX)
print(bitLength)
print(num0x0Base)
print("RUN COMPLETE")        
