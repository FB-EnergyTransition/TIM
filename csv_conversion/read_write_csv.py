import csv
import os

from csv_conversion import time_reformatting, header_handling,\
    check_amount_of_measurements, outfile_validation


def write_data_to_outfile(row_list, outfile):
    with open(outfile, 'a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(row_list)
        print(outfile)


def get_first_and_last_datetime(filename):
    with open(filename, newline='') as csv_file:
        next(csv_file)
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_list = list(csv_reader)
        return time_reformatting.reformat_time(csv_list[0][0]), \
            time_reformatting.reformat_time(csv_list[-1][0])


def get_measurement_name(infile, i):
    with open(infile, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            first_line = row
            break

    measurement_name = first_line[i] # später i anstelle von 1

    return measurement_name


def convert_row(index, row, start_end_array, infile, item):
    time = time_reformatting.reformat_time(row[0])
    value = row[item] # später i anstelle von 1
    # comments == requirements
    start_time = start_end_array[0]  # read first timestamp
    stop_time = start_end_array[1]  # read last timestamp

    # read measurement information from the first line:
    field = "EUR/kWh" # später hier input parameter einfügen
    measurement = get_measurement_name(infile, item)

    row_list = [['','', index, start_time, stop_time,
                       time, value, field, measurement]]

    return row_list





def convert_csv(infile):
    start_end_array = get_first_and_last_datetime(infile)
    # read and write lines one by one (no saving in memory)
    if check_amount_of_measurements.check_if_splitting_is_needed(infile):
        i = check_amount_of_measurements.get_number_of_measurements(infile)
    else:
        i = 1

    for item in range(1, i):

        with open(infile, newline='') as csv_file:
            # skip first line with next
            next(csv_file)
            csv_reader = csv.reader(csv_file, delimiter=',')

            measurement_name = get_measurement_name(infile, item)
            measurement = outfile_validation.check_measurement_name(measurement_name)
            outfile = infile.replace('.csv', '_' + measurement + '_formatted.csv')
            print(outfile)
            if outfile_validation.check_existing_outfile(outfile):
                os.remove(outfile)
            header_handling.write_header(outfile)

            for index, row in enumerate(csv_reader):
                row_list = convert_row(index, row, start_end_array, infile, item)
                write_data_to_outfile(row_list, outfile)
