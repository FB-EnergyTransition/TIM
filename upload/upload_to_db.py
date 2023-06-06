import csv

from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
import os

from config import config as cfg


class Uploader:

    def __init__(self, infile, csv_file, bucket, measurement):
        self.infile = infile
        self.csv_file = csv_file
        self.bucket = bucket
        self.measurement = measurement

    def upload_data(self):
        client = InfluxDBClient(url=cfg.influxdb["url"],
                                token=cfg.influxdb["token"],
                                org=cfg.influxdb["org"])

        write_api = client.write_api(write_options=SYNCHRONOUS)

        with open("{}\\{}".format(os.path.dirname(self.infile), self.csv_file)) as file:
            reader = csv.DictReader(file)

            points = []
            for row in reader:
                point = {
                    "measurement": self.measurement,
                    "tags": {
                        "units": str(row["_field"])
                    },
                    "time": row["_time"],
                    "fields": {
                        row["_measurement"]: float(row["_value"])
                    }
                }

                points.append(point)

            write_api.write(bucket=self.bucket, record=points)
