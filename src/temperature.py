import time
from pymata4EX import pymata4EX
from modules.i2c_liquidcrystaldisplay import \
    LiquidCrystal_I2C  # Assuming the i2c_liquidcrystaldisplay.py module is in the 'modules' directory

# Initialize pymata4EX instance
myboard = pymata4EX.Pymata4EX()

# Set up DHT sensor on pin 2
myboard.set_pin_mode_dht(2, sensor_type=11)

# Initialize LCD display
LCD = LiquidCrystal_I2C(0x27, 0, 1, myboard)
LCD.enable_backlight()

# Main loop to continuously read and display temperature
while True:
    # Read temperature from DHT sensor
    dht_data = myboard.dht_read(2)

    # Check if the DHT sensor reading is valid
    if dht_data is not None:
        temperature = dht_data[1]  # Extract temperature from the returned data
        humidity = dht_data[0]  # Extract humidity from the returned data

        # Clear LCD screen
        LCD.clear()

        # Display temperature and humidity on LCD
        LCD.set_cursor(0, 0)
        LCD.print(f'Temperature: {temperature}C')

        LCD.set_cursor(0, 1)
        LCD.print(f'Humidity: {humidity}%')

    # Wait for a short duration before reading again
    time.sleep(2)
