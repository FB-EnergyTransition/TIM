from os import path
from influxdb_client import InfluxDBClient
from user_interaction import get_user_input_params

from config import config as cfg


def validate_unit_option(option):
    if option == "Y" or option == "N" \
            or option == "YES" or option == "NO" \
            or option == "y" or option == "n" \
            or option == "yes" or option == "no":
        return True
    else:
        get_user_input_params.print_invalid_answer()
        return False


def validate_input_csv_path(csv_path):
    if not path.exists(csv_path):
        print("Path not found")
        valid = False
    elif not csv_path.endswith('.csv'):
        print("Not a csv file")
        valid = False
    else:
        valid = True
    return valid


def validate_bucket_input(bucket):
    client = InfluxDBClient(url=cfg.influxdb["url"],
                            token=cfg.influxdb["token"],
                            org=cfg.influxdb["org"])

    query = 'buckets() |> filter(fn: (r) => r.name !~ /^_/)' \
            '|> map(fn: (r) => ({_value: r.name}))'
    result = client.query_api().query(query)
    buckets = [bk['_value'] for bk in result[0].records]

    if bucket in buckets:
        return True
    else:
        print("Bucket not found: " + str(bucket))
        return False


def validate_option(option):
    if option == "1" or option == "2":
        return True
    else:
        return False


