import csv
from csv_conversion import time_reformatting


def write_data_to_outfile(row_list, outfile):
    with open(outfile, 'a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(row_list)


def get_first_and_last_datetime(filename):
    with open(filename, newline='') as csv_file:
        next(csv_file)
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_list = list(csv_reader)
        return time_reformatting.reformat_time(csv_list[0][0]), \
            time_reformatting.reformat_time(csv_list[-1][0])


def get_measurement_name(infile):
    with open(infile, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            first_line = row
            break

    measurement_name = first_line[1] # später i anstelle von 1

    return measurement_name


def convert_row(index, row, start_end_array, infile):
    time = time_reformatting.reformat_time(row[0])
    value = row[1] # später i anstelle von 1
    # comments == requirements
    start_time = start_end_array[0]  # read first timestamp
    stop_time = start_end_array[1]  # read last timestamp

    # read measurement information from the first line:
    field = "EUR/kWh" # später hier input parameter einfügen
    measurement = get_measurement_name(infile)

    row_list = [['','', index, start_time, stop_time,
                       time, value, field, measurement]]

    return row_list


def convert_csv(infile, outfile):
    start_end_array = get_first_and_last_datetime(infile)
    # read and write lines one by one (no saving in memory)
    with open(infile, newline='') as csv_file:
        # skip first line with next
        next(csv_file)
        csv_reader = csv.reader(csv_file, delimiter=',')
        for index, row in enumerate(csv_reader):
            row_list = convert_row(index, row, start_end_array, infile)
            # row_list = add_startdate_and_enddate(row_list, startdate, enddate)
            write_data_to_outfile(row_list, outfile)
