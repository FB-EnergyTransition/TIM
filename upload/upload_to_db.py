import csv

from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS


def upload_data(csv_file, bucket, measurement):
    client = InfluxDBClient(url='http://172.22.108.135:8086',
                                token='FyHQmuauHLl07gGqwxR_sToKNmCRJSSvXK2ETDSimF'
                                      'FjfwY0zbLFYEFyT7aC-g9gsy1j2_tpOMDC50JSq804WQ==',
                                org='TIM')

    write_api = client.write_api(write_options=SYNCHRONOUS)

    with open('./resources/' + csv_file) as file:
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
