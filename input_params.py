from os import path


def validate_csv_path(csv_path):
    valid = False
    if not path.exists(csv_path):
        print("Path not found")
        valid = False
    elif not csv_path.endswith('.csv'):
        print("Not a csv file")
        valid = False
    else:
        valid = True
    return valid
