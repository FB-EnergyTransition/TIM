import csv
import os

import csv_conversion.time_reformatting
from csv_conversion import read_write_csv,\
    check_amount_of_measurements, outfile_validation, header_handling


class CsvConverter:

    def __init__(self, infile, units):
        self.infile = infile
        self.units = units
        self.csvrw = csv_conversion.read_write_csv.CsvReaderWriter(self.infile)

    def convert_row(self, index, row, start_end_array, item):
        tf = csv_conversion.time_reformatting.TimeFormatter(row[0])
        time = tf.reformat_time()
        value = row[item]
        start_time = start_end_array[0]  # read first timestamp
        stop_time = start_end_array[1]  # read last timestamp

        # check if there is just one or more units
        if type(self.units) is list:
            field = self.units[item-1]
        else:
            field = self.units

        # read measurement information from the first line:
        measurement = self.csvrw.get_measurement_name(item)

        row_list = [['','', index, start_time, stop_time,
                           time, value, field, measurement]]

        return row_list

    def convert_csv(self):
        start_end_array = self.csvrw.get_first_and_last_datetime()

        # check if there is more than 1 measurement in file
        mh = csv_conversion.check_amount_of_measurements.MeasurementHandler(self.infile)
        if mh.check_if_splitting_is_needed():
            i = mh.get_number_of_measurements()
        else:
            i = 1

        # create output file for each measurement
        for item in range(1, i+1):

            with open(self.infile, newline='') as csv_file:
                # skip first line with next
                next(csv_file)
                csv_reader = csv.reader(csv_file, delimiter=',')

                # validate outfile name and check if it already exists
                ov = csv_conversion.outfile_validation.OutfileValidator()
                measurement_name = self.csvrw.get_measurement_name(item)
                measurement = ov.check_measurement_name(measurement_name)
                outfile = self.infile.replace('.csv', '_' + measurement + '_formatted.csv')
                if ov.check_existing_outfile(outfile):
                    os.remove(outfile)

                # write headers
                hh = csv_conversion.header_handling.HeaderHandler(outfile)
                hh.write_header()

                # read and write lines one by one (no saving in memory)

                for index, row in enumerate(csv_reader):
                    row_list = self.convert_row(index, row, start_end_array, item)
                    self.csvrw.write_data_to_outfile(row_list, outfile)


