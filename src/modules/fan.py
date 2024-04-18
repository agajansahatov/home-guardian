import time


class Fan:
    def __init__(self, board):
        self.board = board
        self.fan_pin = 3
        self.board.set_pin_mode_digital_output(self.fan_pin)
        self.is_on = False

    def turn_on(self):
        if(not self.is_on):
            self.board.digital_write(self.fan_pin, 1)
            self.is_on = True
            time.sleep(1)

    def turn_off(self):
        if(self.is_on):
            self.board.digital_write(self.fan_pin, 0)
            self.is_on = False
            time.sleep(1)
