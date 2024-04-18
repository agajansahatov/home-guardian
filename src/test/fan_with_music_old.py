import time
from pymata4EX import pymata4EX

def control_fan_and_play_music():
    # Initialize the board
    board = pymata4EX.Pymata4EX()

    try:
        # Set fan control pin as PWM output
        fan_pin = 3
        board.set_pin_mode_pwm_output(fan_pin)

        # Set fan speed to start running
        fan_speed = 255
        board.pwm_write(fan_pin, fan_speed)

        # Set buzzer pin for playing music
        buzzer_pin = 4
        board.set_pin_mode_tone(buzzer_pin)

        # Play music
        song_notes = [262, 294, 330, 349, 392, 440, 494, 523]  # Frequencies for C major scale
        song_beats = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]    # Beats for each note (in seconds)

        for note, beat in zip(song_notes, song_beats):
            # Play tone
            board.play_tone_continuously(buzzer_pin, note)
            time.sleep(beat)  # Play note for specified duration

    except KeyboardInterrupt:
        pass  # Catch KeyboardInterrupt to gracefully exit the loop

    finally:
        # Cleanup
        board.play_tone_off(buzzer_pin)  # Turn off tone
        board.pwm_write(fan_pin, 0)      # Turn off fan
        time.sleep(1)                     # Wait for the fan to stop before shutting down
        board.shutdown()

if __name__ == "__main__":
    control_fan_and_play_music()
