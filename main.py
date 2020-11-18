from machine import UART

import utime

uart = UART(1, 115200)
uart.write('at+usbkeyboard=https://micropython.org\\n\r')

while True:
    print('move')
    uart.write('at+usbhidmousemove=-100,100\r')
    uart.write('at+usbhidmousebutton=\r')
    uart.write('AT+USBKEYBOARDCODE=00-00-04\r')
    utime.sleep(1)
