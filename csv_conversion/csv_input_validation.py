import csv
import re


class CsvInputValidator:

    def __init__(self, infile):
        self.infile = infile

    def check_delimiter(self):
        with open(self.infile, newline='') as csv_file:
            contents = csv_file.read()
            dialect = csv.Sniffer().sniff(contents)
            delimiter = dialect.delimiter
            if delimiter == ',':
                return True
            else:
                print("Delimiter of csv file has to be ','.")
                return False

    def check_input_timeformat(self):
        pattern = r'^\d{2}.\d{2}.\d{4} \d{2}:\d{2}:\d{2}$'
        time_pattern = '%d.%m.%Y %H:%M:%S'

        with open(self.infile, 'r') as csv_file:
            dialect = csv.Sniffer().sniff(csv_file.read(1024))
            csv_file.seek(0)
            reader = csv.reader(csv_file, delimiter=dialect.delimiter)
            next(reader)

            for row in reader:
                if not re.match(pattern, row[0]):
                    print(f"The value '{row[0]}' does not match the timestamp pattern"
                          f" '{time_pattern}'")
                    return False
            return True

    def check_valid_values(self):
        with open(self.infile, 'r') as csv_file:
            dialect = csv.Sniffer().sniff(csv_file.read(1024))
            csv_file.seek(0)
            reader = csv.reader(csv_file, delimiter=dialect.delimiter)
            next(reader)

            for row in reader:
                for value in row[1:]:

                    try:
                        float(value)

                    except ValueError:
                        print(f"The value '{value}' is not a float.")
                        return False
            return True



