import sys
import time
from pymata4EX import pymata4EX

# Initialize the pymata4EX board
board = pymata4EX.Pymata4EX()

# Set pin 3 as a digital output
board.set_pin_mode_digital_output(3)

try:
    # Turn on the fan
    board.digital_write(3, 1)
    print("Fan is on")

    # Wait for 5 seconds
    time.sleep(5)

    # Turn off the fan
    board.digital_write(3, 0)
    print("Fan is off")

except KeyboardInterrupt:
    # Shutdown the board if the script is interrupted
    board.shutdown()
    sys.exit(0)
