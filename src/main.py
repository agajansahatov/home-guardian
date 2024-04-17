import time

from pymata4EX import pymata4EX
from modules.lightbulb import LightBulb
from modules.slide_potentiometer import SlidePotentiometer

if __name__ == "__main__":
    board = pymata4EX.Pymata4EX()
    potentiometer = SlidePotentiometer(board, 2)
    lightbulb = LightBulb(board)

    try:
        while True:
            pot_value = potentiometer.read_value()

            # Print the value read from the potentiometer
            print("Potentiometer value:", pot_value)

            # Optionally, you can use this value to adjust the light bulb color
            # For example:
            # if pot_value < 512:
            #     lightbulb.set_color("red")
            # else:
            #     lightbulb.set_color("green")

            # Add your logic here to control the light bulb based on the potentiometer value

    except KeyboardInterrupt:
        board.shutdown()
