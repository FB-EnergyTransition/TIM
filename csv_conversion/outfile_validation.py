import os


class OutfileValidator:

    def __init__(self):
        self.outfile = ""
        self.measurement = ""

    def check_existing_outfile(self, outfile):
        self.outfile = outfile
        if os.path.exists(self.outfile):
            return True
        else:
            return False

    def check_measurement_name(self, measurement):
        self.measurement = measurement
        invalid = '<>:"/\\\|?*'
        for char in invalid:
            self.measurement = self.measurement.replace(char, '')

        return self.measurement
