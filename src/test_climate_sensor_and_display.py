import time

from pymata4EX import pymata4EX
from modules.display import Display
from modules.climate_sensor import ClimateSensor

if __name__ == "__main__":
    # Create an instance of the board
    board = pymata4EX.Pymata4EX()

    # Create an instance of the Display class
    display = Display(board)  # Assuming pin 2 is used for the LCD
    display.show('Activating', 'sensors...')

    # Create an instance of the ClimateSensor class
    climate = ClimateSensor(board)
    while True:
        data = climate.get_data()
        if len(data) > 0:
            temperature, humidity = data
            if (-100 < temperature < 100) and (-100 < humidity < 100):
                print(temperature, humidity)
                display.show('Temperature: ' + str(temperature) + 'C', 'Humidity: ' + str(humidity) + '%')
        time.sleep(1)

# After 20 seconds got the error => I2C: Too few bytes received
