# open cmd and 'sudo apt-get install python-smbus'
# Reboot raspy
# type 'i2cdetect -y 1' to find the I2C address, mine was 27

import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Hello World!", 2, 3)
