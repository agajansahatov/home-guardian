import time,sys
from pymata4EX import pymata4EX
board=pymata4EX.Pymata4EX()
trigger_pin=12
echo_pin=13
def the_callback(data):
    print(f'Distance in cm: {data[2]}')
board.set_pin_mode_sonar(trigger_pin,echo_pin,callback=the_callback)

while True:
    try:
        time.sleep(0.1)
        distance = board.sonar_read(trigger_pin)
        print('distance= ', distance)
    except KeyboardInterrupt:
        board.shutdown()
        sys.exit(0)

