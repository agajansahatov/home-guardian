import sys
import time
from pymata4EX import pymata4EX
board=pymata4EX.Pymata4EX()
board.set_pin_mode_digital_output(13)
for i in range(5):
    board.digital_write(13,1)
    time.sleep(1)
    board.digital_write(13,0)
    time.sleep(1)
board.shutdown()
sys.exit(0)