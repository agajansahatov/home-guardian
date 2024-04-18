import time
from modules.display import Display
from modules.fan import Fan
from modules.fire_alarm import FireAlarm
from modules.lightbulb import LightBulb
from modules.slide_potentiometer import SlidePotentiometer


class HomeGuardian:

    def __init__(self, board):
        self.board = board
        self.display = Display(board)
        self.fan = Fan(board)
        self.fire_alarm = FireAlarm(board)
        self.light_bulb = LightBulb(board)

    # We need to pass this the object which it will use to get the stable_temperature value.
    def initialize(self, obj: object, method_name: str) -> None:
        get_input = getattr(obj, method_name)

        try:
            if not isinstance(get_input(), int):
                raise ValueError("The method did not return an integer.")
        except Exception as e:
            raise ValueError(f"Error occurred while calling method '{method_name}': {e}")

        self.display.show('Activating', 'sensors...')
        stable_temperature = -100
        variable_temperature = -100
        while True:
            # Read input and display it
            variable_temperature = get_input()
            if variable_temperature != stable_temperature:
                stable_temperature = variable_temperature
                print(stable_temperature)
                self.display.show(f'Temperature:{str(stable_temperature)}C')

            # Check input and control components accordingly
            if stable_temperature < 10:
                self.fan.turn_off()
                self.light_bulb.set_color("blue")
                self.fire_alarm.stop()
            elif 15 <= stable_temperature <= 35:
                self.fan.turn_off()
                self.light_bulb.set_color("green")
                self.fire_alarm.stop()
            elif 35 < stable_temperature <= 60:
                self.fan.turn_on()
                self.light_bulb.set_color("red")
                self.fire_alarm.stop()
            else:
                self.light_bulb.blink("red", "yellow")
                self.fan.turn_on()
                self.fire_alarm.start()
            time.sleep(.1)
