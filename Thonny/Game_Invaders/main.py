from ClassPlay import Machine
from machine import Pin
from time import sleep_ms 
import BitWisePlay
import binascii

invertBytes = BitWisePlay.invertBytes
bitwise_and_bytes = BitWisePlay.bitwise_and_bytes

count = 0

clk = 37
dt = 36



pin_clock = Pin(clk, Pin.IN)
pin_dt = Pin(dt, Pin.IN)
hold = [[],[]]


def invertX(dataX):
        # return ~(dataX & 0xff)
        return dataX

def pin_clock_triggerHandler(pinX):
    # print("pin_clock: ", pinX)
    x = bitwise_and_bytes(invertBytes(pin_clock.value()))
    y = bitwise_and_bytes(invertBytes(pin_dt.value()))
    hold[0] = (x,y)
    # print(x,y)


def pin_dt_triggerHandler(pinX):
    # print("pin_dt: ", pinX)
    y = bitwise_and_bytes(invertBytes(pin_dt.value()))
    x = bitwise_and_bytes(invertBytes(pin_clock.value()))

    hold[1] = (x,y)
    # hold[1]([x,y])
    # print(x,y)


pin_clock.irq(handler=pin_clock_triggerHandler, trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING)
pin_dt.irq(handler=pin_dt_triggerHandler, trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING)

while True :
    sleep_ms(16)
    print(hold)
    # hold.clear()