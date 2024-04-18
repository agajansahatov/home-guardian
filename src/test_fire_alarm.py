import time

from pymata4EX import pymata4EX
from modules.fire_alarm_old import FireAlarm

if __name__ == "__main__":
    board = pymata4EX.Pymata4EX()

    fire_alarm = FireAlarm(board)

    fire_alarm.start()

    time.sleep(2)

    fire_alarm.stop()
