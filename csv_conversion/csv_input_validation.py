import csv
import re


def check_delimiter(infile):
    with open(infile, newline='') as csv_file:
        contents = csv_file.read()
        dialect = csv.Sniffer().sniff(contents)
        delimiter = dialect.delimiter
        if delimiter == ',':
            return True
        else:
            print("Delimiter of csv file has to be ','.")
            return False


def check_input_timeformat(infile):
    pattern = r'^\d{2}.\d{2}.\d{4} \d{2}:\d{2}:\d{2}$'
    time_pattern = '%d.%m.%Y %H:%M:%S'

    with open(infile, 'r') as csv_file:
        dialect = csv.Sniffer().sniff(csv_file.read(1024))
        csv_file.seek(0)
        reader = csv.reader(csv_file, delimiter=dialect.delimiter)
        next(reader)

        for row in reader:
            if not re.match(pattern, row[0]):
                print(f"The value '{row[0]}' does not match the timestamp pattern '{time_pattern}'")
                return False
        return True


def check_valid_values(infile):
    with open(infile, 'r') as csv_file:
        dialect = csv.Sniffer().sniff(csv_file.read(1024))
        csv_file.seek(0)
        reader = csv.reader(csv_file, delimiter=dialect.delimiter)
        next(reader)

        for row in reader:
            for value in row[1:]:

                try:
                    float_value = float(value)
                    print(float_value)

                except ValueError:
                    print(f"The value '{value}' is not a float.")
                    return False
        return True



