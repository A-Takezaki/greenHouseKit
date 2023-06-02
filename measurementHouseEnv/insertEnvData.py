import sqlite3
import time
from random import uniform

# SQLite DB Name
DB_NAME = "sensorData.db"

# SQLite DB Table Schema
TABLE_NAME = "TemperatureHumidityData"
TABLE_FIELDS = "id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp DATETIME, temperature NUMERIC, humidity NUMERIC"

def simulate_temperature_and_humidity():
    temperature = uniform(20.0, 30.0) # A simulated temperature value in the range 20.0 - 30.0
    humidity = uniform(30.0, 50.0) # A simulated humidity value in the range 30.0 - 50.0
    return temperature, humidity

def log_temperature_and_humidity(temperature, humidity):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} ({TABLE_FIELDS})")
    c.execute(f"INSERT INTO {TABLE_NAME} (timestamp, temperature, humidity) VALUES (datetime('now'), ?, ?)", (temperature, humidity))
    conn.commit()
    conn.close()


def measurementTempAndHum():
    
    return temperature,humidity


temperature, humidity = simulate_temperature_and_humidity()
log_temperature_and_humidity(temperature, humidity)
print('hello')



# https://qiita.com/STDNUL/items/f76a65f7eb4e27d44b5f