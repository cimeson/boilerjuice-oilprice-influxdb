from dotenv import load_dotenv
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime
import os
import requests

# Load configuration from .env file
load_dotenv()

INFLUXDB_URL = os.getenv('INFLUXDB_URL')
INFLUXDB_TOKEN = os.getenv('INFLUXDB_TOKEN')
INFLUXDB_ORG = os.getenv('INFLUXDB_ORG')
INFLUXDB_BUCKET = os.getenv('INFLUXDB_BUCKET')
API_URL = os.getenv('API_URL')

def query_api(url):
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    labels = [col['label'] for col in data['cols']]

    records = []
    for row in data['rows']:
        record = {}
        for idx, cell in enumerate(row['c']):
            record[labels[idx]] = cell['v']
        records.append(record)
    return records

def write_to_influxdb(data):
    client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)
    print(data)

    points = []
    for record in data:
        timestamp = datetime.strptime(record['Date'], '%b %d %Y')
        value = float(record['Price']) / 100.0
        point = Point("oil") \
                .field("price", value) \
                .time(timestamp, WritePrecision.S)
        points.append(point)

    write_api = client.write_api(write_options=SYNCHRONOUS)
    write_api.write(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG, record=points)
    client.close()

def main():
    data = query_api(API_URL)
    write_to_influxdb(data)

if __name__ == "__main__":
    main()
