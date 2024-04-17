import sys
import time
from pymata4EX import pymata4EX

board = pymata4EX.Pymata4EX()

# Set pin 3 as PWM output for fan control
board.set_pin_mode_pwm_output(3)

try:
    # Start the fan and set initial fan speed (80% duty cycle)
    board.pwm_write(3, 205)
    print("Fan is on")
    print("Fan speed set to 80%")

    # Wait for 6 seconds
    time.sleep(6)

    # Decrease fan speed (60% duty cycle)
    board.pwm_write(3, 153)
    print("Fan speed decreased to 60%")

    # Turn off the fan after 3 seconds
    time.sleep(3)
    board.pwm_write(3, 0)
    print("Fan is off")

except KeyboardInterrupt:
    # Shutdown the board if the script is interrupted
    board.shutdown()
    sys.exit(0)
