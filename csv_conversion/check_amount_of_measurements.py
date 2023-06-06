import csv


class MeasurementHandler:

    def __init__(self, infile):
        self.infile = infile

    def get_number_of_measurements(self):
        with open(self.infile, newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                example_row = row
                break
        return len(example_row)-1

    def check_if_splitting_is_needed(self):
        amount_measurements = self.get_number_of_measurements()
        if amount_measurements > 1:
            return True
        else:
            return False

