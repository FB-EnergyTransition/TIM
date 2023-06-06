import csv

import user_interaction.input_validation
from user_interaction import input_validation
from logdata import logdata
from csv_conversion import csv_input_validation


class InputParams:

    def __init__(self):
        self.iv = user_interaction.input_validation.InputValidator()
        self.bucket = ""
        self.infile = ""
        self.units = None
        self.measurement = ""
        self.unit_option = ""

    def get_csv_file(self):
        print("""
        Which CSV file do you want to upload?
        Please put in the absolute or relative path:
        """)
        path = input()

        if self.iv.validate_input_csv_path(path)\
                & csv_input_validation.check_delimiter(path)\
                & csv_input_validation.check_input_timeformat(path)\
                & csv_input_validation.check_valid_values(path):
            self.infile = path
        else:
            self.get_csv_file()

    def get_bucket(self):
        while True:
            print("""
            In which bucket do you want to upload the data?
            """)
            bucket = input()
            try:
                if self.iv.validate_bucket_input(bucket):
                    self.bucket = bucket
                else:
                    self.get_bucket()
                break
            except Exception as e:
                logdata.error_message(e)
                continue

    def get_unit_option(self):
        print("""
        Are all measurements in the CSV file of the same unit?
        Y - Yes
        N - No
        """)
        return input()

    def get_units(self):
        self.unit_option = self.get_unit_option()
        if self.iv.validate_unit_option(self.unit_option):
            if self.unit_option == "Y" or self.unit_option == "YES"\
                    or self.unit_option == "y" or self.unit_option == "yes":
                unit_s = self.get_single_unit()
            else:
                unit_s = self.get_multiple_units()
        else:
            unit_s = []
            self.iv.validate_unit_option(self.get_unit_option())
        self.units = unit_s

    def get_single_unit(self):
        print("""
        Please type in the unit of all measurements in the file:
        """)
        return input()

    def get_multiple_units(self):
        units = []
        with open(self.infile, newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            header = []
            for line in csv_reader:
                header.append(line)
                break
            header[0].pop(0)
            for item in header[0]:
                print("Please type the unit for the measurement "
                      + str(item) + ":")
                unit = input()
                units.append(unit)
        return units

    def get_measurement(self):
        print("""
        Please type in the type of measurement contained in the CSV file:
        """)
        self.measurement = input()

    def get_parameters(self):
        self.get_csv_file()
        self.get_measurement()
        self.get_bucket()
        self.get_units()
