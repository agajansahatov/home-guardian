import sys
import time
from pymata4EX import pymata4EX

# 这是超声波传感器的参数
DISTANCE_CM = 2
TRIGGER_PIN = 7
ECHO_PIN = 9

# 这是三色灯的参数
DIGITAL_PIN = 10  # arduino pin number

# 这是超声波传感器
# 这是回调函数，如果距离发生变化，则会输出一个回调数值。
def the_callback(data):
    """
    The callback function to display the change in distance
    :param data: [pin_type=12, trigger pin number, distance, timestamp]
    """
    # 加f后可以在字符串里面使用用花括号括起来的变量和表达式
    print(data[DISTANCE_CM])

# 这是自定义函数和自定义参数
def sonar(my_board, trigger_pin, echo_pin, callback):
    """
    Set the pin mode for a sonar device. Results will appear via the
    callback.

    :param my_board: an pymata express instance
    :param trigger_pin: Arduino pin number
    :param echo_pin: Arduino pin number
    :param callback: The callback function
    """

    # set the pin mode for the trigger and echo pins 这是规定参数
    my_board.set_pin_mode_sonar(trigger_pin, echo_pin, callback)
    # wait forever
    while True:
        try:
            # 设置读取距离的时间，相当于是读取频率
            time.sleep(.01)
            print(f'data read: {my_board.sonar_read(TRIGGER_PIN)}')
        except KeyboardInterrupt:
            my_board.shutdown()
            sys.exit(0)

def blink(my_board, pin):
    """
    This function will to toggle a digital pin.

    :param my_board: an PymataExpress instance
    :param pin: pin to be controlled
    """

    # set the pin mode
    my_board.set_pin_mode_digital_output(pin)
    # 如果距离小于50，亮灯
    if my_board.sonar_read(TRIGGER_PIN[0]) < 50:
        # while True:
            my_board.digital_write(pin, 1)
            time.sleep(10)
            my_board.digital_write(pin, 0)

# 这是实例化参数
board = pymata4EX.Pymata4EX()
try:
    # 这里都是实参
    sonar(board, TRIGGER_PIN, ECHO_PIN, the_callback)
    blink(board, DIGITAL_PIN)
    board.shutdown()
except (KeyboardInterrupt, RuntimeError):
    board.shutdown()
    sys.exit(0)