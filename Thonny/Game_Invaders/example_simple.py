from machine import Pin
from time import sleep_ms 
clk = 36
dt = 37

count = 0


hold = []
pin_clock = Pin(clk, Pin.IN)
pin_dt = Pin(dt, Pin.IN)
ccw1 = ''.join(['01', '00', '10', '11'])
# holdBin = int('0b0000_0000').to_bytes(2,'big')
# holdBin = ''



def pin_clock_triggerHandler(pinX):
#     global hold
    hold.append([pin_clock.value(), pin_dt.value()])
#     print("pin_clock: ", pin_clock.value(), pin_dt.value())
#     hold.append(str(pin_clock.value()) + str(pin_dt.value()))


def pin_dt_triggerHandler(pinX):
#     global hold
    hold.append([pin_clock.value(), pin_dt.value()])
#     print("pin_dt: ", pin_clock.value(), pin_dt.value())
#     print("pin_dt: ", pinX)
#     hold.append(str(pin_clock.value()) + str(pin_dt.value()))


pin_clock.irq(handler=pin_clock_triggerHandler, trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING)
pin_dt.irq(handler=pin_dt_triggerHandler, trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING)

while True :
    if len(hold) >= 3:
        print(hold)
#         currentState = "".join(hold)
#         print("**** START FRAME: {} = {}: {}".format(currentState, ccw1, currentState == ccw1))
#         if currentState == ccw1 :
#             print("**** START FRAME: {} = {}: {}".format(currentState, ccw1, currentState == ccw1))
#             count += 1

        hold.clear()
#     print('count: ', count)g
    sleep_ms(16)
 
