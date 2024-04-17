import time
from pymata4EX import pymata4EX
from modules.i2c_liquidcrystaldisplay import LiquidCrystal_I2C


class ClimateSensor:
    def __init__(self, board):
        self.board = board
        self.pin = 2
        self.board.set_pin_mode_dht(self.pin, sensor_type=11)

    def get_temperature(self):
        data = self.board.dht_read(self.pin)
        if data is not None and not (int(data[1] == 0) and int(data[0] == 0)):
            temperature = int(data[1])
            return temperature
        else:
            # assuming a temperature cannot be -1000
            return -1000

    def get_humidity(self):
        data = self.board.dht_read(self.pin)

        if data is not None and not (int(data[1] == 0) and int(data[0] == 0)):
            return int(data[0])
        else:
            # assuming a humidity cannot be -1000
            return -1000

    def get_data(self):
        data = self.board.dht_read(self.pin)
        if data is not None and not (int(data[1] == 0) and int(data[0] == 0)):
            return int(data[1]), int(data[0])
        else:
            return []
