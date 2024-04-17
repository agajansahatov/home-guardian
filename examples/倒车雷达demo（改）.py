import sys
import cv2
import time
from pymata4EX import pymata4EX

# 这是超声波传感器的参数
DISTANCE_CM = 2
TRIGGER_PIN = 7
ECHO_PIN = 9
TONE_PIN=4
# 这是三色灯的参数
DIGITAL_PIN = 6  # arduino pin number
board = pymata4EX.Pymata4EX()

def the_callback(data):
    pass
    """
    The callback function to display the change in distance
    :param data: [pin_type=12, trigger pin number, distance, timestamp]
    """
    # 加f后可以在字符串里面使用用花括号括起来的变量和表达式
    # print(data[DISTANCE_CM])
board.set_pin_mode_sonar(TRIGGER_PIN, ECHO_PIN, callback=the_callback)
board.set_pin_mode_digital_output(DIGITAL_PIN)
board.set_pin_mode_tone(TONE_PIN)
# 如果距离小于50，亮灯
while True:
    # try:
    kk=cv2.waitKey(10)
    print(kk)
    distance=board.sonar_read(TRIGGER_PIN)[0]
    print(distance)
    if distance<50:
        print('on')
        board.digital_write(DIGITAL_PIN,1)
        time.sleep(1)
        board.play_tone_continuously(TONE_PIN, 1000)
        time.sleep(1)
        # board.play_tone_off(TONE_PIN)
    else:
        print('off')
        board.digital_write(DIGITAL_PIN, 0)
        time.sleep(0.5)
        board.play_tone_off(TONE_PIN)
        time.sleep(0.5)
# except KeyboardInterrupt:
    if kk==27:
        board.digital_write(DIGITAL_PIN, 0)
        time.sleep(0.1)
        board.play_tone_off(TONE_PIN)
        time.sleep(0.1)
        # board.shutdown()
        # sys.exit(0)
        break
board.shutdown()
sys.exit(0)
# if board.sonar_read(TRIGGER_PIN[0]) < 50:
#     # while True:
#     board.digital_write(DIGITAL_PIN, 1)
#     time.sleep(10)
#     board.digital_write(DIGITAL_PIN, 0)


# 这是超声波传感器
# 这是回调函数，如果距离发生变化，则会输出一个回调数值。
# def the_callback(data):
#     """
#     The callback function to display the change in distance
#     :param data: [pin_type=12, trigger pin number, distance, timestamp]
#     """
#     # 加f后可以在字符串里面使用用花括号括起来的变量和表达式
#     print(data[DISTANCE_CM])
# 
# # 这是自定义函数和自定义参数
# def sonar(my_board, trigger_pin, echo_pin, callback):
#     """
#     Set the pin mode for a sonar device. Results will appear via the
#     callback.
# 
#     :param my_board: an pymata express instance
#     :param trigger_pin: Arduino pin number
#     :param echo_pin: Arduino pin number
#     :param callback: The callback function
#     """
# 
#     # set the pin mode for the trigger and echo pins 这是规定参数
#     board.set_pin_mode_sonar(trigger_pin, echo_pin, callback)
#     # wait forever
#     while True:
#         try:
#             # 设置读取距离的时间，相当于是读取频率
#             time.sleep(1)
#             print(f'data read: {board.sonar_read(TRIGGER_PIN)}')
#         except KeyboardInterrupt:
#             board.shutdown()
#             sys.exit(0)
# 
# def blink(my_board, pin):
#     """
#     This function will to toggle a digital pin.
# 
#     :param my_board: an PymataExpress instance
#     :param pin: pin to be controlled
#     """
#     board.set_pin_mode_sonar(7, 9)
#     # set the pin mode
#     board.set_pin_mode_digital_output(pin)
#     # 如果距离小于50，亮灯
#     board.digital_write(pin, 1)
#     time.sleep(0.5)
#     board.digital_write(pin, 0)
#     time.sleep(0.5)
#     print(board.sonar_read(TRIGGER_PIN[0]))
#     if board.sonar_read(TRIGGER_PIN[0]) < 50:
#         # while True:
#             board.digital_write(pin, 1)
#             time.sleep(10)
#             board.digital_write(pin, 0)
# 
# # 这是实例化参数
# board = pymata4EX.Pymata4EX()
# try:
#     # 这里都是实参
#     # sonar(board, TRIGGER_PIN, ECHO_PIN, the_callback)
#     blink(board, DIGITAL_PIN)
#     board.shutdown()
# except (KeyboardInterrupt, RuntimeError):
#     board.shutdown()
#     sys.exit(0)