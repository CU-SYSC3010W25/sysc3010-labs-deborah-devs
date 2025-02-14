from sense_hat import SenseHat
import time

# This function returns a SenseHat instance
def get_sensehat():
    sense = SenseHat()
    return sense

# This function takes in a SenseHat instance and the flash_time
# The display on the SenseHat flashes red (1 second on, 1 second off) for the duration of flash_time.
# At the end of the flash_time the SenseHat display should be off.
def alarm(sense, flash_time):
    for _ in range(flash_time):
        sense.clear(255, 0, 0)  # Red color
        time.sleep(1)
        sense.clear()  # Turn off display
        time.sleep(1)
    sense.clear()  # Make sure the display is off at the end
