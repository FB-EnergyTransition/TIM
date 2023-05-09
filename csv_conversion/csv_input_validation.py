import csv


def check_delimiter(infile):
    with open(infile, newline='') as csv_file:
        contents = csv_file.read()
        dialect = csv.Sniffer().sniff(contents)
        delimiter = dialect.delimiter
        print(delimiter)
        if delimiter == ',':
            return True
        else:
            print("Delimiter of csv file has to be ','.")
            return False