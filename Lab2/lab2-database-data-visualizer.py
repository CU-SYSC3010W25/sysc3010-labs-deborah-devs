import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

dbconnect = sqlite3.connect("sensorDB.db")
df = pd.read_sql_query("SELECT * FROM sensordata", dbconnect)

dbconnect.close()

df['datetime'] = pd.to_datetime(df['datetime'])
df.set_index('datetime', inplace=True)

plt.figure(figsize=(12, 6))

plt.plot(df.index, df['temperature'], label='Temperature (°C)', color='red')
plt.plot(df.index, df['humidity'], label='Humidity (%)', color='blue')
plt.plot(df.index, df['pressure'], label='Pressure (hPa)', color='green')

plt.xlabel('Time')
plt.ylabel('Values')
plt.title('Sensor Data Over Time')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
