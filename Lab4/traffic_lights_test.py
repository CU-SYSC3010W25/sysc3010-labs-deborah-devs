from traffic_lights import TrafficLights
from time import sleep
def test_traffic_lights():
    # Mock GPIO pins
    red_pin, yellow_pin, green_pin = 17, 27, 22

    lights = TrafficLights(red_pin, yellow_pin, green_pin)

    # Test red light
    lights.red()
    assert lights.red_led.value == 1, "Red LED should be ON"
    assert lights.yellow_led.value == 0, "Yellow LED should be OFF"
    assert lights.green_led.value == 0, "Green LED should be OFF"
    sleep(3)
    print("red passed")

    # Test yellow light
    sleep(3)
    lights.yellow()
    assert lights.red_led.value == 0, "Red LED should be OFF"
    assert lights.yellow_led.value == 1, "Yellow LED should be ON"
    assert lights.green_led.value == 0, "Green LED should be OFF"
    print("yellow passed")
    sleep(3)

    # Test green light
    sleep(3)
    lights.green()
    assert lights.red_led.value == 0, "Red LED should be OFF"
    assert lights.yellow_led.value == 0, "Yellow LED should be OFF"
    assert lights.green_led.value == 1, "Green LED should be ON"
    print("green passed")
    sleep(3)
if __name__ == "__main__":
    test_traffic_lights()
    print("All tests passed!")