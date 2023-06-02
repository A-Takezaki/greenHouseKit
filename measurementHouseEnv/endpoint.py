from typing import List
from fastapi import FastAPI
import sqlite3
from pydantic import BaseModel

class SensorData(BaseModel):
    id: int
    timestamp: str
    temperature: float
    humidity: float

DB_NAME = "sensorData.db"
TABLE_NAME = "TemperatureHumidityData"

app = FastAPI()

def get_db_data():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(f"SELECT * FROM {TABLE_NAME}")
    result = c.fetchall()
    conn.close()
    return result

@app.get("/data", response_model=List[SensorData])
def read_data():
    rows = get_db_data()
    return [{"id": row[0], "timestamp": row[1], "temperature": row[2], "humidity": row[3]} for row in rows]