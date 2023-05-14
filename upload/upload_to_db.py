import csv

from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

from config import config as cfg


def upload_data(csv_file, bucket, measurement):
    client = InfluxDBClient(url=cfg.influxdb["url"],
                            token=cfg.influxdb["token"],
                            org=cfg.influxdb["org"])

    write_api = client.write_api(write_options=SYNCHRONOUS)

    with open('./resources/test_resources/' + csv_file) as file:
        reader = csv.DictReader(file)

        points = []
        for row in reader:
            point = {
                "measurement": measurement,
                "tags": {
                    "units": str(row["_field"])
                },
                "time": row["_time"],
                "fields": {
                    row["_measurement"]: float(row["_value"])
                }
            }
            print(point)
            points.append(point)

        write_api.write(bucket=bucket, record=points)
