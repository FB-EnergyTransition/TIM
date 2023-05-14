import os


def get_all_converted_csvs(infile):
    csvs = []
    for file in os.listdir(os.path.dirname(infile)):
        if file.endswith('_formatted.csv'):
            csvs.append(file)
            print(file)
    return csvs
