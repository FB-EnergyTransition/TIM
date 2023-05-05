import os


def get_all_converted_csvs():
    csvs = []
    for file in os.listdir('./resources'):
        if file.endswith('_formatted.csv'):
            csvs.append(file)
            print(file)
    return csvs