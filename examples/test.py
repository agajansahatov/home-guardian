import sys,time
from pymata4EX import pymata4EX
from i2c_liquidcrystaldisplay import LiquidCrystal_I2C
# board = pymata4EX.Pymata4EX()
myboard=pymata4EX.Pymata4EX()
myboard.set_pin_mode_dht(2, sensor_type=11)
# myboard.set_pin_mode_dht(2,sensor_type=11,callback=0)
LCD=LiquidCrystal_I2C(0x27,0,1,myboard)
LCD.enable_backlight()
while True:
    value=myboard.dht_read(2)
    # print(value)
    LCD.set_cursor(0,0)
    LCD.print('Humidity:'+str(value[0]))
    LCD.set_cursor(0,1)
    LCD.print('Temperature:'+str(value[1]))
    # LCD.clear()
