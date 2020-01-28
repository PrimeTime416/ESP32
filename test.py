import machine
import time
led_blue = machine.Pin(2, machine.Pin.OUT)
led_blue.value(1)
led_blue.value(0)
print("hello world")
for i in range(1,12):
    print(i)
    
# for i in range(0, 10):
while True:
    led_blue.value(1)
    time.sleep(0.5)
    led_blue.value(0)
    time.sleep(0.5)
    
print("hello again :)")
    