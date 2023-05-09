import csv
import locale


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