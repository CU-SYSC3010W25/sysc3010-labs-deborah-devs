import pyrebase
import time
from datetime import datetime
from sense_hat import SenseHat

# Firebase configuration (replace with your actual config)
config = {
    "apiKey": "AIzaSyDE944JQ5l2yq2YpxTSguWdthSHmR7Y-ng",
    "authDomain": "lab3-591ea.firebaseapp.com",
    "databaseURL": "https://lab3-591ea-default-rtdb.firebaseio.com",
    "storageBucket": "lab3-591ea.appspot.com"
}

# Initialize Firebase and SenseHAT
firebase = pyrebase.initialize_app(config)
db = firebase.database()
sense = SenseHat()

# Prompt user for their username
username = input("Enter your username: ")

# Function to write SenseHAT sensor data to the database
def write_data():
    while True:
        # Get SenseHAT sensor data
        temp = round(sense.get_temperature(), 2)
        humidity = round(sense.get_humidity(), 2)
        pressure = round(sense.get_pressure(), 2)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Structure data to include all three sensors
        sensor_data = {
            "temperature": temp,
            "humidity": humidity,
            "pressure": pressure
        }

        # Write data with timestamp as the key
        db.child(username).child("sensor_data").child(timestamp).set(sensor_data)
        print(f"Data written at {timestamp}: {sensor_data}")

        # Alarm if temperature drops below 20°C
        if temp < 20:
            print("Alert! Temperature below 20°C!")
       
        time.sleep(10)  # Write every 10 seconds

# Function to read the three most recent sensor values
def read_data():
    sensor_data = db.child(username).child("sensor_data").get()
    if sensor_data.each() is None:
        print("No data available in the database.")
        return

    # Convert to list and get the last three entries
    sensor_data_list = sensor_data.each()[-3:]
    for entry in sensor_data_list:
        timestamp = entry.key()
        values = entry.val()
        print(f"Timestamp: {timestamp}, Data: {values}")

# Main program loop
def main():
    print("Writing data to Firebase...")
    try:
        write_data()
    except KeyboardInterrupt:
        print("\nReading the three most recent entries...")
        read_data()
        print("Exiting program.")

if __name__ == "__main__":
    main()
