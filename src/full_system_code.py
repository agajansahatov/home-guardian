import time
from pymata4EX import pymata4EX

# Constants for temperature thresholds
TEMP_LOW = 15
TEMP_HIGH = 30
TEMP_CRITICAL = 50

# Pin configurations
TEMP_SENSOR_PIN = 2
FAN_PIN = 3
RGB_RED_PIN = 5
RGB_GREEN_PIN = 6
RGB_BLUE_PIN = 10
ALARM_PIN = 4  # Example pin for alarm sound

# Initialize pymata4EX instance
board = pymata4EX.Pymata4EX()

# Set pin modes
board.set_pin_mode_dht(TEMP_SENSOR_PIN, sensor_type=11)
board.set_pin_mode_digital_output(FAN_PIN)
board.set_pin_mode_pwm_output(RGB_RED_PIN)
board.set_pin_mode_pwm_output(RGB_GREEN_PIN)
board.set_pin_mode_pwm_output(RGB_BLUE_PIN)
board.set_pin_mode_tone(ALARM_PIN)

# Function to set RGB LED colors
def set_rgb_color(red, green, blue):
    board.pwm_write(RGB_RED_PIN, red)
    board.pwm_write(RGB_GREEN_PIN, green)
    board.pwm_write(RGB_BLUE_PIN, blue)

# Main loop to continuously read and monitor temperature
while True:
    # Read temperature from DHT sensor
    temperature = board.dht_read(TEMP_SENSOR_PIN)[1]

    # Control actions based on temperature
    if temperature < TEMP_LOW:
        set_rgb_color(0, 0, 255)  # Blue color
        board.digital_write(FAN_PIN, 0)  # Turn off fan
    elif TEMP_LOW <= temperature < TEMP_HIGH:
        set_rgb_color(0, 255, 0)  # Green color
        board.digital_write(FAN_PIN, 0)  # Turn off fan
    elif TEMP_HIGH <= temperature < TEMP_CRITICAL:
        set_rgb_color(255, 0, 0)  # Red color
        board.digital_write(FAN_PIN, 1)  # Turn on fan
    else:
        # Implement alarm functionality here (play tones, change LED colors, etc.)
        pass

    # Wait for a short duration before reading temperature again
    time.sleep(2)
