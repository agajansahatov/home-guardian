import time


class Fan:
    def __init__(self, board):
        self.board = board
        self.fan_pin = 3
        self.board.set_pin_mode_digital_output(self.fan_pin)

    def turn_on(self):
        self.board.digital_write(self.fan_pin, 1)
        time.sleep(1)

    def turn_off(self):
        self.board.digital_write(self.fan_pin, 0)
        time.sleep(1)
