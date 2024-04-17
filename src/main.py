import time

from pymata4EX import pymata4EX
from modules.lightbulb import LightBulb

if __name__ == "__main__":
    board = pymata4EX.Pymata4EX()
    lightbulb = LightBulb(board)

    lightbulb.turn_on()

    lightbulb.set_color("red")
    time.sleep(2)

    lightbulb.set_color("green")
    time.sleep(2)

    lightbulb.set_color("blue")
    time.sleep(2)

    lightbulb.set_color("yellow")
    time.sleep(2)

    lightbulb.turn_off()
