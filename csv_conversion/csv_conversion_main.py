import csv
import os

from csv_conversion import read_write_csv, time_reformatting,\
    check_amount_of_measurements, outfile_validation, header_handling


def convert_row(index, row, start_end_array, infile, item):
    time = time_reformatting.reformat_time(row[0])
    value = row[item]
    start_time = start_end_array[0]  # read first timestamp
    stop_time = start_end_array[1]  # read last timestamp

    # read measurement information from the first line:
    field = "EUR/kWh" # später hier input parameter einfügen
    measurement = read_write_csv.get_measurement_name(infile, item)

    row_list = [['','', index, start_time, stop_time,
                       time, value, field, measurement]]

    return row_list


def convert_csv(infile):
    start_end_array = read_write_csv.get_first_and_last_datetime(infile)

    # check if there is more than 1 measurement in file
    if check_amount_of_measurements.check_if_splitting_is_needed(infile):
        i = check_amount_of_measurements.get_number_of_measurements(infile)
    else:
        i = 1

    # create output file for each measurement
    for item in range(1, i+1):

        with open(infile, newline='') as csv_file:
            # skip first line with next
            next(csv_file)
            csv_reader = csv.reader(csv_file, delimiter=',')

            # validate outfile name and check if it already exists
            measurement_name = read_write_csv.get_measurement_name(infile, item)
            measurement = outfile_validation.check_measurement_name(measurement_name)
            outfile = infile.replace('.csv', '_' + measurement + '_formatted.csv')
            if outfile_validation.check_existing_outfile(outfile):
                os.remove(outfile)

            # write headers
            header_handling.write_header(outfile)

            # read and write lines one by one (no saving in memory)
            for index, row in enumerate(csv_reader):
                row_list = convert_row(index, row, start_end_array, infile, item)
                read_write_csv.write_data_to_outfile(row_list, outfile)

