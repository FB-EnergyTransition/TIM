import csv
import locale
import re
from datetime import datetime


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


def check_decimal_sign(infile):
    with open(infile, 'r') as csv_file:
        contents = csv_file.read()
        dialect = csv.Sniffer().sniff(contents)
        decimal_separator = dialect.lineterminator
        if decimal_separator == '\n':
            locale.setlocale(locale.LC_ALL, '')
            decimal_separator = locale.localeconv()['decimal_point']
        if dialect.lineterminator == '.':
            return True
        else:
            print("Decimal sign in csv file has to be '.'.") # returns False also when correct and delimiter is ,
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

            if re.match(pattern, row[0]):
                return True
            else:
                print(f"The value '{row[0]}' does not match the timestamp pattern '{time_pattern}'")
                return False


def check_valid_values(infile):
    pass # überprüfen ob float werte enthalten ab zweiter spalte
# überprüfen ob decimal punkt


