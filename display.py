from config import *
from machine import Pin, SoftI2C
import ssd1306
from time import sleep_ms

# Pin Assignment
i2c = SoftI2C(scl=Pin(oled_config['scl']), sda=Pin(oled_config['sda']),freq=400000)

# Reset display
d_rst = Pin(oled_config['reset'], Pin.OUT)
d_rst.value(0)
sleep_ms(20)
d_rst.value(1)

oled = ssd1306.SSD1306_I2C(oled_config['width'], oled_config['height'], i2c, addr=oled_config['addr'])
oled.fill(0)
oled.text('Welcome to ESP32', 5, 25)
oled.show()

def print(text, w, h):
    oled.fill(0)
    oled.text(text, w, h)
    oled.show()

def clear():
    oled.fill(0)
    oled.show()

def display(line1, line2, snr=None, rssi=None):
    oled.fill(0)  # Clear Screen
    oled.text(line1, 0, 0)
    oled.text(line2, 0, 10)
    if snr != None and rssi != None:
        oled.text('SNR: %i' % snr, 0, 20)
        oled.text('RSSI: %i' % rssi, 0, 30)
    oled.show()
  
