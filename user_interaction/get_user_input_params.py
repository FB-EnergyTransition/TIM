import csv
from user_interaction import input_validation


def get_csv_file():
    print("""
    Which CSV file do you want to upload?
    Please put in the absolute or relative path:
    """)
    path = input()
    if input_validation.validate_input_csv_path(path):
        return path
    else:
        get_csv_file()


def get_bucket():
    print("""
    In which bucket do you want to upload the data?
    """)
    bucket = input()
    if input_validation.validate_bucket_input(bucket):
        return bucket
    else:
        get_bucket()


def ask_for_units():
    print("""
    Are all measurements in the CSV file of the same unit?
    Y - Yes
    N - No
    """)
    return input()


def print_invalid_answer():
    print("Invalid option. Please chose Y or N.")


def get_units(option, infile):
    if input_validation.validate_unit_option(option):
        if option == "Y" or option == "YES" or option == "y" or option == "yes":
            unit_s = get_single_unit()
        else:
            unit_s = get_multiple_units(infile)
    else:
        unit_s = []
        input_validation.validate_unit_option(ask_for_units())
    return unit_s


def get_single_unit():
    print("""
    Please type in the unit of all measurements in the file:
    """)
    return input()


def get_multiple_units(infile):
    units = []
    with open(infile, newline='') as csv_file:
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


def get_measurement():
    print("""
    Please type in the type of measurement contained in the CSV file:
    """)
    return input()


def ask_for_parameters():
    csv_file = get_csv_file()
    measurement = get_measurement()
    bucket = get_bucket()
    unit_s = get_units(ask_for_units(), csv_file)

    return [csv_file, measurement, bucket, unit_s]
