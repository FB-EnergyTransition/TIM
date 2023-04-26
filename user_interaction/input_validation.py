from os import path
from influxdb_client import InfluxDBClient

from user_interaction import get_user_input_params


def validate_unit_input(option):
    if option == "Y" or option == "N" \
            or option == "YES" or option == "NO" \
            or option == "y" or option == "n" \
            or option == "yes" or option == "no":
        pass
    else:
        get_user_input_params.print_invalid_answer()
        validate_unit_input(get_user_input_params.ask_for_units())


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
    client = InfluxDBClient(url='http://172.22.108.135:8086',
                            token='FyHQmuauHLl07gGqwxR_sToKNmCRJSSvXK2ETDSimF'
                                  'FjfwY0zbLFYEFyT7aC-g9gsy1j2_tpOMDC50JSq804WQ==',
                            org='TIM', debug=True)
    query = 'buckets() |> filter(fn: (r) => r.name !~ /^_/)' \
            '|> map(fn: (r) => ({_value: r.name}))'
    result = client.query_api().query(query)
    buckets = [bk['_value'] for bk in result[0].records]

    if bucket in buckets:
        return True
    else:
        return False
