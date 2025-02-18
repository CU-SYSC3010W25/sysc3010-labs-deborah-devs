from sense_hat import SenseHat
import time

sense = SenseHat()

while True:
    temperature = sense.get_temperature()
    pressure = sense.get_pressure()
    humidity = sense.get_humidity()

    sense.show_message(f"Temp: {temperature:.1f}C", scroll_speed=0.1)
    sense.show_message(f"Pressure: {pressure:.1f}hPa", scroll_speed=0.1)
    sense.show_message(f"Humidity: {humidity:.1f}%", scroll_speed=0.1)

    time.sleep(5)
