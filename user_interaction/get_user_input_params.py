import csv

from input_params import input_params


def get_csv_file():
    print("""
    Which CSV file do you want to upload?
    Please put in the absolute path:
    """)
    path = input()
    if input_params.validate_csv_path(path):
        return path
    else:
        get_csv_file()


def get_bucket():
    print("""
    In which bucket do you want to upload the data?
    """)
    return input()
    # add validation method


def ask_for_units():
    print("""
    Are all measurements in the CSV file of the same unit?
    Y - Yes
    N - No
    """)
    return input()


def validate_unit_input(option):
    if option == "Y" or option == "N" \
            or option == "YES" or option == "NO" \
            or option == "y" or option == "n" \
            or option == "yes" or option == "no":
        pass
    else:
        print_invalid_answer()
        validate_unit_input(ask_for_units())


def print_invalid_answer():
    print("Invalid option. Please chose Y or N.")


def get_units(option, infile):
    validate_unit_input(option)
    if option == "Y" or option == "YES" or option == "y" or option == "yes":
        unit_s = get_single_unit()
    else:
        unit_s = get_multiple_units(infile)
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


def ask_for_parameters():
    csv_file = get_csv_file()
    bucket = get_bucket()
    unit_s = get_units(ask_for_units(), csv_file)

    return [csv_file, bucket, unit_s]
