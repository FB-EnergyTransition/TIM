import csv

import csv_conversion.time_reformatting


def write_data_to_outfile(row_list, outfile):
    with open(outfile, 'a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(row_list)


def get_first_and_last_datetime(infile):
    with open(infile, newline='') as csv_file:
        next(csv_file)
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_list = list(csv_reader)
        first_last_list = []
        tf1 = csv_conversion.time_reformatting.TimeFormatter(csv_list[0][0])
        first = tf1.reformat_time()
        first_last_list.append(first)
        tf2 = csv_conversion.time_reformatting.TimeFormatter(csv_list[-1][0])
        last = tf2.reformat_time()
        first_last_list.append(last)
        return first, last


def get_measurement_name(infile, item):
    with open(infile, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            first_line = row
            break

    measurement_name = first_line[item]

    return measurement_name



