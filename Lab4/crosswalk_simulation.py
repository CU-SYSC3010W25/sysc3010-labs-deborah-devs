from gpiozero import Button
from time import sleep
from traffic_lights import TrafficLights

# GPIO Pins
red_pin, yellow_pin, green_pin = 17, 27, 22
button_pin = 4

# Initialize components
lights = TrafficLights(red_pin, yellow_pin, green_pin)
button = Button(button_pin)

def crosswalk_simulation():
    print("Starting crosswalk simulation...")

    while True:
        lights.red()
        print("Red Light - Stop")
        sleep(5)

        lights.green()
        print("Green Light - Go")
        # Handle button press during the green phase
        if button.wait_for_press(timeout=5):
            print("Button pressed, transitioning to yellow...")
            sleep(1)
            lights.yellow()
        else:
            lights.yellow()
        print("Yellow Light - Caution")
        sleep(2)

if __name__ == "__main__":
    crosswalk_simulation()