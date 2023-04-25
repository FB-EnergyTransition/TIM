import os


def check_existing_outfile(outfile):
    if os.path.exists(outfile):
        return True
    else:
        return False


def check_measurement_name(measurement):
    invalid = '<>:"/\\\|?*'
    for char in invalid:
        measurement = measurement.replace(char, '')

    return measurement
