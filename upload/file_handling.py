import os


class FileHandler:
    def __init__(self, infile):
        self.infile = infile

    def get_all_converted_csvs(self):
        csvs = []
        for file in os.listdir(os.path.dirname(self.infile)):
            if file.endswith('_formatted.csv'):
                csvs.append(file)
                print(file)
        return csvs
