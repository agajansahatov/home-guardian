import sys
import time
from time import sleep
from pymata4EX import pymata4EX
board=pymata4EX.Pymata4EX()
# print(board)
def the_callback(data):
    print('data',data)
board.set_pin_mode_dht(2, sensor_type=11,callback=None)
value=board.dht_read(2)
tlist=time.localtime()
ftime=f'{tlist.tm_year}-{tlist.tm_mon:2}-{tlist.tm_mday:2}'\
    f'    {tlist.tm_hour:2}-{tlist.tm_min:2}-{tlist.tm_sec:2}'
print(f'poll pin 2: humidity={value[0]} temp={value[1]} '\
      f'time of last report:{ftime}')