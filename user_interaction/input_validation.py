from os import path
from influxdb_client import InfluxDBClient
import user_interaction.welcome_and_end
from config import config as cfg


class InputValidator:

    def __init__(self):
        self.option = 0
        self.csv_path = ""
        self.bucket = ""
        self.pr = user_interaction.welcome_and_end.Printer()

    def validate_unit_option(self, option):
        self.option = option
        if self.option == "Y" or self.option == "N" \
                or self.option == "YES" or self.option == "NO" \
                or self.option == "y" or self.option == "n" \
                or self.option == "yes" or self.option == "no":
            return True
        else:
            self.pr.print_invalid_answer()
            return False

    def validate_input_csv_path(self, csv_path):
        self.csv_path = csv_path
        if not path.exists(self.csv_path):
            print("Path not found")
            valid = False
        elif not self.csv_path.endswith('.csv'):
            print("Not a csv file")
            valid = False
        else:
            valid = True
        return valid

    def validate_bucket_input(self, bucket):
        self.bucket = bucket
        client = InfluxDBClient(url=cfg.influxdb["url"],
                                token=cfg.influxdb["token"],
                                org=cfg.influxdb["org"])

        query = 'buckets() |> filter(fn: (r) => r.name !~ /^_/)' \
                '|> map(fn: (r) => ({_value: r.name}))'
        result = client.query_api().query(query)
        buckets = [bk['_value'] for bk in result[0].records]

        if self.bucket in buckets:
            return True
        else:
            print("Bucket not found: " + str(self.bucket))
            return False

    def validate_option(self, option):
        self.option = option
        if self.option == "1" or self.option == "2":
            return True
        else:
            return False


