import time
import threading

class FireAlarm:
    def __init__(self, board, tone_pin=4):
        self.board = board
        self.tone_pin = tone_pin

        # Define low, medium, and high frequencies
        self.CL = [0, 131, 147, 165, 175, 196, 211, 248]  # Frequency of Low C notes
        self.CM = [0, 262, 294, 330, 350, 393, 441, 495]  # Frequency of Middle C notes
        self.CH = [0, 525, 589, 661, 700, 786, 882, 990]  # Frequency of High C notes

        # Fire alarm song notes and beats
        self.song_fire_alarm = [
            self.CM[1], self.CM[2], self.CM[3], self.CM[4], self.CM[5], self.CM[6], self.CM[7], self.CM[1],
            self.CM[2], self.CM[3], self.CM[4], self.CM[5], self.CM[6], self.CM[7], self.CM[1], self.CM[2],
            self.CM[3], self.CM[4], self.CM[5], self.CM[6], self.CM[7], self.CM[1], self.CM[2], self.CM[3],
            self.CM[4], self.CM[5], self.CM[6], self.CM[7], self.CM[1], self.CM[2], self.CM[3], self.CM[4]
        ]

        self.beat_fire_alarm = [1, 1, 1, 1, 1, 1, 1, 1,  # Beats of the fire alarm song (each note is 1/8 beat)
                                1, 1, 1, 1, 1, 1, 1, 1,
                                1, 1, 1, 1, 1, 1, 1, 1,
                                1, 1, 1, 1, 1, 1, 1, 1]
        self.playing_alarm = False

    def _play(self):
        self.playing_alarm = True
        self.board.set_pin_mode_tone(self.tone_pin)
        for i in range(len(self.song_fire_alarm)):
            if not self.playing_alarm:
                break
            self.board.play_tone_continuously(self.tone_pin, self.song_fire_alarm[i])
            time.sleep(self.beat_fire_alarm[i] * 0.5)
        self.board.play_tone_off(self.tone_pin)
        time.sleep(1)

    def _finish(self):
        self.playing_alarm = False

    def start(self):
        self.alarm_thread = threading.Thread(target=self._play)
        self.alarm_thread.start()

    def stop(self):
        stop_thread = threading.Thread(target=self._finish)
        stop_thread.start()
        self.alarm_thread.join()
