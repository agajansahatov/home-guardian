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
        self.color = "white"

    def turn_on(self):
        self.board.pwm_write(self.red_pin, 255)
        self.board.pwm_write(self.green_pin, 255)
        self.board.pwm_write(self.blue_pin, 255)
        self.color = "black"
        self.is_on = True

    def turn_off(self):
        self.board.pwm_write(self.red_pin, 0)
        self.board.pwm_write(self.green_pin, 0)
        self.board.pwm_write(self.blue_pin, 0)
        self.color = "white"
        self.is_on = False

    def set_color(self, color):
        if color == "red":
            self.board.pwm_write(self.red_pin, 255)
            self.board.pwm_write(self.green_pin, 0)
            self.board.pwm_write(self.blue_pin, 0)
            self.color = "red"
        elif color == "green":
            self.board.pwm_write(self.red_pin, 0)
            self.board.pwm_write(self.green_pin, 255)
            self.board.pwm_write(self.blue_pin, 0)
            self.color = "green"
        elif color == "blue":
            self.board.pwm_write(self.red_pin, 0)
            self.board.pwm_write(self.green_pin, 0)
            self.board.pwm_write(self.blue_pin, 255)
            self.color = "blue"
        elif color == "yellow":
            self.board.pwm_write(self.red_pin, 255)
            self.board.pwm_write(self.green_pin, 255)
            self.board.pwm_write(self.blue_pin, 0)
            self.color = "yellow"
        else:
            self.turn_off()
            self.color = "white"

    def get_color(self):
        return self.color
