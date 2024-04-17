import sys
import time
from pymata4EX import pymata4EX

board=pymata4EX.Pymata4EX()

board.set_pin_mode_tone(3)
board.play_tone(3,1000,500)
time.sleep(2)
board.play_tone_continuously(3,1500)
time.sleep(2)
board.play_tone_off(3)
board.shutdown()
sys.exit(0)