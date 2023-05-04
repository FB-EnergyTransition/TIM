import csv

from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS


def upload_data(csv_file, bucket):
    client = InfluxDBClient(url='http://172.22.108.135:8086',
                                token='FyHQmuauHLl07gGqwxR_sToKNmCRJSSvXK2ETDSimF'
                                      'FjfwY0zbLFYEFyT7aC-g9gsy1j2_tpOMDC50JSq804WQ==',
                                org='TIM')

    write_api = client.write_api(write_options=SYNCHRONOUS)

    with open(csv_file) as file:
        reader = csv.DictReader(file)

        points = []
        for row in reader:
            point = {
                "measurement": "Strompreis", # user input: please input type of measurement in file
                "tags": {
                    "units": str(row["units"])
                },
                "time": row["_time"],
                "fields": {
                    row["field_name"]: float(row["field_value"])
                }
            }
            print(point)
            points.append(point)

        write_api.write(bucket=bucket, record=points)
