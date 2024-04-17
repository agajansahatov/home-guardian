import time
from pymata4EX import pymata4EX

# Initialize pymata4EX instance
board = pymata4EX.Pymata4EX()

# Set up digital pins for dot matrix
DOT_MATRIX_DATA_PIN = 8
DOT_MATRIX_CLOCK_PIN = 11
DOT_MATRIX_LOAD_PIN = 13

board.set_pin_mode_digital_output(DOT_MATRIX_DATA_PIN)
board.set_pin_mode_digital_output(DOT_MATRIX_CLOCK_PIN)
board.set_pin_mode_digital_output(DOT_MATRIX_LOAD_PIN)


# Function to light up individual LEDs on the dot matrix
def test_dot_matrix():
    # Define patterns to light up individual LEDs
    patterns = [
        [1, 0, 0, 0, 0, 0, 0, 0],  # Row 1
        [0, 1, 0, 0, 0, 0, 0, 0],  # Row 2
        [0, 0, 1, 0, 0, 0, 0, 0],  # Row 3
        [0, 0, 0, 1, 0, 0, 0, 0],  # Row 4
        [0, 0, 0, 0, 1, 0, 0, 0],  # Row 5
        [0, 0, 0, 0, 0, 1, 0, 0],  # Row 6
        [0, 0, 0, 0, 0, 0, 1, 0],  # Row 7
        [0, 0, 0, 0, 0, 0, 0, 1]  # Row 8
    ]

    # Loop through each pattern and display it on the dot matrix
    for pattern in patterns:
        # Set the LOAD_PIN low
        board.digital_write(DOT_MATRIX_LOAD_PIN, 0)
        for i in range(8):
            # Set the DATA_PIN to the corresponding value in the pattern
            board.digital_write(DOT_MATRIX_DATA_PIN, pattern[i])
            # Pulse the CLOCK_PIN to shift the data
            board.digital_write(DOT_MATRIX_CLOCK_PIN, 1)
            board.digital_write(DOT_MATRIX_CLOCK_PIN, 0)
        # Pulse the LOAD_PIN to latch the data
        board.digital_write(DOT_MATRIX_LOAD_PIN, 1)
        board.digital_write(DOT_MATRIX_LOAD_PIN, 0)

        # Wait for a short duration to observe the LED pattern
        time.sleep(1)


# Test the dot matrix
test_dot_matrix()

# Clean up before exiting
board.shutdown()
