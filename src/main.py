import time
from pymata4EX import pymata4EX
from modules.climate_sensor import ClimateSensor
from modules.slide_potentiometer import SlidePotentiometer
from home_guardian import HomeGuardian

if __name__ == "__main__":
    board = pymata4EX.Pymata4EX()
    # climate_sensor = ClimateSensor(board)
    slide_potentiometer = SlidePotentiometer(board)
    home_guardian = HomeGuardian(board)

    try:
        # If you want to test the real-time climate_sensor, then pass climate_sensor object to this method.
        # The climate_sensor object should have a method which returns an integer value
        # For example, if we want the system work based on the temperature,
        # we use get_temperature() method of climate_sensor object
        # home_guardian.initialize(climate_sensor, "get_temperature")

        # If we want to use slider to check the system works or not,
        # we pass slide_potentiometer object and its read_value method to the home_guardian system.
        # the read_value() method of the slide_potentiometer returns int value.
        home_guardian.initialize(slide_potentiometer, "read_value")
    except KeyboardInterrupt:
        board.shutdown()
