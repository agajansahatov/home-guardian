class LightBulb:
    def __init__(self, board, red_pin=5, green_pin=6, blue_pin=10):
        self.board = board
        self.red_pin = red_pin
        self.green_pin = green_pin
        self.blue_pin = blue_pin
        self.board.set_pin_mode_pwm_output(self.red_pin)
        self.board.set_pin_mode_pwm_output(self.green_pin)
        self.board.set_pin_mode_pwm_output(self.blue_pin)
        self.is_on = False

    def turn_on(self):
        self.board.pwm_write(self.red_pin, 255)
        self.board.pwm_write(self.green_pin, 255)
        self.board.pwm_write(self.blue_pin, 255)
        self.is_on = True

    def turn_off(self):
        self.board.pwm_write(self.red_pin, 0)
        self.board.pwm_write(self.green_pin, 0)
        self.board.pwm_write(self.blue_pin, 0)
        self.is_on = False

    def set_color(self, color):
        if color == "red":
            self.board.pwm_write(self.red_pin, 255)
            self.board.pwm_write(self.green_pin, 0)
            self.board.pwm_write(self.blue_pin, 0)
        elif color == "green":
            self.board.pwm_write(self.red_pin, 0)
            self.board.pwm_write(self.green_pin, 255)
            self.board.pwm_write(self.blue_pin, 0)
        elif color == "blue":
            self.board.pwm_write(self.red_pin, 0)
            self.board.pwm_write(self.green_pin, 0)
            self.board.pwm_write(self.blue_pin, 255)
        elif color == "yellow":
            self.board.pwm_write(self.red_pin, 255)
            self.board.pwm_write(self.green_pin, 255)
            self.board.pwm_write(self.blue_pin, 0)
        else:
            self.turn_off()
