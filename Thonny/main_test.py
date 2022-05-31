# Test file
# https://github.com/AnthonyKNorman/MicroPython_SSD1306/blob/master/main.py
# "address": "/dev/ttyUSB0",
# MicroPython_SSD1306-master
   
# Complete project details at https://RandomNerdTutorials.com
# https://randomnerdtutorials.com/micropython-oled-display-esp32-esp8266/

from machine import Pin, SoftI2C
from SSD1306 import SSD1306_I2C
# from SSD1306 import SSD1306
from time import sleep

# HelTec Automation(TM) ESP32 Series Dev boards Pin assignment 
i2c = SoftI2C(scl=Pin(15), sda=Pin(4))

oled_width = 128
oled_height = 64

rst = Pin(16, Pin.OUT)
rst.value(1)
oled = SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Hello Hyacinth', 0, 0)
oled.text('Hello, World 2!', 0, 10)
oled.text('Hello, World 3!', 0, 20)
oled.text('Hello Roman :)', 0, 30)
        
oled.show()
