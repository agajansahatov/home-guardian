import time
import threading

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
        self.blink_thread = None
        self.blinking = False

    def get_color(self):
        return self.color

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
        if self.blinking:
            self._stop_blink()

    def set_color(self, color):
        if self.blinking:
            self._stop_blink()

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
        elif color == "black":
            self.board.pwm_write(self.red_pin, 0)
            self.board.pwm_write(self.green_pin, 0)
            self.board.pwm_write(self.blue_pin, 0)
            self.color = "black"
        else:
            self.turn_off()
            self.color = "white"

    def _blink_thread(self, color1, color2):
        while self.blinking:
            if self.color == color1:
                self.set_color(color2)
            else:
                self.set_color(color1)
            time.sleep(.1)

    def blink(self, color1, color2):
        if not self.blinking:
            self.blinking = True
            self.blink_thread = threading.Thread(target=self._blink_thread, args=(color1, color2))
            self.blink_thread.start()

    def _stop_blink(self):
        if self.blinking:
            self.blinking = False
            if not self.blink_thread:
                self.blink_thread.join()
            self.blink_thread = None

