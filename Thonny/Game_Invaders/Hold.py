from machine import Pin, Signal
from time import sleep_ms 
clk = 21
dt = 19

count = 0


hold = []
pin_clock = Pin(clk, Pin.IN)
pin_dt = Pin(dt, Pin.IN)

# pin_clock = Signal(clk, Pin.IN, invert=True)
# pin_dt = Signal(Pin(dt, Pin.IN), invert=True)

ccw1 = ''.join(['01', '00', '10', '11'])
# holdBin = int('0b0000_0000').to_bytes(2,'big')
# holdBin = ''


def invertX(dataX):
        # return ~(dataX & 0xff)
        return dataX

def pin_clock_triggerHandler(pinX):
    global hold
    print("pin_clock: ", pinX)
    hold.append(str(pin_clock.value()) + str(pin_dt.value()))
    print('pin_clock', hold);


def pin_dt_triggerHandler(pinX):
    global hold
    print("pin_dt: ", pinX)
    hold.append(str(pin_clock.value()) + str(pin_dt.value()))
    print('pin_dt', hold);


pin_clock.irq(handler=pin_clock_triggerHandler, trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING)
pin_dt.irq(handler=pin_dt_triggerHandler, trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING)

while True :
    if len(hold) < 1:
        print('pin_clock: {}'.format(bin(invertX(pin_clock.value()))))
        print('pin_dt: {}'.format(bin(invertX(pin_dt.value()))))
    # if len(hold) >= 3: 
    #     currentState = "".join(hold)
    #     if currentState == ccw1 :
    #         print("**** START FRAME: {} = {}: {}".format(currentState, ccw1, currentState == ccw1))
    #         count += 1

    #     hold.clear()
    # print('count: ', count)
    sleep_ms(16)
 




# The MIT License (MIT)
# Copyright (c) 2021 Mike Teachman
# https://opensource.org/licenses/MIT

# example for MicroPython rotary encoder

# import sys
# if sys.platform == 'esp8266' or sys.platform == 'esp32':
#     from rotary_irq_esp import RotaryIRQ
# elif sys.platform == 'pyboard':
#     from rotary_irq_pyb import RotaryIRQ
# elif sys.platform == 'rp2':
#     from rotary_irq_rp2 import RotaryIRQ
# else:
#     print('Warning:  The Rotary module has not been tested on this platform')

# import time


# r = RotaryIRQ(pin_num_clk=21,
#               pin_num_dt=19,
#               min_val=0,
#               max_val=10,
#               reverse=False,
#               range_mode=RotaryIRQ.RANGE_WRAP)

# val_old = r.value()
# while True:
#     val_new = r.value()

#     if val_old != val_new:
#         val_old = val_new
#         print('result =', val_new)

#     time.sleep_ms(16)
