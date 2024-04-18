import time
from pymata4EX import pymata4EX
from modules.i2c_liquidcrystaldisplay import LiquidCrystal_I2C

class Display:
    def __init__(self, board):
        self.lcd = LiquidCrystal_I2C(0x27, 0, 1, board)
        self.lcd.enable_backlight()

    def show(self, line1, line2=""):
        self.lcd.clear()

        # Truncate line1 if it exceeds 16 characters
        if len(line1) > 16:
            if len(line2) == 0:
                line2 = line1[16:]
            line1 = line1[:16]

        # Truncate line2 if it exceeds 16 characters
        if len(line2) > 16:
            line2 = line2[:16]

        # Print line1
        if len(line1) > 0:
            self.lcd.set_cursor(0, 0)
            self.lcd.print(line1)

        # Print line2
        if len(line2) > 0:
            self.lcd.set_cursor(0, 1)
            self.lcd.print(line2)

        # Need to give some time to execute printing both lines, otherwise it doesn't work
        time.sleep(1)
