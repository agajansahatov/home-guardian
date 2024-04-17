"""
 Copyright (c) 2020 Alan Yorinks All rights reserved.

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 Version 3 as published by the Free Software Foundation; either
 or (at your option) any later version.
 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

 You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
 along with this library; if not, write to the Free Software
 Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

import sys
import time
from pymata4EX import pymata4EX

"""
This is a demonstration of the tone methods
"""
# 定义低中高频率
CL = [0, 131, 147, 165, 175, 196, 211, 248]  # Frequency of Low C notes

CM = [0, 262, 294, 330, 350, 393, 441, 495]  # Frequency of Middle C notes

CH = [0, 525, 589, 661, 700, 786, 882, 990]  # Frequency of High C notes

# 第一首歌谱子频率
song_1 = [CM[3], CM[5], CM[6], CM[3], CM[2], CM[3], CM[5], CM[6],  # Notes of song1
          CH[1], CM[6], CM[5], CM[1], CM[3], CM[2], CM[2], CM[3],
          CM[5], CM[2], CM[3], CM[3], CL[6], CL[6], CL[6], CM[1],
          CM[2], CM[3], CM[2], CL[7], CL[6], CM[1], CL[5]]
# 节奏
beat_1 = [1, 1, 3, 1, 1, 3, 1, 1,  # Beats of song 1, 1 means 1/8 beats
          1, 1, 1, 1, 1, 1, 3, 1,
          1, 3, 1, 1, 1, 1, 1, 1,
          1, 2, 1, 1, 1, 1, 1, 1,
          1, 1, 3]
# instantiate pymata4EX
board = pymata4EX.Pymata4EX()
TONE_PIN=4
# set a pin's mode for tone operations
board.set_pin_mode_tone(TONE_PIN)
for i in range(1, len(song_1)):  # Play song 1
    # board.play_tone(TONE_PIN, song_1[i], beat_1[i] * 0.5)
    # Buzz.ChangeFrequency()  # Change the frequency along the song note
    # time.sleep(beat_1[i] * 500)  # delay a note for beat * 0.5s
# specify pin, frequency and duration and play tone
#
# time.sleep(2)
#
# # specify pin and frequency and play continuously
    board.play_tone_continuously(TONE_PIN, song_1[i])
    time.sleep(beat_1[i] * 0.5)

# specify pin to turn pin off
board.play_tone_off(TONE_PIN)

# clean up
board.shutdown()
# except KeyboardInterrupt:
#     board.shutdown()
#     sys.exit(0)
