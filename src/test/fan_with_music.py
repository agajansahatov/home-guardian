import sys
import time
from pymata4EX import pymata4EX

# Initialize the pymata4EX board
board = pymata4EX.Pymata4EX()

# Set pin 3 as a digital output for controlling the fan
board.set_pin_mode_digital_output(3)

# Set pin 4 for music output
board.set_pin_mode_tone(4)

try:
    # Turn on the fan
    board.digital_write(3, 1)
    print("Fan is on")

    # Start playing music
    board.play_tone_continuously(4, 440)  # A4 note (440 Hz)
    print("Music is played")

    # Wait for 5 seconds
    time.sleep(5)

    # Turn off the fan
    board.digital_write(3, 0)
    print("Fan is off")

    # Stop playing music
    board.play_tone_off(4)
    print("Music stopped")

except KeyboardInterrupt:
    # Shutdown the board if the script is interrupted
    board.shutdown()
    sys.exit(0)
