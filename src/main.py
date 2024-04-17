import time

from pymata4EX import pymata4EX
from modules.fan import Fan

if __name__ == "__main__":
    # Create an instance of the board
    board = pymata4EX.Pymata4EX()

    fan = Fan(board)
    fan.turn_on()
    time.sleep(5)
    fan.turn_off()
