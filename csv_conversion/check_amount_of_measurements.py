import csv


def get_number_of_measurements(infile):
    with open(infile, newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            example_row = row
            break
    return len(example_row)-1


def check_if_splitting_is_needed(infile):
    amount_measurements = get_number_of_measurements(infile)
    if amount_measurements > 1:
        return True
    else:
        return False

