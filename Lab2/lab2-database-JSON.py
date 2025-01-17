'''
Script to access weather data from openweathermap.org using a REST API
Data are returned as a JSON string
The JSON string is then deserialized/parsed into a Python dictionary
Sample data fields are printed.

See http://openweathermap.org/current#current for the API

Originally written by Cheryl Schramm ~2015
Updated by James Green Jan-2023
'''

from urllib.request import urlopen 
from urllib.parse import urlencode
import json
import sqlite3

dbconnect = sqlite3.connect("sensorDB.db")
dbconnect.row_factory = sqlite3.Row
cursor = dbconnect.cursor()

for i in range(1, 10):
	# The URL that is formatted: http://api.openweathermap.org/data/2.5/weather?APPID=a808bbf30202728efca23e099a4eecc7&units=imperial&q=ottawa
	# As of October 2015, you need an API key.
	# Prof Schramm created this API key several years ago. If it doesn’t work, get your own.
	apiKey = "a808bbf30202728efca23e099a4eecc7"   
	# Query the user for a city
	city = input("Enter the name of a city whose weather you want: ")

	# Build the URL parameters
	params = {"q":city, "units":"metric", "APPID":apiKey }
	arguments = urlencode(params)

	# Get the weather information
	address = "http://api.openweathermap.org/data/2.5/weather"
	url = address + "?" + arguments

	print(f"Requesting data from URL: {url}")
	webData = urlopen(url)
	results = webData.read().decode('utf-8')  # results is a JSON string
	webData.close()

	print("The raw JSON string returned by the query is")
	print(results)

	# Deserialize/parse the JSON string into a Python Dictionary data structure
	# See https://www.geeksforgeeks.org/json-loads-in-python/ for loads details
	data = json.loads(results)  

	# Use the Dictionary to print specific fields from the data
	print ("Temperature: %d%sC" % (data["main"]["temp"], chr(176) ))
	print ("Humidity: %d%%" % data["main"]["humidity"])
	print ("Pressure: %d" % data["main"]["pressure"] )
	print ("Wind : %d" % data["wind"]["speed"])
	
	windSpeed = data["wind"]["speed"]
	cursor.execute('''
        INSERT INTO Winds (City, WindSpeed)
        VALUES (?, ?);
        ''', (city, windSpeed))
	dbconnect.commit()
	
	# Check the most recent wind speed for this city before this entry
	cursor.execute('''
		SELECT WindSpeed FROM Winds
        WHERE City = ?
        ORDER BY Date DESC
        LIMIT 2;
    ''', (city,))
	rows = cursor.fetchall()

	if len(rows) > 1:
		previousSpeed = float(rows[1]["WindSpeed"])
		if windSpeed > previousSpeed:
			print(f"Wind speed in {city} increased to {windSpeed} m/s.")
		elif windSpeed < previousSpeed:
			print(f"Wind speed in {city} decreased {windSpeed} m/s.")
		else:
			print(f"Wind speed in {city} stays the same at {windSpeed} m/s.")
	else:
		print(f"Wind speed in {city} is: {windSpeed} m/s.")
		
dbconnect.close()
