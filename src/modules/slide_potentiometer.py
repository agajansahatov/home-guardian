class SlidePotentiometer:
    def __init__(self, board):
        self.board = board
        self.pin = 2
        self.board.set_pin_mode_analog_input(self.pin)

    def read_value(self) -> int:
        """
        Read the analog value from the slide potentiometer.
        Returns:
            int: The percentage value based on the analog reading.
        """
        # Get the analog reading as a tuple and extract the first element
        analog_value = self.board.analog_read(self.pin)[0]

        # Convert the analog value to a percentage
        percentage = int(analog_value / 1023 * 100)

        return percentage
