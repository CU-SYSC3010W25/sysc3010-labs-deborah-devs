import time
import sqlite3
from sense_hat import SenseHat

# Initialize the SenseHAT instance
sense = SenseHat()

# Connect to the SQLite database
dbconnect = sqlite3.connect("sensorDB.db")
dbconnect.row_factory = sqlite3.Row
cursor = dbconnect.cursor()

# Create the sensordata table if it does not exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS sensordata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datetime DATETIME DEFAULT CURRENT_TIMESTAMP,
    temperature REAL NOT NULL,
    humidity REAL NOT NULL,
    pressure REAL NOT NULL
);
''')
dbconnect.commit()

try:
    while True:
        # Read data from SenseHAT sensors
        temperature = round(sense.get_temperature(), 2)
        humidity = round(sense.get_humidity(), 2)
        pressure = round(sense.get_pressure(), 2)

        # Insert data into the sensordata table
        cursor.execute('''
        INSERT INTO sensordata (temperature, humidity, pressure)
        VALUES (?, ?, ?);
        ''', (temperature, humidity, pressure))
        dbconnect.commit()

        # Print logged data for confirmation
        print(f"Logged: Temperature={temperature:.2f}C, Humidity={humidity:.2f}%, Pressure={pressure:.2f}hPa")

        # Wait for 1 second
        time.sleep(1)
except KeyboardInterrupt:
    print("\nData logging stopped.")
finally:
    # Close the database connection
    dbconnect.close()

