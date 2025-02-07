from gpiozero import LED
from time import sleep
class TrafficLights:
    def __init__(self, red_pin, yellow_pin, green_pin):
        self.red_led = LED(red_pin)
        self.yellow_led = LED(yellow_pin)
        self.green_led = LED(green_pin)

    def red(self):
        self.red_led.on()
        self.yellow_led.off()
        self.green_led.off()

    def yellow(self):
        self.red_led.off()
        self.yellow_led.on()
        self.green_led.off()

    def green(self):
        self.red_led.off()
        self.yellow_led.off()
        self.green_led.on()
if __name__=="__main__":
    traffic=TrafficLights(17,27,22)
    while True:
        traffic.red()
        sleep(3)
        traffic.yellow()
        sleep(3)
        traffic.green()
        sleep(3)