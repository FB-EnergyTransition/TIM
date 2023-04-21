import argparse
from os import path


def process_input_params():
    parser = argparse.ArgumentParser()
    parser.add_argument('-input_file', type=str, default="input.csv",
                        help="name of the csv file that shall be uploaded to InfluxDB")
    parser.add_argument('-bucket', type=str,
                        help="InfluxDB bucket the data shall be uploaded into")
    args = parser.parse_args()
    return args


def validate_csv_path(csv_path):
    if not path.exists(csv_path):
        print("Path not found")
        valid = False
    elif not csv_path.endswith('.csv'):
        print("Not a csv file")
        valid = False
    else:
        valid = True
    return valid
