class SlidePotentiometer:
    def __init__(self, board):
        self.board = board
        self.pin = 2
        self.board.set_pin_mode_analog_input(self.pin)

    def read_value(self):
        """
        Read the analog value from the slide potentiometer.
        Returns:
            int: The analog value read from the potentiometer.
        """
        return self.board.analog_read(self.pin)
