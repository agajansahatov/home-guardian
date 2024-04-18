import time
from pymata4EX import pymata4EX
from modules.climate_sensor import ClimateSensor
from modules.display import Display
from modules.fan import Fan
from modules.fire_alarm import FireAlarm
from modules.light_bulb import LightBulb
from modules.slide_potentiometer import SlidePotentiometer

if __name__ == "__main__":
    # Initialize board and components
    board = pymata4EX.Pymata4EX()
    climate_sensor = ClimateSensor(board)
    display = Display(board)
    fan = Fan(board)
    fire_alarm = FireAlarm(board)
    light_bulb = LightBulb(board)
    slide_potentiometer = SlidePotentiometer(board)

    display.show('Activating', 'sensors...')

    try:
        while True:
            # Read temperature from climate sensor
            temperature = climate_sensor.read_temperature()

            # Update display with temperature
            display.show(str(temperature))

            # Check temperature and control components accordingly
            if temperature < 15:
                fan.turn_off()
                light_bulb.set_color("blue")
            elif 15 <= temperature <= 30:
                fan.turn_off()
                light_bulb.set_color("green")
            elif 30 < temperature <= 50:
                fan.turn_on()
                light_bulb.set_color("red")
            else:
                while true:
                    light_bulb.set_color
                    time.sleep(1)
                fire_alarm.start()

            # Check slide potentiometer for user input

            # Add a delay to avoid excessive polling
            time.sleep(1)

    except KeyboardInterrupt:
        # Clean up GPIO pins on keyboard interrupt
        board.shutdown()
